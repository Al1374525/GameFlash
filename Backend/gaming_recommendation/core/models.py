from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    rating  = models.FloatField()
    release_date = models.DateField(null=True, blank=True)
    developer = models.CharField(max_length=100, null=True, blank=True)
    platform = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.FloatField()
    review_date = models.DateTimeField()

    def __str__(self):
        return  f'Review by{self.user.username} on {self.game.title}'

class UserGameInteraction(models.Model):
    INTERACTION_CHOICES = {
        ('viewed', 'Viewed'),
        ('liked', 'Liked'),
        ('played', 'Played'),
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_interactions')
    game = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_interactions' )
    interaction_type = models.CharField(max_length=10, choices=INTERACTION_CHOICES)
    interation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.interaction_type}, {self.game.title}'