import requests

# Set your OpenAI API key
api_key = "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"

# Define the API endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Define the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the request payload as a Python dictionary
payload = {
    "model": "dall-e-3",
    "prompt": "a black man painting the mona lisa",
    "n": 1,
    "size": "1024x1024"
}

# Make the POST request to the API using the requests library
response = requests.post(url, json=payload, headers=headers)

# Check the response status code (200 indicates success)
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    # Get the URL of the generated image from the response
    image_url = data['data'][0]['url']
    # Print the image URL
    print("Generated image URL:", image_url)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)