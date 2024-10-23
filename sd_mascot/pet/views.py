from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Pet
from django.utils import timezone


def pet_status(request):
    pet = update_pet_stats()

    context = {
        'pet': pet
    }
    return render(request, 'pet/status.html', context)

def feed_pet(request):
    if request.method == 'POST':
        pet = Pet.objects.first()
        pet.hunger = max(0, pet.hunger - 20)  # Feeding reduces hunger
        pet.last_fed = timezone.now()

        # Update health based on the new hunger level
        pet = calculate_health_decay(pet)
        pet.save()

        response_data = {
            'health': pet.health,
            'hunger': pet.hunger,
            'happiness': pet.happiness,
        }
        return JsonResponse(response_data)

def play_with_pet(request):
    if request.method == 'POST':
        pet = Pet.objects.first()
        pet.happiness = min(100, pet.happiness + 20)  # Playing increases happiness
        pet.last_played = timezone.now()

        # Update health based on the new happiness level
        pet = calculate_health_decay(pet)
        pet.save()

        response_data = {
            'health': pet.health,
            'hunger': pet.hunger,
            'happiness': pet.happiness,
        }
        return JsonResponse(response_data)

def calculate_health_decay(pet):
    # Health Decay
    if pet.hunger > 50:
        pet.health = max(0, pet.health - (pet.hunger - 50) // 10)

    if pet.happiness < 50:
        pet.health = max(0, pet.health - (50 - pet.happiness) // 5)

    # Health Regeneration
    if pet.hunger < 30 and pet.happiness > 70:
        pet.health = min(100, pet.health + 5)  # Regenerate health slowly (1 point)

    return pet

def get_pet_stats(_):
    pet = update_pet_stats()
    return JsonResponse(pet)

def update_pet_stats():
    pet = Pet.objects.first()

    # Calculate hunger, happiness, and health decay/regeneration
    time_since_fed = (timezone.now() - pet.last_fed).total_seconds() / 60
    time_since_played = (timezone.now() - pet.last_played).total_seconds() / 60

    pet.hunger = min(100, pet.hunger + round(time_since_fed) * 5)
    pet.happiness = max(0, pet.happiness - round(time_since_played) * 5)
    pet = calculate_health_decay(pet)
    pet.save()

    return {
        'health': pet.health,
        'hunger': pet.hunger,
        'happiness': pet.happiness,
        'name': pet.name,
    }
