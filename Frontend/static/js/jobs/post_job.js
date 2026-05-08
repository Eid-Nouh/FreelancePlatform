document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('jobForm');
    const messageDiv = document.getElementById('formMessage');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        // Get values
        const title = document.getElementById('title').value.trim();
        const company = document.getElementById('company').value.trim();
        const budget = document.getElementById('budget').value;
        const description = document.getElementById('description').value.trim();

        // Simple validation
        if (title === '') {
            showMessage('❌ Please enter a job title', 'error');
            return;
        }
        if (company === '') {
            showMessage('❌ Please enter a company / client name', 'error');
            return;
        }
        if (description === '') {
            showMessage('❌ Please write a job description', 'error');
            return;
        }

        // If everything is ok
        const jobData = {
            title: title,
            company: company,
            budget: budget ? budget : 'Not specified',
            description: description,
            postedAt: new Date().toLocaleString()
        };
        console.log('Job posted:', jobData);

        showMessage(`✅ Job "${title}" posted successfully!`, 'success');

        // Optional: clear the form after success
        // form.reset();

        // Hide message after 4 seconds
        setTimeout(() => {
            messageDiv.className = 'message';
            messageDiv.style.display = 'none';
        }, 4000);
    });

    function showMessage(msg, type) {
        messageDiv.textContent = msg;
        messageDiv.className = `message ${type}`;
        messageDiv.style.display = 'block';
    }
});