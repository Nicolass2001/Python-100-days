from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
from tqdm import tqdm
import requests


year = input("Which year do you want to travel to? Type the date in this format YYYY: ")

response = requests.get(url=f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/")
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

songs_list = [song.string.strip() for song in soup.select(selector="li.o-chart-results-list__item > h3#title-of-a-story")]
artist_list = [artist.string.strip() for artist in soup.select(selector="li.o-chart-results-list__item > span.a-font-primary-s")]

ytmusic = YTMusic("oauth.json")

video_ids = []

for i in tqdm(range(0, 100)):
    song = songs_list[i]
    artist = artist_list[i]
    response_song = ytmusic.search(query=f"{song} {artist}", filter="songs")
    video_ids.append(response_song[0]["videoId"])

ytmusic.create_playlist(title=f"{year} Billboard 100", description="Playlist generated with python", privacy_status="PUBLIC", video_ids=video_ids)