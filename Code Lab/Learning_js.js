
//Functions - reusable code blocks
//Arrow function: const name = (params) => what it returns
const add = (a, b) => a + b;
document.addEventListener("DOMContentLoaded", () => {
    
    //document.cookie shows all cookies on this page
    let cookie = document.cookie;
    //If cookie is empty (like on file://), show a message
    if (cookie === "") {
        cookie = "none (open via Flask server for cookies to work!)";
    }
    document.querySelector("h1").textContent = `Here's a cookie: ${document.cookie}`;
    document.querySelector("h1").style.color = "red";
});
