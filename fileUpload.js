const form = document.getElementById('uploadForm');
form.addEventListener('submit', uploadFile);

async function uploadFile(event) {
    // Prevent the page from refreshing
    event.preventDefault();

    let formData = new FormData();
    const file = document.getElementById('srcFile').files[0];
    const numWorkers = document.getElementById('numWorkers').value;

    formData.append('file', file);
    formData.append('numWorkers', numWorkers);

    // Submit POST request to the server's API endpoint
    await fetch('/upload', {
        method: 'POST',
        body: formData
    }).then(function(response) {
        /* Get plain text from the response (the
        response should be the output of the script) */
        return response.text();
    }).then(function(outputText) {
        // Append the text to the bottom of the page
        let outputElem = document.createElement('div');
        outputElem.innerHTML = outputText;
        document.body.appendChild(outputElem);
    });

    return false;
}