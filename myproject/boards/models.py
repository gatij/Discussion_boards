from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Board(models.Model):
	# 'max_legth' used in form validation and 
	# 'Charfield' used in database validation
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    #reverse relationship identified by 'related_name'
    board = models.ForeignKey(Board, on_delete = models.CASCADE,
            related_name='topics')
    #reverse relationship
    starter = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user),
            related_name='topics')

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    #reverse relationship (one to many relationship)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE,
    	  related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    #reverse relationship
    created_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user),
               related_name='posts')
    #reverse relationship ignored using '+'and  
    #this is direct association(intersted in one side of relationship only)
    updated_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user),
               null=True, related_name='+')

    def __str__(self):
        return self.message