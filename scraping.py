import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })

df = pd.DataFrame(data)

df.to_csv("hasil_scraping.csv", index=False, encoding="utf-8-sig")
df.to_excel("hasil_scraping.xlsx", index=False)

print("Scraping berhasil!")
print(df)