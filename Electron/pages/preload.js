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

let sendImageUrl  = (url) => {
    console.log(url);
    const filename = "sanjay.jpg";
    const directory = path.join(__dirname,'../images/');
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

// ipcRenderer.on('gesture-executed', (event, data) => {
//     console.log(`Received data in renderer process: ${data}`);
//     const gestureExec = document.getElementById('gesture-executed');
//     gestureExec.innerHTML = data;
// });

let indexBridge = {
    sendUrl,
    sendImageUrl,
    sendTXTUrl,
    gestureControl,
    voiceControl
}

contextBridge.exposeInMainWorld("Bridge",indexBridge);