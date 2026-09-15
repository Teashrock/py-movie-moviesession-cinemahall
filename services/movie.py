from db.models import Movie


def get_movies(
        genres_ids: list = [],
        actors_ids: list = []
) -> list[Movie]:
    movies = Movie.objects.all()
    if not genres_ids and not actors_ids:
        return movies
    if genres_ids and actors_ids:
        return movies.filter(genres__id__in=genres_ids).filter(actors__id__in=actors_ids).all()
    if genres_ids:
        return movies.filter(genres__id__in=genres_ids).all()
    if actors_ids:
        return movies.filter(actors__id__in=actors_ids).all()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genre_ids: list = [],
        actors_ids: list = []
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )
    if genre_ids:
        movie.genres.set(genre_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    movie.save()
    return movie
