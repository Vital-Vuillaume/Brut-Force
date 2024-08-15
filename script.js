//------Https------\\

/*if (window.location.protocol != "https:") {
  window.location.protocol="https:";
}*/

const input = document.querySelector(".input");
const btn = document.querySelector(".btn");

let password = "bonjour"

function correctPassword() {
  if(input.value === password) {
    alert("The right password!");
  }
}

btn.addEventListener("click", function(){
  correctPassword()
})

input.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    correctPassword()
  }
})