import requests

from send_email import send_email

topic = "tesla"
api_key = "82908d425f184086abb2e75e01db7b36"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2022-12-25&" \
      "sortBy=publishedAt&apiKey=82908d425f184086abb2e75e01db7b36&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's News" + "\n" + body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
