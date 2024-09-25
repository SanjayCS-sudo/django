import requests

# Define the base URL and append query parameters directly
url = "https://api.cloudflare.com/client/v4/radar/attacks/layer7/summary/http_method"
url_with_params = f"{url}?start=2024-09-20T10:22:57Z&end=2024-09-22T10:22:57Z&format=json"

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": "sanjaykmrcs@gmail.com",  
    "X-Auth-Key": "3ece1ffa9c008ba16d254282447802a81329d"  # Replace with your actual API key
}

# Making the GET request with the URL containing query parameters
response = requests.get(url_with_params, headers=headers)

# Enhanced error handling
if response.status_code == 200:
    print("Response JSON:", response.json())
elif response.status_code == 400:
    print("Bad Request - Likely a parameter issue:", response.text)
elif response.status_code == 401:
    print("Unauthorized - Check your API key and email:", response.text)
elif response.status_code == 403:
    print("Forbidden - You may not have access to this endpoint:", response.text)
else:
    print(f"Error {response.status_code}: {response.text}")
