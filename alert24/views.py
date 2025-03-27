from django.shortcuts import render
from main.models import categories,News
from .form import students


def search(request):
    query = request.GET.get('search')
    data = News.objects.filter(title__icontains = query)
    context ={
        'news':data
    }
    return render(request, 'search.html', context)

def studentsview(request):
    sf = students()
    context ={
        'fm':sf
    }
    return render(request, 'form.html', context)


def home(request):
    category = categories.objects.all()
    allnews = News.objects.all().order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
               'categories':category,
               'allnews':allnews,
               'topnews':topnews,
               'title':'alert24 | Home'
            }
    return render(request, 'index.html', context)


def allnews(request):
    category = categories.objects.all()
    Allnews = News.objects.all().order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
               'categories':category,
               'Allnews':Allnews,
               'topnews':topnews,
               'title':'alert24 | Home'
            }
    return render(request, 'categories/AllNews.html', context)

def india(request):
    category = categories.objects.all()
    indianews = News.objects.filter(category__title='India News').order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'indianews':indianews,
        'topnews':topnews,
        'title':'alert24 | India'    
        }
    return render(request, 'categories/india.html', context)


def bollywood(request):
    category = categories.objects.all()
    bollynews = News.objects.filter(category__title='Bollywood News').order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'bollynews':bollynews,
        'topnews':topnews,
        'title':'alert24 | Bollywood'    
        }
    return render(request, 'categories/bollywood.html', context)


def sports(request):

    category = categories.objects.all()
    sportsnews = News.objects.filter(category__title='Sports News').order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'sportsnews':sportsnews,
        'topnews':topnews,
        'title':'alert24 | Sports'    
        }
    return render(request, 'categories/sports.html', context)


def health(request):
    
    category = categories.objects.all()
    healthnews = News.objects.filter(category__title='Health News').order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'healthnews':healthnews,
        'topnews':topnews,  
        'title':'alert24 | Health'
        }
    return render(request, 'categories/health.html', context)


def contact(request):
    category = categories.objects.all()
    contactnews = News.objects.all()
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'topnews':topnews,  
        'title':'alert24 | Health'
        }
    return render(request, 'categories/contact.html', context)


def entertainment(request):
    category = categories.objects.all()
    enternews = News.objects.filter(category__title='Entertainment News').order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'enternews':enternews,
        'topnews':topnews,  
        'title':'alert24 | Entertainment'
        }
    return render(request, 'categories/entertainment.html', context)


def political(request):
    
    category = categories.objects.all()
    politicalnews = News.objects.filter(category__title='Political News').order_by('-id')
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'categories':category,
        'politicalnews':politicalnews,
        'topnews':topnews,  
        'title':'alert24 | political'
        }
    return render(request, 'categories/political.html', context)

def details(request, id):
    category = categories.objects.all()
    news = News.objects.get(pk = id)
    topnews = News.objects.order_by('-id')[:5]
    context = {
        'news':news,
        'topnews':topnews,  
        }
    return render(request, 'details.html', context)
