
function vdata(data){
    if (data.length === 0){
        return false;
    }
    let lol = data.split('/');
    if (isNaN(lol[0]) || isNaN(lol[1]) || isNaN(lol[2])){
        return false;
    }
    return !(lol[0] < 1 || lol[0] > 31 || lol[1] < 1 || lol[1] > 12 || lol[2] < 0 || lol[2].length === 0);
}

function vvrst(vrst){
    return (isNaN(vrst) || vrst < 1);
}

function vemail(email){
    if (email.length === 0){
        return false;
    }
    let lol = email.split('@');
    if (lol.length !== 2 ){
        return false;
    }
    if(lol[1].length < 1 || lol[0].length < 1){
        return false;
    }
    let bruh = lol[1].split('.');
    try{
        return !(bruh[0].length < 1 || bruh[1].length < 1);
    }
    catch(err){
        return false;
    }

}

$('#mario').submit((event) => {
    event.preventDefault();
});

init();

function init(){
    $('#eroare').css('display', 'none');
    $('#succes').css('display', 'none');
}

function checkForMeaning(string){
    return string.includes("a") || string.includes("e");
}

function lastCheck() {
    if ( !checkForMeaning($('#eroare').text().split(":")[1]) ){
        $('#eroare').css('display', 'none');
        $('#succes').css('display', 'block');
    }
}

$('#name').change( () => {
    let message = 'Campuri completate gresit: ';
    value = $('#name').val();

    if ( ! (value.match('^[a-zA-Z]{3,16}$')) || value.length === 0){
        // THAT AINT NO NAME
        $('#succes').css('display', 'none');
        $('#name_div').css('border', '1px solid red');
        let eroare = $('#eroare');
        eroare.css('display', 'block');
        if ( eroare.text().length === 0) {
            eroare.append(message + "nume").show();
        }
        else eroare.append(", nume").show();
    }
    else {
        while($('#eroare').text().includes('nume')){
            $('#eroare').text($('#eroare').text().replace('nume',''));
        }
        lastCheck();
        $('#name_div').css('border', 'none');
    }
});

$('#data').change( () => {
    let message = 'Campuri completate gresit: ';
    value = $('#data').val();

    if (vdata(value) === false || value.length === 0){
        $('#succes').css('display', 'none');
        $('#date_div').css('border', '1px solid red');
        let eroare = $('#eroare');
        eroare.css('display', 'block');
        if ( eroare.text().length === 0) {
            eroare.append(message + "data").show();
        }
        else eroare.append(", data").show();
    }
    else{
        while($('#eroare').text().includes('data')){
            $('#eroare').text($('#eroare').text().replace('data',''));
        }
        // $('#eroare').text($('#eroare').text().replace('data', ''));
        lastCheck();
        $('#date_div').css('border', 'none');
    }
});

$('#varsta').change( () => {
    let message = 'Campuri completate gresit: ';
    value = $('#varsta').val();

    if (vvrst(value) === true){
        $('#succes').css('display', 'none');
        $('#age_div').css('border', '1px solid red');
        let eroare = $('#eroare');
        eroare.css('display', 'block');
        if ( eroare.text().length === 0) {
            eroare.append(message + "varsta").show();
        }
        else eroare.append(", varsta").show();
    }
    else{

        while($('#eroare').text().includes('varsta')){
            $('#eroare').text($('#eroare').text().replace('varsta',''));
        }
        lastCheck();
        $('#age_div').css('border', 'none');
    }
});

$('#email').change( () => {
    let message = 'Campuri completate gresit: ';
    value = $('#email').val();

    if (!vemail(value) || value.length === 0){
        $('#succes').css('display', 'none');
        $('#email_div').css('border', '1px solid red');
        let eroare = $('#eroare');
        eroare.css('display', 'block');
        if ( eroare.text().length === 0) {
            eroare.append(message + "email").show();
        }
        else eroare.append(", email").show();
    }
    else{

        while($('#eroare').text().includes('email')){
            $('#eroare').text($('#eroare').text().replace('email',''));
        }
        lastCheck();
        $('#email_div').css('border', 'none');
    }
});



