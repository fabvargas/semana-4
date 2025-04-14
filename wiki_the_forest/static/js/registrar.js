const emailInput = document.getElementById("email");
const contrasenaInput = document.getElementById("pass" );
const confirmPassInput = document.getElementById("pass-con" );
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

function validarContrasenaIguales(contrasena, confirmContrasena) {
    return contrasena === confirmContrasena;
}

function validarFormulario() {
    const email = emailInput.value;
    const contrasena = contrasenaInput.value;
    const confirmContrasena = confirmPassInput.value;

    successTxt.textContent = "";

    if (!validarEmail(email)) {
        errorTxt.textContent = "El correo electrónico no es válido.";
        return false;
    }

    if (!validarContrasena(contrasena)) {
        errorTxt.textContent = "La contraseña debe tener al menos 6 caracteres, una letra mayúscula y un número. sin caracteres especiales";
        return false;
    }

    if (!validarContrasenaIguales(contrasena, confirmContrasena)) {
        errorTxt.textContent = "Las contraseñas no coinciden.";
        return false;
    }

    errorTxt.textContent = "";
    return true;
}


button.addEventListener("click", (event) => {
    event.preventDefault(); 
    if (validarFormulario()) {      
       fetch("/registrar_usuario/",{
        
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: emailInput.value,
                contrasena: contrasenaInput.value,
                confirmContrasena: confirmPassInput.value
            })
        })
        .then(response => {
            if (response.ok) {
                errorTxt.textContent = "";
                successTxt.textContent = "Usuario registrado con éxito.";
            } else {
                errorTxt.textContent = "Error al registrar el usuario. Inténtalo de nuevo.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            successTxt.textContent = "";
            errorTxt.textContent = "Error al registrar el usuario. Inténtalo de nuevo.";
       })
       
    }
}
);


