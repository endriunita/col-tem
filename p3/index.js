window.remainingmoves = 2;
window.lastmove = -1;
window.currentmove = -1;
window.count = 0;
window.busy = 0;

window.board = [ "aku.jpg", "bluto.JPG", "bufny.jpg", "covid19.JPG", "devil.JPG", "aku.jpg", "duchess.jpg", "thanos.png", "devil.JPG", "bluto.JPG", "duchess.jpg", "vio.JPG", "vio.JPG", "covid19.JPG", "thanos.png", "bufny.jpg"];
window.numberboard = [11, 55, 88, 44, 33, 11, 77, 99, 33, 55, 77, 22, 22, 44, 99, 88]

window.node = document.getElementsByClassName("cell");
window.nodes = [...window.node];

function startGame(){
    window.board = shuffle(window.board);
    window.numberboard = shuffle(window.numberboard);

    let len = nodes.length;
    var i;
    b = document.getElementsByTagName("button")[0];
    b.disabled = true;
    for (i = 0; i < len; i++){
        window.nodes[i].index = i;
        window.nodes[i].addEventListener("click", displayEvt, false);
    }
}

function displayEvt(evt){

    if (window.busy === 1){
        return;
    }

    if (typeof window.nodes[evt.target.index] !== 'undefined') {
        window.currentmove = evt.target.index;
        window.nodes[evt.target.index].style.backgroundImage = "url(' " + window.board[evt.target.index] + "')"; //switch these 2 for numbers
        //window.nodes[evt.target.index].innerText = window.numberboard[evt.target.index];                      //
        brr(evt.target.index);
    }
}

function brr(i){

    if (window.remainingmoves === 1){
        window.busy = 1;
        if (window.board[i] === window.board[lastmove] && i !== window.lastmove){                     //switch there 2 for numbers
  //    if (window.numberboard[i] === window.numberboard[lastmove] && i !== window.lastmove){         //
            count ++;
            window.busy = 0;
            window.remainingmoves = 2;
            if(count === 8){
                document.getElementById('announcement').style.display="block";
            }
        }
        else{
            setTimeout(function(){
                //window.nodes[i].innerText = "";                                                   //
                //window.nodes[window.lastmove].innerText = "";                                     //
                window.nodes[i].setAttribute("style", " background-image: none ");                  //switch these 4 for
                window.nodes[window.lastmove].setAttribute("style", " background-image: none ");    //      numbers
                window.busy = 0;
            }, 2000);
            window.remainingmoves = 2;
        }
    }
    else{
        if (window.remainingmoves === 2){
            window.remainingmoves--;
            window.lastmove = i;
        }
    }
}

//shuffle the array for better functioning game
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}