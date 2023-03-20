const { app, BrowserWindow,ipcMain } = require("electron");
const path = require("path");
const {download} = require('electron-dl');
const { spawn } = require('child_process');
require("electron-reload")(__dirname, {
    // Note that the path to electron may vary according to the main file
    electron: require(`${__dirname}/node_modules/electron`),
});
const nativeImage = require('electron').nativeImage;
let appIcon = nativeImage.createFromPath(path.join(__dirname, 'assets', 'appicon.png'));
var winone;

function createWindow() {
    winone = new BrowserWindow({
        maxWidth: 850,
        maxHeight: 600,
        title: 'GestEaves',
        autoHideMenuBar: true,
        icon: appIcon,
        webPreferences: {
            nodeIntegration: false,
            enableRemoteModule: true,
            contextIsolation: true,
            preload: path.join(__dirname,"./pages/preload.js"),
        },
    });
    //NOTE:
    //node integration must be false for security.
    // contextIsolation was false, set to true to enable ipc communication between renderer and main via preload script.
    //winone.setMenu(null);
    winone.loadFile(path.join(__dirname, "./pages/home/home.html"));
    winone.on("closed", () => { });
}

const isDebug =
  process.env.NODE_ENV === 'development' || process.env.DEBUG_PROD === 'true';

if (isDebug) {
  require('electron-debug')();
}

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});

app.whenReady().then(() => {
    createWindow();
    app.on("activate", () => {
        if (BrowserWindow.getAllWindows().length === 0) createMainWindow();
    });
});

ipcMain.on("download",async (event, {payload}) => {
    console.log("here " + payload.url);
    download(BrowserWindow.getFocusedWindow(), payload.url, payload.properties)
    .then(dl => 
        {
        console.log("complete");
        });
    
});

ipcMain.on("gesture",async (event, command) => {
    console.log(command);
    let child; 
    if(command == 'start'){
        console.log('STARTING GESTEASE - Gesture....');
        child = spawn('C:/Users/Hp/anaconda3/envs/Gestease-Gesture/python.exe', ['../python_scripts/gesture/app.py']);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
            result.textContent = data.toString('utf8');
        });
        
        child.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });
        child.on('close', (code) => {
            child.kill('SIGTERM');
            console.log(`child process exited with code ${code}`);
        });
    }else if(command == 'stop'){
        console.log('stopping gestease');
        child.kill('SIGTERM');
    }else if(command == 'train'){
        console.log('TRAINING');
        child = spawn('C:/Users/Hp/anaconda3/envs/Gestease-Gesture/python.exe', ['../python_scripts/gesture/keypoint_csv_from_video.py']);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
            // result.textContent = data.toString('utf8');
        });

        child.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });
        child.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
    }
});

ipcMain.on("voice",async (event, command) => {
    if(command == 'start'){
        console.log('STARTING GESTEASE - Voice....');
        child = spawn('python', ['../python_scripts/voice/speechrec.py', "start"]);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
            result.textContent = data.toString('utf8');
        });
        
        child.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });
        child.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
    }else if(command == 'stop'){
        console.log('STOPPING GESTEASE - voice');
        child.kill('SIGTERM');
    }
});
