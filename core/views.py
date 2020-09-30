from django.shortcuts import render, redirect
from .models import *

# Display the intro page of website
def display_shop(request):
  best_items = sorted(Item.objects.all(), key=lambda item: item.rating, reverse=True)

  context = {
    'bestsellers': best_items[:4],
    'best_items': best_items[:10],
  }

  return render(request, 'core/main.html', context=context)