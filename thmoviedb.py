import requests


class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "0d4edbbcefc23026c46f1dea0448248a"

    def getPopulers(self):
        responce = requests.get(f"{self.api_url}+/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return responce.json()

    def getSearchResults(self, Keyword):
        response = requests.get(f"{self.api_url}/search/keywordapi_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movieApi = theMovieDb()

while True:
    secim = input("1- Populer Movies\n2- Search\n3- Exit\nSeçim :")

    if secim == "3":
        break
    if secim == "1":
        movies = movieApi.getPopulers()
        for movie in movies['results']:
            print(movie["title"])
    if secim == "2":
        keyword = input("keyword : ")
        movies = movieApi.getSearchResults(keyword)
        for movie in movies["results"]:
            print(movie["name"])
