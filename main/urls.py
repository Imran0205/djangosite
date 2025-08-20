from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('a', views.a, name='a'),
    path('lang', views.lang, name='lang'),
    path('lang/<int:pk>', views.langDetailView.as_view(), name='detail'),
    path('createadvice', views.create_advice, name='createadvice'),
    path('advice', views.advice, name='advice'),
]