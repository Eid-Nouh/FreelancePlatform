// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    
    // Toggle password visibility
    const togglePassword = document.querySelector('.toggle-password');
    const passwordInput = document.getElementById('password');
    
    if (togglePassword && passwordInput) {
        togglePassword.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            
            // Toggle eye icon
            this.classList.toggle('fa-eye');
            this.classList.toggle('fa-eye-slash');
        });
    }
    
    // Form validation
    const form = document.querySelector('.auth-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const username = document.querySelector('input[name="username"]').value.trim();
            const password = passwordInput.value.trim();
            
            // Validate username
            if (username === '') {
                e.preventDefault();
                showError('Please enter your username');
                return false;
            }
            
            // Validate password
            if (password === '') {
                e.preventDefault();
                showError('Please enter your password');
                return false;
            }
            
            if (password.length < 6) {
                e.preventDefault();
                showError('Password must be at least 6 characters');
                return false;
            }
            
            return true;
        });
    }
    
    // Show error message function
    function showError(message) {
        // Remove existing error
        const existingError = document.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }
        
        // Create error element
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.cssText = `
            background: #fee2e2;
            color: #dc2626;
            padding: 0.75rem;
            border-radius: 12px;
            font-size: 0.85rem;
            margin-bottom: 1rem;
            text-align: center;
            border-right: 3px solid #dc2626;
            animation: fadeInUp 0.3s ease;
        `;
        errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
        
        // Insert at top of form
        const formCard = document.querySelector('.auth-card');
        const formElement = document.querySelector('.auth-form');
        formCard.insertBefore(errorDiv, formElement);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            if (errorDiv) {
                errorDiv.style.opacity = '0';
                setTimeout(() => {
                    if (errorDiv) errorDiv.remove();
                }, 300);
            }
        }, 3000);
    }
    
    // Add input cleanup on focus
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            const error = document.querySelector('.error-message');
            if (error) {
                error.remove();
            }
        });
    });
    
    // Remember me functionality (local storage)
    const rememberCheckbox = document.querySelector('#remember-me');
    const usernameInput = document.querySelector('input[name="username"]');
    
    if (rememberCheckbox && usernameInput) {
        // Load saved username
        const savedUsername = localStorage.getItem('savedUsername');
        if (savedUsername) {
            usernameInput.value = savedUsername;
            rememberCheckbox.checked = true;
        }
        
        // Save username when form submits
        form.addEventListener('submit', function() {
            if (rememberCheckbox.checked) {
                localStorage.setItem('savedUsername', usernameInput.value);
            } else {
                localStorage.removeItem('savedUsername');
            }
        });
    }
});