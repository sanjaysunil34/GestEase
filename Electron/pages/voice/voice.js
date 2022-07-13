var gestease = require('../../linkers/voice');
// var createVoiceManualWindow = require('../../main')

// function createVoiceManualWindow() {
//     const electron = require("electron");
//     const BrowserWindow = electron.BrowserWindow;
//     const win = new BrowserWindow({
//         width: 800,
//         height: 600,
//         webPreferences: {
//         nodeIntegration: true,
//         enableRemoteModule: true
//         }
//         })
    
//       win.loadURL('../home/home.html');
//     }

var voiceBtn = document.getElementById('voice');
// var voiceManualBtn = document.getElementById('voice-manual');


voiceBtn.addEventListener('click',(e) => {
    const command = voiceBtn.innerText.toLowerCase();
    gestease(command);
    console.log(command);
    switch(command){
        case 'start':
            voiceBtn.innerText = "Stop";
            break;
        case 'stop':
            voiceBtn.innerText = "Start";
            break;
    }
});

// voiceManualBtn.addEventListener('click',(e) => {
//     console.log('Hii');
//     createVoiceManualWindow();
// });