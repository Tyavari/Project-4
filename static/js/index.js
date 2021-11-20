var button = d3.select("#click-me");
d3.selectAll("#selDataset").on("change", getData);

function handleClick() {
    console.log("A button was clicked!");
    // We can use d3 to see the object that dispatched the event
    // console.log(d3.event.target);
}
button.on("click", handleClick);