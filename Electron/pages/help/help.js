var element = document.getElementById('help-back');
element.setAttribute('href', document.referrer);
element.onclick = function() {
  history.back();
  return false;
}