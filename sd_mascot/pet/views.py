from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET

from .models import Pet

@require_GET
def mascot_index(request):
    return render(request, 'pet/status.html', { 'pet': sd_mascot()})

def sd_mascot():
    return Pet.objects.first()

def sd_mascot_props():
    return {
            'health': sd_mascot().health,
            'hunger': sd_mascot().hunger,
            'happiness': sd_mascot().happiness,
            'health_state': sd_mascot().health_state.name,
            'name': sd_mascot().name,
        }

@require_POST
def feed_mascot(request):
    try:
        sd_mascot().feed()
    except:
        raise

    return JsonResponse(sd_mascot_props())
    sd_mascot().feed()

@require_POST
def play_with_mascot(request):
    try:
        sd_mascot().play()
    except:
        raise BaseException()
    return JsonResponse(sd_mascot_props())
    sd_mascot().feed()

@require_GET
def update_mascot_state(request):
    sd_mascot().increase_hunger()
    sd_mascot().decrease_happiness()
    return JsonResponse(sd_mascot_props())
    sd_mascot().feed()

def foo():
    pass