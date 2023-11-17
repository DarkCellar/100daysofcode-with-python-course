from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
import os

Movie = namedtuple('Movie', 'title year score gross')
movies_csv = os.path.join(".\\", "movies.csv")

def main():
    #movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
    #urlretrieve(movie_data, movies_csv)

    directors = get_movies_by_director(movies_csv)

    cnt = Counter()
    #print(directors.items())
    for director, movies in directors.items():
        cnt[director] += len(movies)

    print(cnt.most_common(5))


def get_movies_by_director(data):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
                gross = float(line['gross'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score, gross=gross)
            if m.year >= 1960:
                directors[director].append(m)

    return directors


if __name__ == "__main__":
    main()
