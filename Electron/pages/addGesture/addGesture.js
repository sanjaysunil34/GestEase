function startRecording(thisButton){
	navigator.mediaDevices.getUserMedia({
			audio: false,
			video: true,
		}).then((mediaStream) => {
			let chunks = [];
			const mediaRecorder =
			new MediaRecorder(mediaStream);

			//Make the mediaStream global
			window.mediaStream = mediaStream;
			//Make the mediaRecorder global
			window.mediaRecorder = mediaRecorder;

			mediaRecorder.start();
			const duration = 22000;
			setTimeout(function(){
				stopRecording();
				thisButton.disabled = false;
			},duration);
			mediaRecorder.ondataavailable = (e) => {
				chunks.push(e.data);
			};
			mediaRecorder.onstop = () => {
				const blob = new Blob(
					chunks, {
						type: "video/mp4" 
					});
				chunks = [];
				
				const recordedMediaURL = URL.createObjectURL(blob);
				window.Bridge.sendUrl(recordedMediaURL);
			}
			const webCamContainer = document.getElementById("web-cam-container");
			webCamContainer.srcObject = mediaStream;
			document.getElementById(
				`vid-record-status`)
				.innerText = "Recording";
			thisButton.disabled = true;
		})
}

function stopRecording() {
	window.mediaRecorder.stop();
	window.mediaStream.getTracks()
	.forEach((track) => {
		track.stop();
		track.enabled = false;
	});
	document.getElementById(
		`vid-record-status`)
		.innerText = "Recording done!";
	window.Bridge.gestureControl("train");
	location.replace("./loadingPage.html");
}

var element = document.getElementById('addgesture-back');
element.setAttribute('href', document.referrer);
element.onclick = function() {
  history.back();
  return false;
}