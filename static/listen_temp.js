const dialogue_sample = [
    "<span class ='red-text'> Suspect:</span> Listen, you gotta believe me officer. I did nothing wrong! I am being framed! I would never kill a person ;)",
    "<span class='blue-text'>Officer:</span> *Sigh* You winked at me...I know you're lying.", 
    "<span class ='red-text'> Suspect:</span> Whatttttt...Lying? Pshhhh, we both know I am innocent ;)",
    "<span class='blue-text'>Officer:</span> No. I know you are guilty.",
    "<span class ='red-text'> Suspect:</span>: Guilty? Me? What evidence is there that proves I am a murderer?",
    "<span class='blue-text'>Officer:</span> Security camera footage at the scene where the murder took place.",
    "<span class ='red-text'> Suspect:</span> Ha! Well, that footage must be a deepfake because I never left Manhattan much less went all the way up to Buffalo",
    "<span class='blue-text'>Officer:</span> Alright we are done here. Take 'em away.",
    "<span class ='red-text'> Suspect:</span> What? Why? You didn't even provide evidence.",
    "<span class='blue-text'>Officer:</span> I didn't tell you where the murder happened. -_-",
    "<span class ='red-text'> Suspect:</span> ;)"
]
let index = 0;
function changeText(dialogue) {
    const textBox = document.querySelector('.text-box');
    textBox.innerHTML = dialogue[index];
    if (index + 1 < dialogue.length){
        index++;
    }
        
}  