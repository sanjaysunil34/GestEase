const { contextBridge, ipcRenderer} = require("electron");
const path = require('path');

let sendUrl  = (url) => {
    console.log(url);
    const filename = "recording.mp4";
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

let sendTXTUrl  = (url) => {
    console.log(url);
    const filename = "file.txt";
    const directory = path.join(__dirname,'../gestureFile/');
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

let getDataVoice = () => ipcRenderer.invoke("load-file-voice");
let getDataGesture = () => ipcRenderer.invoke("load-file-gesture");
let indexBridge = {
    sendUrl,
    sendTXTUrl,
    gestureControl,
    voiceControl,
    getDataVoice,
    getDataGesture
}

contextBridge.exposeInMainWorld("Bridge",indexBridge);