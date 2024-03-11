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
});