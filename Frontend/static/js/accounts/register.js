// register.js - Basic form validation for the register page

const form = document.getElementById('registerForm');

if (form) {
    form.addEventListener('submit', function (e) {
        const password1 = document.getElementById('password1').value;
        const password2 = document.getElementById('password2').value;
        const terms = document.getElementById('terms');

        // Check passwords match
        if (password1 !== password2) {
            e.preventDefault();
            alert('Passwords do not match.');
            return;
        }

        // Check password length
        if (password1.length < 6) {
            e.preventDefault();
            alert('Password must be at least 6 characters.');
            return;
        }

        // Check terms checkbox
        if (!terms.checked) {
            e.preventDefault();
            alert('Please agree to the Terms of Service.');
        }
    });
}