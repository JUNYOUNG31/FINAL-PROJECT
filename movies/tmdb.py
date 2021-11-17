import requests


ret = []

for page in range(1, 51):
    url = "https://api.themoviedb.org/3/movie/popular?api_key=16d1729d729f6d8c5d36bfaba0aee1a6&language=ko-KR&page=" + str(page)
    res = requests.get(url).json()
    movies = res["results"]

    for movie in movies:
        ret.append(movie)

###########################################################
    
import json

file = open("../data/moviedata.json", "w+") 

with file as f:
    file.write(json.dump(ret, f, indent=4))

############################################################

file = open("../data/moviedata.json", "r") 

with file as f:
    json_data = json.load(f)
    json_data = json.dumps(f, ensure_ascii=False)