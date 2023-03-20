// function startRecording(thisButton){
// 	navigator.mediaDevices.getUserMedia({
// 			audio: false,
// 			video: true,
// 		}).then((mediaStream) => {
// 			let chunks = [];
// 			const mediaRecorder =
// 			new MediaRecorder(mediaStream);

// 			//Make the mediaStream global
// 			window.mediaStream = mediaStream;
// 			//Make the mediaRecorder global
// 			window.mediaRecorder = mediaRecorder;

// 			mediaRecorder.start();
// 			const duration = 22000;
// 			setTimeout(function(){
// 				stopRecording();
// 				thisButton.disabled = false;
// 			},duration);
// 			mediaRecorder.ondataavailable = (e) => {
// 				chunks.push(e.data);
// 			};
// 			mediaRecorder.onstop = () => {
// 				const blob = new Blob(
// 					chunks, {
// 						type: "video/mp4" 
// 					});
// 				chunks = [];
				
// 				const recordedMediaURL = URL.createObjectURL(blob);
// 				window.Bridge.sendUrl(recordedMediaURL);
// 			}
// 			const webCamContainer = document.getElementById("web-cam-container");
// 			webCamContainer.srcObject = mediaStream;
// 			document.getElementById(
// 				`vid-record-status`)
// 				.innerText = "Recording";
// 			thisButton.disabled = true;
// 		})
// }

// function stopRecording() {
// 	window.mediaRecorder.stop();
// 	window.mediaStream.getTracks()
// 	.forEach((track) => {
// 		track.stop();
// 		track.enabled = false;
// 	});
// 	document.getElementById(
// 		`vid-record-status`)
// 		.innerText = "Recording done!";
// 	window.Bridge.gestureControl("train");
// }

// var element = document.getElementById('addgesture-back');
// element.setAttribute('href', document.referrer);
// element.onclick = function() {
//   history.back();
//   return false;
// }

const canvas = document.querySelector('.canvas')
const video = document.querySelector('.video')

function startRecording(thisButton){
	navigator.mediaDevices.getUserMedia({video: true})
	.then(stream => {
		video.srcObject = stream;
		video.play();
	})

	canvas.getContext("2d").drawImage(video, 0, 0, canvas.clientWidth, canvas.height)
	let image_data_url = canvas.toDataURL("image/png")
	console.log(image_data_url);
	const link = document.createElement("a")
	link.href = image_data_url
	// window.Bridge.sendImageUrl(image_data_url);

	link.download = "sanjay.png"
	document.body.appendChild(link)
	link.click()
	document.body.removeChild(link)
}