let tableRef = document.getElementById("table-body");

const gestures = [{
    "img": "image",
    "action": "Plays media"
},{
    "img": "image",
    "action": "Pause media"
},{
    "img": "image",
    "action": "Increase the volume"
},{
    "img": "image",
    "action": "Decreases the volume"
},{
    "img": "image",
    "action": "Go back few seconds"
},
{
    "img": "image",
    "action": "Enter full screen"
},{
    "img": "image",
    "action": "Mutes the media"
},{
    "img": "image",
    "action": "Close the app"
},{
    "img": "image",
    "action": "Switch tabs"
}];

for (let index = 0; index < gestures.length; index++) {
    let rowContent = "<tr><th scope='row'>" + gestures[index]["img"]+ "</th><td>" + gestures[index]["action"] + "</td></tr>";
    let row = tableRef.insertRow(tableRef.rows.length);
    row.innerHTML = rowContent;    
}