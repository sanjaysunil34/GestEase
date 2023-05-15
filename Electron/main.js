const { app, BrowserWindow,ipcMain } = require("electron");
const path = require("path");
const fs = require("fs");
const {download} = require('electron-dl');
const { spawn } = require('child_process');
const treeKill = require('tree-kill');
const { exit } = require("process");
require("electron-reload")(__dirname, {
    // Note that the path to electron may vary according to the main file
    electron: require(`${__dirname}/node_modules/electron`),
});
const nativeImage = require('electron').nativeImage;
let appIcon = nativeImage.createFromPath(path.join(__dirname, 'assets', 'appicon.png'));
var winone;

function createWindow() {
    winone = new BrowserWindow({
        minWidth: 1064,
        minHeight: 688,
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
    winone.on("closed", () => { exit()});
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

let child; 
ipcMain.on("gesture",async (event, command) => {
    if(command == 'start'){
        console.log('STARTING GESTEASE - Gesture....');

        child = spawn('python', ['../python_scripts/gesture/app-test.py']);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
        });
        
        child.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });
        child.on('close', (code) => {
            child.kill('SIGTERM');
            console.log(`child process exited with code ${code}`);
            
        });
    }else if(command == 'stop'){        
        if (child) {
            treeKill(child.pid, "SIGTERM", (err) => {
              if (err) {
                console.error(err);
              } else {
                console.log("Child process terminated successfully");
              }
            });
          }
    }else if(command == 'train'){
        console.log('TRAINING');
        child = spawn('python', ['../python_scripts/gesture/keypoint_csv_from_video.py']);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
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
        //var loc = window.location.pathname;
        //console.log(path.resolve(__dirname, '..'));
        var parent = path.resolve(__dirname, '..');
        var reqPath = parent + '\\python_scripts\\voice\\speechrec.py'
        child = spawn('python', [reqPath, "start"]);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
            //result.textContent = data.toString('utf8');
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

function openFile() {
    return new Promise((resolve, reject) => {
        fs.readFile("../python_scripts/gesture/db.json", "utf-8", (error, data) => {
            if (error) {
                console.log('reject: ' + error); // Testing
                reject(error);
            } else {
                console.log('resolve: ' + data); // Testing
                resolve(data)
            }
        });
    });
}

ipcMain.handle('load-file', async (event, message) => {
    return await openFile()
        .then((data) => {
            console.log('handle: ' + data); // Testing
            return data;
        })
        .catch((error) => {
            console.log('handle error: ' + error); // Testing
            return 'Error Loading Log File';
        })
});