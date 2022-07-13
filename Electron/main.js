console.log('Main process working');
console.log('main.js');


const electron = require("electron");
require('electron-reload')(__dirname, {
    // Note that the path to electron may vary according to the main file
    electron: require(`${__dirname}/node_modules/electron`)
});
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