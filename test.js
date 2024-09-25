const axios = require('axios');

// Define the base URL
const url = 'https://api.cloudflare.com/client/v4/radar/attacks/layer7/top/locations/origin';

// Define query parameters
const params = {
    dateStart: '2024-09-20T10:22:57Z',
    dateEnd: '2024-09-22T10:22:57Z',
    format: 'json'
};

// Headers containing authentication
const headers = {
    'Content-Type': 'application/json',
    'X-Auth-Email': 'sanjaykmrcs@gmail.com',
    'X-Auth-Key': '3ece1ffa9c008ba16d254282447802a81329d'  // Replace with your actual API key
};

// Polling function to request data every 10 seconds (adjust interval as needed)
function pollAPI() {
    axios.get(url, {
        headers: headers,
        params: params
    })
    .then(response => {
        console.log('Response JSON:', response.data);
    })
    .catch(error => {
        if (error.response) {
            console.log('Error:', error.response.status, error.response.data);
        } else {
            console.log('Error:', error.message);
        }
    });
}

``
