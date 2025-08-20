from django.shortcuts import render
from .models import newsl
# Create your views here.
def newsmain(request):
    news = newsl.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})
