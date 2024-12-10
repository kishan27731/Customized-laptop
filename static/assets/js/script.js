document.getElementById('pdf-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var startDate = document.getElementById('start-date').value;
    var endDate = document.getElementById('end-date').value;

    fetch('/get-pdf', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Add this line
        },
        body: JSON.stringify({
            start_date: startDate,
            end_date: endDate,
        }),
    })
    .then(response => response.blob())
    .then(blob => {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'Custom data.pdf';
        a.click();
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('message').textContent = 'An error occurred while generating the PDF.';
    });
});

// Function to get cookie value
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}