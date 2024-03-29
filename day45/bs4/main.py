from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(selector=".titleline > a")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.string
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.string.split()[0]) for score in soup.select(selector=".score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(largest_number)
print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])


# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)