import tmdb_client
from main import app
from unittest.mock import Mock

def test_get_movies_list(monkeypatch):
   mock_movies_list = []
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
   mock_single_movie = []
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   single_movie = tmdb_client.get_single_movie(movie_id='634649')
   assert single_movie == mock_single_movie

def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = []
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   single_movie = tmdb_client.get_single_movie_cast(movie_id='634649')
   assert single_movie == mock_single_movie_cast

