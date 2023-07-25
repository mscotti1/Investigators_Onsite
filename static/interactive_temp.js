let id1 = "#option_L0_1";
let id2 = "#option_R0_1";

const dialogue_start = [
    { sender: 'heard', text: "ME? MURDER? NEVER!" },
    { sender: 'said', text: "Definitely, something a murderer would say..." },
    { sender: 'heard', text: "But I am being framed. FRAMED I SAY!" },
    { sender: 'said', text: "*Gasp* I never considered this! Who do you think is framing you?" },
    { sender: 'heard', text: "I think I remember seeing Joe that day." },
    { sender: 'heard', text: "Yea!"}, 
    { sender: 'heard', text: "He was definitely the last person to see Beck alive before me!"},
    { sender: 'said', text: "-_-" },
    { sender: 'said', text: "Do you hear yourself?" },
    { sender: 'said', text: "Straight to jail. Do not pass go." },
    { sender: 'heard', text: "Man, why did you have to pretend to be on my side. T_T" },
];

const message_container = document.querySelector('.talk-box');

const right_dia_1 = [
    { sender: 'heard', text: "SAVE ME FROM JAIL TIME" },
    { sender: 'said', text: "Choosing right" },
    { sender: 'heard', text: "Please bestie ;)" }
];

const left_dia_1 = [
    { sender: 'said', text: "-_-" },
    { sender: 'said', text: "Choosing left" },
    { sender: 'said', text: "JAIL TIME" },
    { sender: 'heard', text: "Boooo. I don't wanna go to jail... T_T" }
];

const right_dia_1_01 = [
    { sender: 'heard', text: "SAVE ME FROM JAIL TIME" },
    { sender: 'said', text: "Choosing right AGAIN" },
    { sender: 'heard', text: "Please bestie ;)" }
];

const right_dia_1_02 = [
    { sender: 'heard', text: "SAVE ME FROM JAIL TIME" },
    { sender: 'said', text: "Choosing right YET AGAIN" },
    { sender: 'heard', text: "Please bestie ;)" }
];

const left_dia_1_01 = [
    { sender: 'said', text: "-_-" },
    { sender: 'said', text: "Choosing left AGAIN" },
    { sender: 'said', text: "JAIL TIME" },
    { sender: 'heard', text: "Boooo. I don't wanna go to jail... T_T" }
];

const left_dia_1_02 = [
    { sender: 'said', text: "-_-" },
    { sender: 'said', text: "Choosing left YET AGAIN" },
    { sender: 'said', text: "JAIL TIME" },
    { sender: 'heard', text: "Boooo. I don't wanna go to jail... T_T" }
];

class Script{
    constructor(script_list, left_opt, right_opt, id_left, id_right) {
        this.script_list = script_list;
        this.left_opt = left_opt;
        this.right_opt = right_opt;
        this.id_left = id_left;
        this.id_right = id_right;
    }
}

const right_1_02 = new Script(right_dia_1_02, null,null, null, null);
const right_1_01 = new Script(right_dia_1_01, null, null, null, null);

const left_1_02 = new Script(left_dia_1_02, null, null, null, null);
const left_1_01 = new Script(left_dia_1_01, null, null, null, null);

const right_1 = new Script(right_dia_1, right_1_01, right_1_02, "#option_R1_1", "#option_R1_2");
const left_1 = new Script(left_dia_1, left_1_01, left_1_02, "#option_L1_1", "#option_L1_2");

const root = new Script(dialogue_start, left_1, right_1, '#option_L0_1', 'option_R0_1');

let current_node = root;

function node_tracker(node){
    console.log(node);
    // allows messages to be displayed after choposing button by resetting the message_index
    if (current_node != node){
        message_index = 0;
        button_hide(id1, id2);
        id1 = node.id_left;
        id2 = node.id_right;
    }
    current_node = node;
    if (node != null){
        display_script(node.script_list);
        return;
    }
    console.log("Reached the end");
}

let message_index = 0;

function display_script(dialogue){
    document.getElementById('start').innerHTML = "";
    if (message_index < dialogue.length){
        const message = dialogue[message_index];
        const message_element = document.createElement('div');
        const stylish = document.createElement('div');
        message_element.classList.add('message', message.sender);
        stylish.textContent = message.text;
        if (message.sender == 'heard'){
            stylish.classList.add('stylish_heard');
        }
        else if (message.sender == 'said'){
            stylish.classList.add('stylish_said');
        }
        message_element.appendChild(stylish);
        message_container.appendChild(message_element);

        scroll_talk_box_bottom();
        message_index++;
    }
    // displays the buttons when the script runs out
    // even if it slightly alters the goal of display_script
    if (message_index >= dialogue.length){
        if (id1 != null && id2 != null){
            button_reveal(id1, id2);
        }
    }
}

function button_reveal(id1, id2){
    const option_0 = document.querySelector(id1);
    const option_1 = document.querySelector(id2);

    option_0.style.display = 'block';
    option_1.style.display = 'block';
}

function button_hide(id1, id2){
    const option_0 = document.querySelector(id1);
    const option_1 = document.querySelector(id2);

    option_0.style.display = 'none';
    option_1.style.display = 'none';
}

function scroll_talk_box_bottom() {
    message_container.scrollTop = message_container.scrollHeight;
}