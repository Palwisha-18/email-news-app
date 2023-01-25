import requests


api_key = "82908d425f184086abb2e75e01db7b36"
url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-25&" \
      "sortBy=publishedAt&apiKey=82908d425f184086abb2e75e01db7b36"

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])

