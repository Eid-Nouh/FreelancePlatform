// Password strength checker
const passwordInput = document.getElementById('password1');
const strengthBar = document.querySelector('.strength-bar');
const strengthText = document.getElementById('strengthText');

if (passwordInput) {
    passwordInput.addEventListener('input', function() {
        const password = this.value;
        let strength = 0;
        
        if (password.length >= 6) strength++;
        if (password.length >= 10) strength++;
        if (password.match(/[a-z]/) && password.match(/[A-Z]/)) strength++;
        if (password.match(/[0-9]/)) strength++;
        if (password.match(/[^a-zA-Z0-9]/)) strength++;
        
        const percentage = (strength / 5) * 100;
        strengthBar.style.width = percentage + '%';
        
        if (percentage < 40) {
            strengthBar.style.background = '#dc3545';
            strengthText.textContent = 'Password strength: Weak';
        } else if (percentage < 70) {
            strengthBar.style.background = '#ffc107';
            strengthText.textContent = 'Password strength: Medium';
        } else {
            strengthBar.style.background = '#28a745';
            strengthText.textContent = 'Password strength: Strong';
        }
    });
}

// Toggle password visibility
document.querySelectorAll('.toggle-password').forEach(icon => {
    icon.addEventListener('click', function() {
        const target = document.getElementById(this.dataset.target);
        if (target.type === 'password') {
            target.type = 'text';
            this.classList.remove('fa-eye');
            this.classList.add('fa-eye-slash');
        } else {
            target.type = 'password';
            this.classList.remove('fa-eye-slash');
            this.classList.add('fa-eye');
        }
    });
});

// Form validation
const form = document.querySelector('.auth-form');
if (form) {
    form.addEventListener('submit', function(e) {
        const password1 = document.getElementById('password1').value;
        const password2 = document.getElementById('password2').value;
        const terms = document.getElementById('terms');
        
        if (password1 !== password2) {
            e.preventDefault();
            alert('Passwords do not match');
            return false;
        }
        
        if (password1.length < 6) {
            e.preventDefault();
            alert('Password must be at least 6 characters');
            return false;
        }
        
        if (!terms.checked) {
            e.preventDefault();
            alert('Please agree to the Terms & Conditions');
            return false;
        }
        
        return true;
    });
}