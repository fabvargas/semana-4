const emailInput = document.getElementById("email");
const contrasenaInput = document.getElementById("pass");
const button = document.getElementById("submit");
const errorTxt = document.getElementById("errorTxt");
const successTxt = document.getElementById("successTxt");

function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function validarContrasena(contrasena) {
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/;
    return regex.test(contrasena);
}

function validarFormulario() {
    const email = emailInput.value.trim();
    const contrasena = contrasenaInput.value.trim();

    successTxt.textContent = "";
    errorTxt.textContent = "";

    if (!validarEmail(email)) {
        errorTxt.textContent = "El correo electrónico no es válido.";
        return false;
    }

    if (!validarContrasena(contrasena)) {
        errorTxt.textContent = "La contraseña debe tener al menos 6 caracteres, una letra mayúscula y un número, sin caracteres especiales.";
        return false;
    }

    return true;
}

button.addEventListener("click", (event) => {
    event.preventDefault();

    if (validarFormulario()) {
        fetch("/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                
            },
            body: JSON.stringify({
                email: emailInput.value.trim(),
                contrasena: contrasenaInput.value.trim()
            }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Error en la respuesta del servidor.");
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                successTxt.textContent = "Inicio de sesión exitoso.";
                errorTxt.textContent = "";
                
                setTimeout(() => {
                    window.location.href = "/";
                }, 1000);
            } else {
                successTxt.textContent = "";
                errorTxt.textContent = data.error || "Error al iniciar sesión.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            successTxt.textContent = "";
            errorTxt.textContent = "Error en la solicitud.";
        });
    }
});

