document.addEventListener("DOMContentLoaded", function () {
    // Function to start the quiz
    function startQuiz() {
        document.getElementById("displayText").style.display = "block";
        document.getElementById("stopButton").style.display = "block";
        startButton.style.display = "none";
    }

    // Function to end the quiz
    function endQuiz() {
        displayText.style.display = "none";
        stopButton.style.display = "none";
        startButton.style.display = "block";
    }

    // Function to logout
    function logout() {
        window.location.href = "/logout";
    }

    // Adding event listeners
    const startButton = document.getElementById("startButton");
    const stopButton = document.getElementById("stopButton");
    const logoutButton = document.getElementById("btnLogin-popup");

    startButton.addEventListener("click", startQuiz);
    stopButton.addEventListener("click", endQuiz);
    logoutButton.addEventListener("click", logout);
});