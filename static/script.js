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

// ------------------------------------------

async function cercaRicette() {
    const ingredientiSelezionati = [];
    document.querySelectorAll("input[name='ingrediente']:checked").forEach(cb => {
        ingredientiSelezionati.push(cb.value);
    });

    try {
        const collegamento = await fetch("/api/ricerca", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                ingredienti: ingredientiSelezionati
            })
        });

        if (collegamento.ok === false) {
            alert("Errore durante la ricerca delle ricette!");
            return;
        }

        const ricette = await collegamento.json();

        sessionStorage.setItem("ricetteTrovate", JSON.stringify(ricette));

        window.location.href = "/risultati";

    } catch (error) {
        console.error("Errore:", error);
        alert("Errore di connessione al server.");
    }
}

//---------------------------------------

function mostraRisultati() {
    const dati = sessionStorage.getItem("ricetteTrovate");
    if (!dati) return;

    const ricette = JSON.parse(dati);
    const container = document.getElementById("lista-ricette");

    ricette.forEach(r => {
        const selezione_ricetta = document.createElement("div");
        selezione_ricetta.classList.add("ricetta-box");

        selezione_ricetta.innerHTML = ` <img src="${r.foto}" alt="${r.nome}" class="img-risultati">
            <h3>${r.nome}</h3>
            <button onclick="apriRicetta('${r._id}')">Apri ricetta</button>`

        container.appendChild(selezione_ricetta);
    });
}

//-------------------------

function apriRicetta(id) {
    window.location.href = `/ricetta/${id}`;
}

//-------------------------

async function aggiungiPreferito(id) {
    const collegamento = await fetch("/api/aggiungipreferiti", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            id: id
        })
    });

    const risultato = await collegamento.json();
    alert(risultato.message);
}

// -----------------------------------

async function caricaPreferiti() {
    try {
        const collegamento = await fetch("/api/caricapreferiti", {
            method: "GET"
        });

        if (collegamento.ok === false) {
            alert("Errore nel caricamento dei preferiti! Riprova.");
            return;
        }

        const ricette = await collegamento.json();
        const container = document.getElementById("lista-ricette");

        ricette.forEach(r => {
            const selezione_ricetta = document.createElement("div");
            selezione_ricetta.classList.add("ricetta-box");

            selezione_ricetta.innerHTML = `<img src="${r.foto}" alt="${r.nome}" class="img-risultati">
                <h3>${r.nome}</h3>
                <button onclick="apriRicetta('${r._id}')">Apri ricetta</button>`;

            container.appendChild(selezione_ricetta);
        });

    } catch (errore) {
        console.error("Errore:", errore);
        alert("Errore di connessione al server");
    }
}

//---------------------------

async function inviaRecensione(id) {

    const testo = document.getElementById("testo-recensione").value;
    const voto = document.getElementById("voto").value;

    try {
        const risposta = await fetch("/api/recensione", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                ricetta_id: id,
                testo: testo,
                voto: voto
            })
        });

        const risultato = await risposta.json();
        alert(risultato.message);

        if (risultato.ok === true) {
            location.reload();
        }

    } catch (errore) {
        console.error("Errore:", errore);
        alert("Errore di connessione al server");
    }
}
