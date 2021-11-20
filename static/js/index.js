var button = d3.select("#click-me");
d3.selectAll("#selDataset").on("change", getData);

// Define getData, which updates all plots and metadata section when change is detected in the dropdown 
function getData(){

 // On change of dropdown menu, get the 'value' (index) of the selected element
    var dropdownMenu = d3.select("#selDataset");
    var dataset = dropdownMenu.property("value");
}
button.on("click", function() {
    d3.select(".giphy-me").html("<img src='https://gph.to/2Krfn0w' alt='giphy'>");
  });
function handleClick() {
    console.log("A button was clicked!");
    // We can use d3 to see the object that dispatched the event
    // console.log(d3.event.target);
}
button.on("click", handleClick);