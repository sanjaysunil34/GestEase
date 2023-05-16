// var element = document.getElementById('addGestureForm-back');
// element.setAttribute('href', document.referrer);
// element.onclick = function() {
//   history.back();
//   return false;
// }

var element = document.getElementById('addGestureFormButton');
//console.log('Hi');
element.setAttribute('href', document.referrer);
element.onclick = function() {
    var functionality = document.getElementById('func').value;
    var binding = document.getElementById('bind').value;
    // console.log(functionaility);
    // console.log(binding);
    var res = functionality.concat('\n');
    res = res.concat(binding);
    const blob = new Blob([res], {type: "text/plain"});
    const fileUrl = URL.createObjectURL(blob);
    window.Bridge.sendTXTUrl(fileUrl);
    location.replace("./addGesture.html")
  return false;
}
