from db.models import Movie


def get_movies(genres_ids: list=[], actors_ids: list=[]) -> list:
    movies = Movie.query.all()
    if not genres_ids and not actors_ids:
        return movies