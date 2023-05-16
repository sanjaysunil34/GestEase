var gestureBtn = document.getElementById('gesture');
var sidePane = document.getElementById('grid-left');
gestureBtn.addEventListener('click',(e) => {
    const command = gestureBtn.innerText.toLowerCase();
    //console.log(window.Bridge)
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



