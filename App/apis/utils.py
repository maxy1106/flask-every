import uuid

MOVIEUSER = "movie_user"
ADMINUSER = "admin_user"
CINEMAUSER = "cinema_user"

def generator_token(prefix=None):
    token = prefix + uuid.uuid4().hex
    return token

def generator_movie_user_token():
    return generator_token(MOVIEUSER)

def generator_admin_user_token():
    return generator_token(ADMINUSER)

def generator_cinema_user_token():
    return generator_token(CINEMAUSER)
