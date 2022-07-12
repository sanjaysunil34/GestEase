console.log('Main process working');
console.log('main.js');


const electron = require("electron");
const {PythonShell} = require('python-shell')
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const electronIpcMain = require('electron').ipcMain;
const path = require("path");
const url = require("url");

let winone;

function createWindow() {
    winone = new BrowserWindow({
      autoHideMenuBar: true,
        webPreferences: {
          nodeIntegration: true,          
          nodeIntegrationInWorker: true,
            nodeIntegrationInSubFrames: true,
            enableRemoteModule: true,
            contextIsolation: false
        }
    });
    
    winone.loadURL(url.format({
        pathname: path.join(__dirname, './pages/home/home.html'),
        protocol: 'file',
        slashes: true
    }))
    
    winone.webContents.openDevTools();

    winone.on('closed', () => {
        win = null;
    })
}

function record_speech  () {
    // var btnstatus = document.getElementById('voice').innerText;
    // var options = {
    //     scriptPath: path.join(__dirname,'./python/'),
    //     mode: 'text',
    // }
    
    // PythonShell.run('main.py', options, function (err, results) {
    //     if (err) throw err;
    //     console.log('results: ', results);
    //   }); 
    
    var options = {
        scriptPath : path.join(__dirname, './python'),
        args : [],
        //mode: "json"
    };
    
    let pyshell = new PythonShell('main.py', options);
    
    pyshell.run(function(message) {
        console.log(message);
        console.log(typeof message);
    });
}


app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
});

app.on('activate', () => {
    if(win == null) {
        createWindow()
    }
});