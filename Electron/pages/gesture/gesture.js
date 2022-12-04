var gestease_gesture = require('../../linkers/gesture');

var gestureBtn = document.getElementById('gesture');
// var voiceManualBtn = document.getElementById('voice-manual');


gestureBtn.addEventListener('click',(e) => {
    const command = gestureBtn.innerText.toLowerCase();
    gestease_gesture(command);
    switch(command){
        case 'start':
            gestureBtn.innerText = "Stop";
            break;
        case 'stop':
            gestureBtn.innerText = "Start";
            break;
    }
});