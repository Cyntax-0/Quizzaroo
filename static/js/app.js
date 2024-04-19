document.addEventListener("DOMContentLoaded", function () {
    // Login function
    function login() {
        window.location.href = "/login";
    }
    const loginButton = document.querySelector("button[onclick='login();']");
    loginButton.addEventListener("click", login);

    // Signin function
    function signin() {
        window.location.href = "/signup";
    }
    const signButton = document.querySelector("button[onclick='signin();']");
    signButton.addEventListener("click", signin);

    // Join function
    function join() {
        window.location.href = "/join";
    }
    const joinButton = document.querySelector("button[onclick='join();']");
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