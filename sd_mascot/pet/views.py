from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET

from .models import Pet

def mascot_index(request):
    return render(request, 'pet/status.html', { 'pet': sd_mascot()})

def sd_mascot():
    return Pet.objects.first()

def sd_mascot_props():
    return {
            'health': sd_mascot().health,
            'hunger': sd_mascot().hunger,
            'happiness': sd_mascot().happiness,
            'name': sd_mascot().name,
        }

@require_POST
def feed_mascot(request):
    sd_mascot().feed()
    return JsonResponse(sd_mascot_props())

@require_POST
def play_with_mascot(request):
    sd_mascot().play()
    return JsonResponse(sd_mascot_props())

@require_GET
def update_mascot_state(request):
    sd_mascot().increase_hunger()
    sd_mascot().decrease_happiness()
    return JsonResponse(sd_mascot_props())
