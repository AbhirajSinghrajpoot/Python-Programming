import requests
from bs4 import BeautifulSoup
import pathlib

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movie_titles.reverse()


with open(pathlib.Path("Day_45/100 Movies Scraping Project/movies.txt"), mode="w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")