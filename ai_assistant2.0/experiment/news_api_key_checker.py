import requests

newsapi = "b3453c25bd244728bf3c54bc3682d13f"
# base_url = "https://newsapi.org/v2/top-headlines"
base_url = "http://api.mediastack.com/v1/"

params = {
    "apiKey": newsapi,
    "country": "in",
    "language": "en",
    "pageSize": 5
}

response = requests.get(base_url, params=params)
if response.status_code == 200:
    print("API key is valid. Here are the headlines:")
    news_data = response.json()
    for article in news_data.get("articles", []):
        print(article.get("title", "No title available"))
else:
    print(f"Error: {response.status_code} - {response.json()}")