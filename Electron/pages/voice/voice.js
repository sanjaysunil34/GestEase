var gestease = require('../../linkers/voice');

var voiceBtn = document.getElementById('voice');


voiceBtn.addEventListener('click',(e) => {
    const command = voiceBtn.innerText.toLowerCase();
    gestease(command);
    switch(command){
        case 'start':
            voiceBtn.innerText = "Stop";
            break;
        case 'stop':
            voiceBtn.innerText = "Start";
            break;
    }
});

