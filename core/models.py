from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Fixture(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_fixtures')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_fixtures')

    home_goals = models.IntegerField(null=True, blank=True)
    away_goals = models.IntegerField(null=True, blank=True)

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE, related_name='predictions')
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()

    def __str__(self):
        return f"{self.fixture.home_team.name} {self.home_goals} - {self.away_goals} {self.fixture.away_team.name}"