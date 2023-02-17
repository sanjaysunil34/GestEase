console.log("Main process working");
console.log("main.js");

const { app, BrowserWindow, Menu } = require("electron");
const path = require("path");
require("electron-reload")(__dirname, {
    // Note that the path to electron may vary according to the main file
    electron: require(`${__dirname}/node_modules/electron`),
});
const nativeImage = require('electron').nativeImage;
let appIcon = nativeImage.createFromPath(path.join(__dirname, 'assets', 'appicon.png'));

function createWindow() {
    const winone = new BrowserWindow({
        maxWidth: 850,
        maxHeight: 600,
        autoHideMenuBar: true,
        icon: appIcon,
        webPreferences: {
            nodeIntegration: true,
            nodeIntegrationInWorker: true,
            nodeIntegrationInSubFrames: true,
            enableRemoteModule: true,
            contextIsolation: false,
        },
    });

    winone.loadFile(path.join(__dirname, "./pages/home/home.html"));

    winone.on("closed", () => {
        winone = null;
    });
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
