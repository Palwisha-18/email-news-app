import requests

from send_email import send_email

api_key = "82908d425f184086abb2e75e01db7b36"
url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-25&" \
      "sortBy=publishedAt&apiKey=82908d425f184086abb2e75e01db7b36"

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
