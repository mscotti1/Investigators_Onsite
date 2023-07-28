let display_1 = true;
let display_2 = false;
let display_3 = false;

let total_evidence = 6;

let found_1 = false;
let found_2 = false;
let found_3 = false;
let found_4 = false;
let found_5 = false;
let found_6 = false;
let first_find = true;

info_list = [
    "This is evidence 1.",
    "Wow some good info from evidence 2.",
    "Would ya look at that more info from evidence 3.",
    "Some superb clues from evidence 4.",
    "These criminals left a lot of clues with evidence 5.",
    "Good thing you are a master detective and could spot evidence 6."
]

function display_image_1(){
    display_1 = true;
    display_2 = false;
    display_3 = false;
    changeImage();
}

function display_image_2(){
    display_1 = false;
    display_2 = true;
    display_3 = false;
    changeImage();
}

function display_image_3(){
    display_1 = false;
    display_2 = false;
    display_3 = true;
    changeImage();
}

function changeImage() {
    const image1 = document.querySelector('#image1');
    const image2 = document.querySelector('#image2');
    const image3 = document.querySelector('#image3');

    const button_up = document.querySelector('#up');
    const button_right = document.querySelector('#right');
    const button_down = document.querySelector('#down');
    const button_left = document.querySelector('#left');

    const ev1 = document.querySelector('#ev1');
    const ev2 = document.querySelector('#ev2');
    const ev3 = document.querySelector('#ev3');
    const ev4 = document.querySelector('#ev4');
    const ev5 = document.querySelector('#ev5');
    const ev6 = document.querySelector('#ev6');

    console.log(ev6.getAttribute('class'))


    if (display_1 == true) {
        image1.style.display = 'block';
        image2.style.display = 'none';
        image3.style.display = 'none';

        button_up.style.display = 'block';
        if (button_right.getAttribute('class') !=  'hidden'){
            button_right.style.display = 'block';
        }
        button_down.style.display = 'none';
        button_left.style.display = 'none';


        if (ev1.getAttribute('class') != 'hidden'){
            ev1.style.display = 'block';
        }
        if (ev2.getAttribute('class') != 'hidden'){
            ev2.style.display = 'block';
        }
        ev3.style.display = 'none';
        ev4.style.display = 'none';
        ev5.style.display = 'none';
        ev6.style.display = 'none';
        
    } 
    else if (display_2 == true){
        image1.style.display = 'none';
        image2.style.display = 'block';
        image3.style.display = 'none';

        button_up.style.display = 'none';
        button_right.style.display = 'none';
        button_down.style.display = 'none';
        button_left.style.display = 'block';

        ev1.style.display = 'none';
        ev2.style.display = 'none';

        if (ev3.getAttribute('class') != 'hidden'){
            ev3.style.display = 'block';
        }
        if (ev4.getAttribute('class') != 'hidden'){
            ev4.style.display = 'block';
        }
        ev5.style.display = 'none';
        ev6.style.display = 'none';
    }
    else if (display_3 == true){
        image1.style.display = 'none';
        image2.style.display = 'none';
        image3.style.display = 'block';

        button_up.style.display = 'none';
        button_right.style.display = 'none';
        button_down.style.display = 'block';
        button_left.style.display = 'none';

        ev1.style.display = 'none';
        ev2.style.display = 'none';
        ev3.style.display = 'none';
        ev4.style.display = 'none';

        if (ev5.getAttribute('class') != 'hidden'){
            ev5.style.display = 'block';
        }
        if (ev6.getAttribute('class') != 'hidden'){
            ev6.style.display = 'block';
        }
    }
}

function display_info(ev){
    const info_box = document.querySelector('.info-box');
    if (ev == ev1){
        found_1 = true;
        info_box.innerHTML = info_list[0];
    }
    else if (ev == ev2){
        found_2 = true;
        info_box.innerHTML = info_list[1];
    }
    else if (ev == ev3){
        found_3 = true;
        info_box.innerHTML = info_list[2];
    }
    else if (ev == ev4){
        found_4 = true;
        info_box.innerHTML = info_list[3];
    }
    else if (ev == ev5){
        found_5 = true;
        info_box.innerHTML = info_list[4];
    }
    else if (ev == ev6){
        found_6 = true;
        info_box.innerHTML = info_list[5];
    }
    reveal_continue();
}

function reveal_continue(){
    const button_continue = document.querySelector('#continue');
    if (found_1 == true && found_2 == true && found_3 == true && found_4 == true && found_5 == true && found_6 == true){
        if (first_find == true){
            button_continue.style.display = 'block';
            alert("You found all the evidence!");
            first_find = false;
        }
    }
}