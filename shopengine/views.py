from django.shortcuts import render, redirect

def redirect_to_shop(request):
  return redirect('shop/')