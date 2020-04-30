
$('#source').dblclick(() => {
    console.log("hello from source");
    let option = $("#source option:selected");
    $("#destination").append(option);
});

$('#destination').dblclick( () => {
    var option = $("#destination option:selected");
    $('#source').append(option);
});

