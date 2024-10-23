from django.http import JsonResponse
from django.shortcuts import render
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

def feed_mascot(request):
    if request.method == 'POST':
        sd_mascot().feed()
        return JsonResponse(sd_mascot_props())

def play_with_mascot(request):
    if request.method == 'POST':
        sd_mascot().play()
        return JsonResponse(sd_mascot_props())

def get_mascot_state(request):
    if request.method == 'GET':
        sd_mascot().increase_hunger()
        sd_mascot().decrease_happiness()
        return JsonResponse(sd_mascot_props())
