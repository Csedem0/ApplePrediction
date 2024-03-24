from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Prediction(models.Model):
    Size = models.FloatField()
    Weight = models.FloatField()
    Sweetness = models.FloatField()
    Crunchiness = models.FloatField()
    Juiciness = models.FloatField()
    Ripeness = models.FloatField()
    Acidity = models.FloatField()
    time_date = models.DateTimeField(default=timezone.now)
    PredictionResult = models.CharField(blank=True, null=True, max_length=30)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

