from statistics import mode
from django.db import models
from django.urls import reverse

RATING = (
  ('1','Very Bad'),
  ('2','Somewhat Bad'),
  ('3','Okay'),
  ('4','Pretty Good'),
  ('5','Very Good'),
)

class Item(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("items_detail", kwargs={"pk": self.id})
  

# Create your models here.
class Swallow(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  speed = models.FloatField()
  items = models.ManyToManyField(Item)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("swallows_detail", kwargs={"swallow_id": self.id})

class Migration(models.Model):
  destination = models.CharField(max_length=100)
  rating = models.CharField(max_length=1, choices=RATING, default=RATING[0][0])
  swallow = models.ForeignKey(Swallow, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'{self.destination} is {self.get_rating_display()}'
  
