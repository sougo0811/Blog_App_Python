from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Product

def index(request):
    return render(request, 'yatoi_lab/index.html', {})