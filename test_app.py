import requests

def test_home(base_url):
    response = requests.get(base_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        results = response.json()
        for result in results:
            print(result['text'])
    else:
        print(f"Error: {response.status_code} - {response.text}")

def test_sentiment(base_url,data):
    # Send a POST request to the endpoint
    response = requests.post(base_url, json=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the sentiment analysis results
        results = response.json()
        for result in results:
            print(f"Text: {result['text']}, Sentiment: {result['sentiment']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")


# Define the base URL of the Flask home
base_url = 'http://localhost:8080'

# Define the list of texts to analyze sentiment
texts = ["It is worth it", "It is a waste of time and money"]

# Create a dictionary containing the texts
data = {'texts': texts}

test_home(base_url=base_url)
test_sentiment(base_url=base_url,data=data)
