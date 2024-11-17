import csv
import json

list = []

with open("netflix_titles.tsv", mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        title = row["PRIMARYTITLE"]
        if row["PRIMARYTITLE"]:
            titles = row["PRIMARYTITLE"].split(",")
        else:
            titles = []
        if row["DIRECTOR"]:
            directors = row["DIRECTOR"].split(",")
        else:
            directors = []
        if row["CAST"]:
            cast = row["CAST"].split(",")
        else:
            cast = []
        if row["GENRES"]:
            genres = row["GENRES"].split(",")
        else:
            genres = []
        if row["STARTYEAR"].isdigit():
            year = int(row["STARTYEAR"])
            decade = (year // 10) * 10
        else:
            decade = None
        movie_dictionary = {
            "title": [title.strip() for title in titles if title.strip()],
            "director": [director.strip() for director in directors if director.strip()],
            "cast": [actor.strip() for actor in cast if actor.strip()],
            "genres": [genre.strip() for genre in genres if genre.strip()],
            "decade": decade
        }
        list.append(movie_dictionary)
with open("hw02_output.json", mode='w', encoding='utf-8') as json_file:
    json.dump(list, json_file, indent=4, ensure_ascii=False)
