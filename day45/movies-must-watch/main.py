from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
print(soup.title)

movies_list = [movie.string for movie in soup.select(selector="h3.title")]
movies_list.reverse()
print(movies_list)

with open("movies.txt", mode="a") as file:
    for movie in movies_list:
        file.write(movie + "\n")