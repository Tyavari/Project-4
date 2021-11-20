var button = d3.select("#click-me");
// d3.selectAll("#selDataset").on("change", getData);
var data = new FormData();
function handleClick() {
    console.log("A button was clicked!");
    console.log(document.getElementById("selDataset").value)
    console.log(document.getElementById("selDataset1").value)
    console.log(document.getElementById("selDataset2").value)
    console.log(document.getElementById("selDataset3").value)
    console.log(document.getElementById("selDataset4").value)
    console.log(document.getElementById("selDataset5").value)
    data.append("neighborhood", document.getElementById("selDataset").value)
    data.append("building-type", document.getElementById("selDataset1").value)
    data.append("zip-code", document.getElementById("selDataset2").value)
    data.append("units", document.getElementById("selDataset3").value)
    data.append("sqft", document.getElementById("selDataset4").value)
    data.append("year", document.getElementById("selDataset5").value)
    console.log(data)
}
button.on("click", handleClick);

