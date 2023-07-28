const dialogue_sample = [
  "<span class='blue-text'>Officer:</span> Good morning, Mr. Smith. My name is Detective Johnson. I'd like to talk to you about the recent armed robberies that have occurred in connection to this McDonald's. We have reason to believe that you might have information that could assist us in our investigation.",
  "<span class ='red-text'>Suspect:</span> (Nervously) I don't know anything about those robberies. I wasn't involved!",
  "<span class='blue-text'>Officer:</span> I understand your concern, and I'm here to get to the truth. We have surveillance footage showing someone who fits your description at the scene of one of the robberies. Can you explain why you were in the vicinity at that time?",
  "<span class ='red-text'>Suspect:</span> I-I was just passing by. I wasn't involved in anything illegal!",
  "<span class='blue-text'>Officer:</span> It's important to be honest here, Mr. Smith. We have eyewitness accounts of a suspect wearing clothes similar to what you were wearing that night and found you walking out of the forest close vicinity of the crime.",
  "<span class ='red-text'>Suspect:</span> (Pauses) I was just going to church to repent but not for the crimes! (He realizes he just slipped up and GASPS (Sadly))",
  "<span class='blue-text'>Officer:</span> What do you mean not for the crimes? We caught you with all the tools. We can help you with a plea.",
  "<span class ='red-text'>Suspect:</span> (doesn’t speak)",
  "<span class='blue-text'>Officer:</span> This is your chance to become clean before we throw the book at you in court.",
  "<span class ='red-text'>Suspect:</span> Okay, Okay, listen. I was going through tough times and wanted to have more money.",
  "<span class='blue-text'>Officer:</span> You are looking up to 25 years. We can help you, but if you don’t cooperate, we will book you.",
  "<span class ='red-text'>Suspect:</span> Okay, It was me. I have been robbing McDonald's each time at the base. No one has been hurt… I just needed the money… Stop it, that’s all.",
];
let index = 0;
function changeText(dialogue) {
  const textBox = document.querySelector(".text-box");
  textBox.innerHTML = dialogue[index];
  if (index + 1 < dialogue.length) {
    index++;
  } else {
    reveal_continue();
  }
}

function reveal_continue() {
  const button_continue = document.querySelector("#continue");
  button_continue.style.display = "block";
}
