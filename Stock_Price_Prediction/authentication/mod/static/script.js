document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("loginForm");
    const signupForm = document.getElementById("signupForm");
    const showSignup = document.getElementById("showSignup");
    const showLogin = document.getElementById("showLogin");

    // Show Signup Form
    showSignup.addEventListener("click", function(event) {
        event.preventDefault();
        loginForm.classList.add("hidden");
        signupForm.classList.remove("hidden");
        loginBtn.classList.remove("active");
        signupBtn.classList.add("active");
    });

    // Show Login Form
    showLogin.addEventListener("click", function(event) {
        event.preventDefault();
        signupForm.classList.add("hidden");
        loginForm.classList.remove("hidden");
        signupBtn.classList.remove("active");
        loginBtn.classList.add("active");
    });

});