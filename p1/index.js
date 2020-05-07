
function go(){
    let e = document.getElementById("source");
    let val = e.options[e.selectedIndex].value;
    e.options[e.selectedIndex].remove();
    let dest = document.getElementById("destination");
    let newoption = document.createElement("option");
    newoption.value = newoption.text = val;
    dest.add(newoption);
}

function fo(){
    let e = document.getElementById("destination");
    let val = e.options[e.selectedIndex].value;
    e.options[e.selectedIndex].remove();
    let dest = document.getElementById("source");
    let newoption = document.createElement("option");
    newoption.value = newoption.text = val;
    dest.add(newoption);
}
