import requests
from bs4 import BeautifulSoup
import io

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage,"html.parser")

movie_titles = [movie.getText() for movie in soup.find_all(name="h3")]
print(movie_titles)
movies_order = movie_titles[::-1]
print(movies_order)


with io.open("movies.txt", "w", encoding="utf-8") as file:
    for i in range(100):
        file.write(movies_order[i] + "\n")


file.close()




