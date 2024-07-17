document.addEventListener('DOMContentLoaded', () => {
    const productList = document.getElementById('productos');
    const cartList = document.getElementById('lista-carrito');
    const cartCount = document.getElementById('cart-count');
    const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

    let cart = [];
    const products = [];

    products.forEach(product => {
        const productoDiv = document.createElement('div');
        productoDiv.className = 'producto';
        productoDiv.innerHTML = `
            <img src="${product.img}" alt="${product.name}">
            <h2>${product.name}</h2>
            <button onclick="agregarAlCarrito('${product.name}')">Agregar al Carrito</button>
        `;
        productList.appendChild(productoDiv);
    });

    // Evento para agregar al carrito
    productList.addEventListener('click', event => {
        if (event.target.tagName === 'BUTTON') {
            const name = event.target.parentElement.querySelector('h2').textContent;

            // Verificar si ya esta la mascota en el carrito 
            const existingProduct = cart.find(item => item.name === name);
            if (!existingProduct) {
                cart.push({ name });
                updateCart();
            }
        }
    });

    // Vaciar carrito
    vaciarCarritoBtn.addEventListener('click', () => {
        cart = []; // Vaciar el carrito
        updateCart(); // Actualizar la vista del carrito
    });

    // Actualizar carrito
    function updateCart() {
        cartList.innerHTML = ''; // Limpiar lista del carrito
        cart.forEach((item, index) => {
            const listItem = document.createElement('li');
            listItem.className = 'list-group-item';
            listItem.textContent = `${item.name}`;
            cartList.appendChild(listItem);
        });

        cartCount.textContent = cart.length;
    }
});


//Funciones de validar login
function validateLogin(event){
    event.preventDefault();

    var username = document.getElementsById('username').value;
    var password = document.getElementById('password').value;

    var validUsername = 'user';
    var validPassword = 'password';

    if (username === validUsername && password === validPassword) {
        alert("Inicio Exitoso");
    }
    else {
        var errorMessage = document.getElementById('error-message');
        errorMessage.textContent = "Contraseña incorrecta, Porfavor intentar nuevamente";
    }
}
//validar signup
function validateForm() {
    var username = document.getElementById("username").value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var usernameError = document.getElementById('usernameError');
    var emailError = document.getElementById('emailError');
    var passwordError = document.getElementById('passwordError');
    var isValid = true;



    usernameError.textContent = '';
    emailError.textContent = '';
    passwordError.textContent = '';

    if (username === '') {
        usernameError.textContent = "Por favor ingresa un Usuario.";
        isValid = false;
    }
    if (email === "") {
        emailError.textContent = "Por favor ingresa un Correo Electronico.";
        isValid = false;
    } else if (!isValidEmail(email)){
        emailError.textContent = "Por favor ingresa un Correo Electronico.";
        isValid = false;
    }
    
    if (password ===''){
        passwordError.textContent = "Por Favor ingresa una contraseña";
        isValid = false;
    }

}
function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}


// Slider automático
let slideIndex = 0;
carousel();

function carousel() {
    const slides = document.querySelectorAll('.slide');
    if (slides.length === 0) return;

    slides.forEach(slide => {
        slide.style.display = 'none';
    });

    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }

    slides[slideIndex - 1].style.display = 'block';

    setTimeout(carousel, 3000);  //3 segundos
}
//controlar el modal
var btnAbrirModal = document.getElementById('btn-abrir-modal');
var btnCerrarModal = document.getElementById('btn-cerrar-modal');
var modal = document.getElementById('modal');

    btnAbrirModal.addEventListener('click', function() {
        modal.classList.add('active');
    });

    btnCerrarModal.addEventListener('click', function() {
        modal.classList.remove('active'); 
    });