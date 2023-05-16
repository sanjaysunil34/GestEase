let tableRef = document.getElementById("table-body");

window.Bridge.getDataGesture().then((data) => {
    let dbdata = JSON.parse(data);
    dbdata = dbdata["_default"]
    let ids = Object.keys(dbdata)
    console.log(ids);

    ids.forEach((id) => {
        console.log(dbdata[id]);
        let rowContent = "<tr class='table-row'><th scope='row'><img width='150' height='150' src=\"../../images/" + dbdata[id]["image"]+ "\"/></th><td style='vertical-align: middle'><div>" + dbdata[id]["action"] + "</div></td></tr>";
        let row = tableRef.insertRow(tableRef.rows.length);
        row.innerHTML = rowContent;
    })   
});

