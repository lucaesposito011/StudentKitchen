//REGISTRAZIONE
const registerForm = document.getElementById("registerform");
if (registerForm) {
    registerForm.addEventListener("submit", async function(event) {
        event.preventDefault();

        const nome = document.getElementById("reg_username").value;
        const cognome = document.getElementById("reg_usersurname").value;
        const email = document.getElementById("reg_useremail").value;
        const password = document.getElementById("reg_userpassword").value;

        const collegamento = await fetch("/api/registrazione", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                nome: nome,
                cognome: cognome,
                email: email,
                password: password
            })
        });

        const risultato = await collegamento.json();
        alert(risultato.message);

        if (risultato.ok === true) {
            window.location.href = "/login";
        }
    });
}

//--------------------

//LOGIN
const loginForm = document.getElementById("loginform");
if (loginForm) {
    loginForm.addEventListener("submit", async function(event) {
        event.preventDefault();

        const email = document.getElementById("log_useremail").value;
        const password = document.getElementById("log_userpassword").value;

        const collegamento = await fetch("/api/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const risultato = await collegamento.json();
        alert(risultato.message);

        if (risultato.ok === true) {
            window.location.href = "/home";
        }
    });
}
