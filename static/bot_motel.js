document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('garbage-content')) {
        generateGarbageContent();
        setInterval(generateGarbageContent, 3000); // Update every 3 seconds
    }

    if (document.getElementById('random-content')) {
        generateRandomContent();
        setInterval(generateRandomContent, 3500); // Update every 3.5 seconds
    }

    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const query = searchForm.querySelector('input[name="query"]').value;  // Fix the input name
            fetchSearchResults(query);
        });
    }
});

function fetchSearchResults(query) {
    fetch(`/search?query=${encodeURIComponent(query)}`)  // Fix the query parameter
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            const searchResults = document.getElementById('search-results');
            if (searchResults) {
                searchResults.innerHTML = html;
            } else {
                console.error('Element #search-results not found');
            }
        })
        .catch(error => console.error('Error fetching search results:', error));
}

function generateGarbageContent() {
    const garbageContentElement = document.getElementById('garbage-content');
    garbageContentElement.innerHTML = ''; // Clear previous content
    let garbageContent = '';

    for (let i = 0; i < 1000; i++) {
        garbageContent += getRandomChar();
    }

    for (let i = 0; i < 20; i++) {
        const link = document.createElement('a');
        const randomText = generateRandomString(20);
        link.href = `/${randomText}`;
        link.textContent = randomText;
        link.className = 'invisible';
        link.style.display = 'block';
        garbageContentElement.appendChild(link);
    }

    for (let i = 0; i < 10; i++) {
        garbageContent += `<p>User${generateRandomString(5)}: ${generateRandomString(50)}</p>`;
    }

    for (let i = 0; i < 5; i++) {
        garbageContent += `<p>Encrypted Data: ${generateRandomString(50)}</p>`;
    }

    garbageContent += '<table>' + Array.from({length: 10}, () => `<tr><td>${generateRandomString(10)}</td><td>${generateRandomString(10)}</td></tr>`).join('') + '</table>';

    garbageContentElement.innerHTML += garbageContent;
}

function generateRandomContent() {
    const randomContentElement = document.getElementById('random-content');
    randomContentElement.innerHTML = ''; // Clear previous content
    let randomContent = '';

    for (let i = 0; i < 500; i++) {
        randomContent += getRandomChar();
    }

    for (let i = 0; i < 10; i++) {
        const link = document.createElement('a');
        const randomText = generateRandomString(15);
        link.href = `/${randomText}`;
        link.textContent = randomText;
        link.style.display = 'block';
        randomContentElement.appendChild(link);
    }

    for (let i = 0; i < 5; i++) {
        randomContent += `<p>User${generateRandomString(4)}: ${generateRandomString(40)}</p>`;
    }

    randomContentElement.innerHTML += randomContent;
}

function getRandomChar() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    return chars.charAt(Math.floor(Math.random() * chars.length));
}

function generateRandomString(length) {
    let result = '';
    for (let i = 0; i < length; i++) {
        result += getRandomChar();
    }
    return result;
}
