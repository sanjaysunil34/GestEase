var element = document.getElementById('addVoiceFormButton');
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