from django.shortcuts import render
from django.http import HttpResponse
from .models import Newspaper
from django.contrib.admin.views.decorators import staff_member_required

home='home'
def homepage(request):
    return render(request = request, template_name = 'newsroom/home.html')
    
@staff_member_required
def howtoguide(request):
    return render(request = request, template_name = 'newsroom/howtoguide.html')

def newspaper_detail(request, SLUG):
    all_newspapers= Newspaper.objects.all()
    this_newspaper = Newspaper.objects.filter(slug=SLUG).first()
    return render(request = request, 
    template_name = 'newsroom/newspaper_detail.html', 
    context = {'this_newspaper':this_newspaper, 'all_newspapers':all_newspapers})
    
def newsroom(request):
    all_newspapers= Newspaper.objects.all()
    return render(request = request, 
    template_name = 'newsroom/newsroom.html', 
    context = {'all_newspapers':all_newspapers[::-1]})