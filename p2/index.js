function gobrrr(){
    init();

    let name = vnume(document.forms['mario'].elements['name'].value);
    let data = vdata(document.forms['mario'].elements['data'].value);
    let varsta = vvrst(document.forms['mario'].elements['varsta'].value);
    let email = vemail(document.forms['mario'].elements['email'].value);

    let check = true;
    let eroare = "Campurile ";

    if (name === false){
        document.getElementById("name_div").style.border="1px solid red";
        //document.getElementById("eroare").style.display="block";
        check = false;
        eroare = eroare + " nume";
    }

    if (data === false){
        document.getElementById("date_div").style.border="1px solid red";
        //document.getElementById("eroare").style.display="block";
        if (check === false) {
            eroare = eroare + ",";
        }
        check = false;
        eroare = eroare + " data";
    }

    if (varsta === false){
        document.getElementById("age_div").style.border="1px solid red";
        //document.getElementById("eroare").style.display="block";
        if (check === false) {
            eroare = eroare + ",";
        }
        check = false;
        eroare = eroare + " varsta";
    }

    if (email === false){
        document.getElementById("email_div").style.border="1px solid red";
        //document.getElementById("eroare").style.display="block";
        if (check === false) {
            eroare = eroare + ",";
        }
        check = false;
        eroare = eroare + " email";
    }

    if (check === false){
        eroare = eroare + " nu sunt completate corect";
        document.getElementById("eroare").innerHTML = eroare;
        document.getElementById("eroare").style.display="block";
    }
    else{
        document.getElementById("succes").style.display="block";
    }
    return false;
}

function vnume(nume){
    return nume.length !== 0;
    //no discrimination here, anybody can have any name they wish
}

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
    if (vrst.length === 0){
        return false;
    }
    return !(isNaN(vrst) || vrst < 1);
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

function init(){
    document.getElementById("name_div").style.border="none";
    document.getElementById("age_div").style.border="none";
    document.getElementById("email_div").style.border="none";
    document.getElementById("date_div").style.border="none";
    document.getElementById("eroare").style.display="none";
    document.getElementById("succes").style.display="none";
}