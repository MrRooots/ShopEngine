from django.db import models
from django.utils.text import slugify
from time import time
from random import randint, choice

# Build Slug from item title
def build_slug(t):  
  return slugify(t, allow_unicode=True) + str(int(time()))[:8] + str(randint(1, 150))

# item = Item.objects.create(title='First item title', description='flsdgfhsdlfhalsdfucnosrungfxdshalfgovurcgfnkshgfwycergfnkssgkhsdgk', price=125.00, rating=4.25, sizes='XS|S|M|L', colors='White|Black')
def create_items(count):
  titles = [
    'First item', 'hilfiger shoes', 'lacoste shoes', 'levi\'s jeans', 'second item'
  ]
  prices = [
    125, 150, 200, 225.33, 365, 378.48, 452.23
  ]
  colors = [
    'White', 'White|Black', 'Black|Yellow|Pink|White', 'Hacki|Lemon|White|Black'
  ]
  ratings = [
    1, 1.5, 2, 2.25, 3, 3.45, 3.75, 4, 4.32, 5
  ]
  sizes = [
    'S', 'S|M', 'XS|S|M|XL', 'M|L|XL', 'S|M|L|XL'
  ]
  
  for i in range(count):
    Item.objects.create(
      title=choice(titles), price=choice(prices), rating=choice(ratings), colors=choice(colors), sizes=choice(sizes)
    )


class Item(models.Model):
  title = models.CharField(max_length=50)   
  description = models.TextField()
  slug = models.SlugField(unique=True)
  price = models.FloatField()
  rating = models.FloatField()               # The deciminal number
  sizes = models.CharField(max_length=150)   # Avaliable sizes in format: XS|S|M|L|XL
  colors = models.CharField(max_length=150)  # Avaliable colors in format: White|Black

  def save(self, *args, **kwargs):
    self.title = self.title.title()
    if not self.slug:
      self.slug = build_slug(self.title)

    return super().save(*args, **kwargs)

  def __str__(self):
    return self.title


