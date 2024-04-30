document.addEventListener("DOMContentLoaded", function () {
    // Login function
    function login() {
        window.location.href = "/login";
    }
    const loginButton = document.querySelector("button[onclick='login();']");
    loginButton.addEventListener("click", login);

    // Signin function
    function register() {
        window.location.href = "/register";
    }
    const registerButton = document.querySelector("button[onclick='register();']");
    registerButton.addEventListener("click", register);

    // Join function
    function join() {
        window.location.href = "/join";
    }
    const joinButton = document.getElementById("joinButton");
    joinButton.addEventListener("click", join);

    function home() {
        window.location.href = "/home";
    }
    const homeButton = document.querySelector("button[onclick='home();']");
    homeButton.addEventListener("click", home);

    function quizz() {
        window.location.href = "/quizz";
    }
    const qzButton = document.querySelector("button[onclick='quizz();']");
    qzButton.addEventListener("click", quizz);
});