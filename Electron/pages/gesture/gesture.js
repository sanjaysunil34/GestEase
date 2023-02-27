var gestureBtn = document.getElementById('gesture');
gestureBtn.addEventListener('click',(e) => {
    const command = gestureBtn.innerText.toLowerCase();
    window.Bridge.gestureControl(command);
    switch(command){
        case 'start':
            gestureBtn.innerText = "Stop";
            break;
        case 'stop':
            gestureBtn.innerText = "Start";
            break;
    }
});