// var element = document.getElementById('addGestureForm-back');
// element.setAttribute('href', document.referrer);
// element.onclick = function() {
//   history.back();
//   return false;
// }

var element = document.getElementById('addGestureFormButton');
console.log('Hi');
element.setAttribute('href', document.referrer);
element.onclick = function() {
    var functionaility = document.getElementById('func').value;
    var binding = document.getElementById('bind').value;
    console.log(functionaility);
    console.log(binding);
    var res = functionaility.concat('\n');
    res = res.concat(binding);
    const blob = new Blob([res], {type: "text/plain"});
    const fileUrl = URL.createObjectURL(blob);
    window.Bridge.sendTXTUrl(fileUrl);
    location.replace("./addGesture.html")
  return false;
}

// var targArea = document.getElementById("keyPrssInp");
// targArea.addEventListener('keydown',  reportKeyEvent);
// class reportKeyEvent {
//   constructor(zEvent) {
//     var keyStr = ["Control", "Shift", "Alt", "Meta"].includes(zEvent.key) ? "" : zEvent.key + " ";
//     var reportStr = "The " +
//       (zEvent.ctrlKey ? "Control " : "") +
//       (zEvent.shiftKey ? "Shift " : "") +
//       (zEvent.altKey ? "Alt " : "") +
//       (zEvent.metaKey ? "Meta " : "") +
//       keyStr + "key was pressed.";
//     console.log(reportStr);
//     $("#statusReport").text(reportStr);

//     zEvent.stopPropagation();
//     zEvent.preventDefault();
//   }
// }
// const selectedKey1 = () => {
//   const key = document.getElementById("key1");
//   if(key.value !== "Choose key"){

//   }
//   console.log(key.value);
// }
// const selectedKey2 = () => {
//   const key = document.getElementById("key2");
//   if(key.value !== "Choose key"){

//   }
//   console.log(key.value);
// }
// const selectedKey3 = () => {
//   const key = document.getElementById("key3");
//   if(key.value !== "Choose key"){

//   }
//   console.log(key.value);
// }
