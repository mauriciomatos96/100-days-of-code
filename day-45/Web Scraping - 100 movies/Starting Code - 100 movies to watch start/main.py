import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

with open(file="movies.txt", mode="w") as file:
    response = requests.get(URL)
    response.raise_for_status()
    empire_online_webpage = response.text

    soup = BeautifulSoup(empire_online_webpage, "html.parser")

    best_movies_title = soup.find_all(name="h3", class_="title")
    titles = [title.get_text() for title in best_movies_title]
    titles.reverse()
    for title in titles:
        file.write(f"{title}\n")



