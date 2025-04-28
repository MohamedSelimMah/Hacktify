// Adding dynamic effect for showing the flag after the user successfully submits the correct flag
const flag = document.getElementById("flag");
if (flag) {
    flag.style.opacity = 0;
    flag.style.transition = "opacity 2s ease-in-out";
    flag.addEventListener("mouseover", function() {
        flag.style.opacity = 1;
    });
}

// Button animations
const buttons = document.querySelectorAll("button");
buttons.forEach(button => {
    button.addEventListener("mouseover", function() {
        button.style.transform = "scale(1.1)";
    });
    button.addEventListener("mouseout", function() {
        button.style.transform = "scale(1)";
    });
});
