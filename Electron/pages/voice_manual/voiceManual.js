

// window.Bridge.getDataVoice().then((data) => {
//     let tableRef = document.getElementById("table-body");
//     let dbdata = JSON.parse(data);
//     dbdata = dbdata["_default"]
//     console.log(dbdata)
//     let ids = Object.keys(dbdata)
//     console.log(ids);

//     ids.forEach((id) => {
//         console.log(dbdata[id]);
//         let rowContent = "<tr class='table-row'><th scope='row'>" + dbdata[id]["action"]+ "</th><td style='vertical-align: middle'><div>" + dbdata[id]["keys"] + "</div></td></tr>";
//         let row = tableRef.insertRow(tableRef.rows.length);
//         row.innerHTML = rowContent;
//     })   
// });