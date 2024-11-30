import requests
import json

query = "Search news by keyword you are interested in: "
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-10-30&sortBy=publishedAt&apiKey=API_KEY"
r = requests.get(url)

news = json.loads(r.text)
print(news , type(news))

for article in news["articles"]:
  print(article["title"])
  print(article["description"])