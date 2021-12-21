from django.contrib.auth.models import User
from django.test import TestCase, Client
from .models import Actor, Movie
from serializers import ActorSerializer, CommentSerializer, MovieSerializer

class TestMovieList(TestCase):
    def setUp(self) -> None:
        self.cl = Client()
        self.actor = Actor.objects.create(name="Raj Kapoor", gender="Male", birth_date='1956-04-13')
        self.movie = Movie.objects.create(name="421", genre="Comedy", imdb=6.9, year='1978-09-18')
        self.movie.actor.add(self.actor)

    def test_all_movies(self):
        movies = self.cl.get('/movie/').data
        assert len(movies) == 1
        assert movies[0]['id'] is not None
        assert movies[0]['name'] == '421'
        assert movies[0]['genre'] == 'Comedy'
        assert movies[0]['imdb'] > 6.0

class TestActorListCreateView(TestCase):
    def setUp(self) -> None:
        self.cl = Client()

    def test_post_an_actor(self):
        aktyor = {
            "id":1,
            "name":"Ulug'bek Qodirov",
            "birth_date":'1985-10-23',
            "gender":"Male"
        }
        ak2 = {
            "id":1,
            "name":"Tom Hardy",
            "birth_date":'1977-10-23',
            "gender":"Male"
        }
        a = self.cl.post("/actor/", data=aktyor)
        b = self.cl.post("/actor/", data=ak2)
        assert a.status_code == 201
        assert b.status_code == 201
        actors = self.cl.get("/actor/").data
        assert len(actors) > 0
        assert actors[0]['id'] is not None
        assert actors[0]['name'] == "Ulug'bek Qodirov"
        assert actors[0]['gender'] == "Male"
        assert actors[0]['birth_date'] == '1985-10-23'

class TestMovieListCreateView(TestCase):
    def setUp(self) -> None:
        self.cl = Client()

    def test_post_a_movie(self):
        aktyor = {
            "id": 1,
            "name": "Ulug'bek Qodirov",
            "birth_date": '1985-10-23',
            "gender": "Male"
        }
        a = self.cl.post("/actor/", data=aktyor)
        b = self.cl.post("/actor/", data=aktyor)
        kino = {
            "id":1,
            "name":"3 Savdoyi",
            "imdb":7.3,
            "genre":"Comedy",
            "year":'2005-05-10',
            "actor":[1]
        }
        m1 = self.cl.post("/movie/", data=kino)
        movies = self.cl.get("/movie/").data
        print(movies)
        # assert actors[0]['id'] is not None
        # assert actors[0]['name'] == "Ulug'bek Qodirov"
        # assert actors[0]['gender'] == "Male"
        # assert actors[0]['birth_date'] == '1985-10-23'