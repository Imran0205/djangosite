from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  adviceslol
from .models import advices, langmod
from django.views.generic import DetailView
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def lang(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
        is_mobile = True
    else:
        is_mobile = False

    langu = langmod.objects.all()
    return render(request, 'main/lang.html', {'langu': langu}, {'is_mobile': is_mobile})

class langDetailView(DetailView):
    model = langmod
    template_name = 'main/details.html'
    context_object_name = 'langdetails'

def a(request):
    return render(request, 'main/a.html')

def create_advice(request):
    session_data = {}
    error = ''
    if request.method == "POST":
        hi = adviceslol(request.POST)
        if hi.is_valid():
            request.session['form_data'] = {
                'Name': hi.cleaned_data['Name'],
                'Advice': hi.cleaned_data['Advice']
            }
            hi.save()
            return redirect('advice')
        else:
            error = 'Введите правильно'
            session_data = request.session.get('form_data', {})
    lol = adviceslol(initial=session_data)

    i = {
        'lol': lol,
        'error': error
    }
    return render(request, 'main/createadvice.html', i)

def advice(request):
    advicess = advices.objects.all()
    return render(request, 'main/advice.html', {'advicess': advicess})
