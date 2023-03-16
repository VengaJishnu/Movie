from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cinema
from .forms import Movieform


# Create your views here.

def demo(request):
    # return HttpResponse("hello world")
    items = cinema.objects.all()
    content = {'movie': items}
    return render(request, 'welcome.html', content)


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name1')
        desc = request.POST.get('desc3')
        budget = request.POST.get('budget2')
        img = request.FILES['img4']  # only here it should be [] brackets
        movie = cinema(name1=name, desc3=desc, budget2=budget, img4=img)
        movie.save()  # movie is a variable name
    return render(request, 'add.html')


def movie_id(request, movie_id):
    movie1 = cinema.objects.get(id=movie_id)
    return render(request, 'movie_details.html', {'movie1': movie1})
    # return HttpResponse("movie.jpeg id is %s" % movie_id)  # %s is just to show the value isnide a comment ,movie_id is just a id number


def edit(request, id):
    movie = cinema.objects.get(id=id)
    form = Movieform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "edit.html", {'form': form, 'movie': movie})


def delete(requset, id):
    if requset.method == "POST":
        movie = cinema.objects.get(id=id)
        movie.delete()
        return render(requset,"welcome.html")
    return render(requset,"delete.html")
