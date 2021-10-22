from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero    

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)
# 4
def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id) 
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    print(request.method)
    if request.method == 'POST':
        # save the form contents as a new db object
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catch_phrase=catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    elif request.method == 'GET':
        return render(request, 'superheroes/create.html')

def update_hero(request, hero_id):
    print(request.method)
    # If request.method is POST 
        # Get the superhero from the database using the "hero_id" parameter value
    if request.method == 'POST':
        update_hero = Superhero.objects.get(pk=hero_id) 
        update_hero.name = request.POST.get('name')
        update_hero.alter_ego = request.POST.get('alter_ego')
        update_hero.primary_ability = request.POST.get('primary_ability')
        update_hero.secondary_ability = request.POST.get('secondary_ability')
        update_hero.catch_phrase = request.POST.get('catch_phrase')
        update_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
        
    # If request.method is GET
        # Get the superhero from the database using the "hero_id" parameter value
        # Create a context object with that superhero from the db inside of it
        # Bring up the update.html page and send in the superhero object
    elif request.method == 'GET':
        update_hero = Superhero.objects.get(pk=hero_id) 
        context = {
            'update_hero': update_hero
        }
        return render(request, 'superheroes/update_hero.html', context)

def delete_hero(request, hero_id):
    delete_hero = Superhero.objects.get(pk=hero_id)
    delete_hero.delete()
    return redirect(reverse('superheroes:index'))