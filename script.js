document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('newsForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent form from submitting and refreshing the page

        const newsText = document.getElementById('newsText').value;

        // Sending the news text to the backend for fake news detection
        fetch('/detect', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `news_text=${encodeURIComponent(newsText)}`
        })
        .then(response => response.json())  // Parse the response as JSON
        .then(data => {
            // Log the response data to the browser console for debugging
            console.log(data);  // This will show the response in the console

            // Check if the result is fake news
            if (data.is_fake) {
                resultDiv.textContent = "This news article is likely FAKE!";
                resultDiv.classList.add('true');  // Apply 'true' class for styling
                resultDiv.classList.remove('false');  // Remove 'false' class
            } else {
                resultDiv.textContent = "This news article seems TRUE.";
                resultDiv.classList.add('false');  // Apply 'false' class for styling
                resultDiv.classList.remove('true');  // Remove 'true' class
            }

            // Make the result visible on the page
            resultDiv.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);  // Log any errors to the console
            resultDiv.textContent = 'An error occurred. Please try again.';
            resultDiv.style.display = 'block';
        });
    });
});
