document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('applyForm');
    const messageDiv = document.getElementById('formMessage');

    if (form) {
        form.addEventListener('submit', function (event) {
            const fullName = form.querySelector('input[name="full_name"]').value.trim();
            const email = form.querySelector('input[name="email"]').value.trim();
            const proposal = form.querySelector('textarea[name="message"]').value.trim();

            if (fullName === '') {
                event.preventDefault();
                showMessage('❌ Please enter your full name.', 'error');
                return;
            }
            if (email === '') {
                event.preventDefault();
                showMessage('❌ Please enter your email address.', 'error');
                return;
            }
            if (proposal === '') {
                event.preventDefault();
                showMessage('❌ Please write your proposal.', 'error');
                return;
            }
            // If all valid, show success message (form will submit normally)
            showMessage('✅ Application submitted! Redirecting...', 'success');
            setTimeout(() => {}, 100);
        });
    }

    function showMessage(msg, type) {
        messageDiv.textContent = msg;
        messageDiv.className = `message ${type}`;
        messageDiv.style.display = 'block';

        setTimeout(() => {
            messageDiv.style.display = 'none';
        }, 5000);
    }
});