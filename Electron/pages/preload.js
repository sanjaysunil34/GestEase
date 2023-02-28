const { contextBridge, ipcRenderer} = require("electron");
const path = require('path');

let sendUrl  = (url) => {
    console.log(url);
    const filename = "irene.mp4";
    const directory = path.join(__dirname,'../recording/');
    ipcRenderer.send('download',{
        payload: {
            url,
            properties: {
               filename,
               directory
            }
        }
    });
}

let gestureControl = (command) => {
    ipcRenderer.send('gesture',command);
}

let voiceControl = (command) => {
    ipcRenderer.send('voice',command);
}

let indexBridge = {
    sendUrl,
    gestureControl,
    voiceControl
}

contextBridge.exposeInMainWorld("Bridge",indexBridge);