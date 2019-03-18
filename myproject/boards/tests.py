from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, board_topics
from .models import Board, Topic, Post

# Create your tests here.
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('boards_home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/boards/')
        self.assertEquals(view.func, home) 


class BoardTopicsTests(TestCase):
	# Django testing suite doesn’t run your tests against the current database. 
	# To run the tests Django creates a new database on the fly, applies all 
	# the model migrations, runs the tests, and when done, destroys the testing 
	# database.
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')



    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
