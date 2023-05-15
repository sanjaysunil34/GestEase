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


window.Bridge.getData().then((data) => {
    let dbdata = JSON.parse(data);
    dbdata = dbdata["_default"]
    let ids = Object.keys(dbdata)
    console.log(ids);

    ids.forEach((id) => {
        console.log(dbdata[id]);
        let rowContent = "<tr><th scope='row'><img width='200' src=\"../../images/" + dbdata[id]["image"]+ "\"/></th><td style='vertical-align: middle'><div>" + dbdata[id]["action"] + "</div></td></tr>";
        let row = tableRef.insertRow(tableRef.rows.length);
        row.innerHTML = rowContent;
    }) 
        
        
    
});

