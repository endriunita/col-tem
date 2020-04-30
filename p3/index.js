window.remainingmoves = 2;
window.lastmove = -1;
window.currentmove = -1;
window.count = 0;
window.busy = 0;

window.board = [ "aku.jpg", "bluto.JPG", "bufny.jpg", "covid19.JPG", "devil.JPG", "aku.jpg", "duchess.jpg", "thanos.png", "devil.JPG", "bluto.JPG", "duchess.jpg", "vio.JPG", "vio.JPG", "covid19.JPG", "thanos.png", "bufny.jpg"];
window.numberboard = [11, 55, 88, 44, 33, 11, 77, 99, 33, 55, 77, 22, 22, 44, 99, 88];

cells = $('.cell')

$('button').click(function() {
    $('.cell').css('backgroundImage', 'none');
    window.remainingmoves = 2;
    window.lastmove = -1;
    window.currentmove = -1;
    window.count = 0;
    window.busy = 0;
    $('#announcement').css('display', 'none');
});

$(document).ready(function() {
    window.board = shuffle(window.board);
    window.numberboard = shuffle(window.numberboard);
});

cells.click( function() {
   let index = $(this).index() + $(this).parent().index() * 4;
    if (window.busy === 1){
        return;
    }

    if(typeof $(this) !== 'undefined')
    {
        window.currentmove = index;
        $(this).css('backgroundImage', "url('" + window.board[index] + "')");

        brr(index);
    }
});

function brr(i){

    if (window.remainingmoves === 1){
        window.busy = 1;
        if (window.board[i] === window.board[lastmove] && i !== window.lastmove){
            count ++;
            window.busy = 0;
            window.remainingmoves = 2;
            if(count === 8){
                $('#announcement').css('display', 'block');
            }
        }
        else{
            setTimeout(function(){
                $(cells.get(window.lastmove)).css('backgroundImage', 'none');
                $(cells.get(i)).css('backgroundImage', 'none');
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
    let j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}