// login.js - Basic form validation for the login page

document.addEventListener('DOMContentLoaded', function () {

    // Toggle password visibility (show/hide password)
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.querySelector('.toggle-password');

    if (toggleIcon && passwordInput) {
        toggleIcon.addEventListener('click', function () {
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                this.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                passwordInput.type = 'password';
                this.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });
    }

    // Basic client-side validation before submitting
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (e) {
            const username = form.querySelector('input[name="username"]').value.trim();
            const password = passwordInput ? passwordInput.value.trim() : '';

            if (username === '') {
                e.preventDefault();
                alert('Please enter your username.');
                return;
            }

            if (password === '') {
                e.preventDefault();
                alert('Please enter your password.');
            }
        });
    }

});