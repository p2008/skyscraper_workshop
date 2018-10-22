from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rooms.models import Room
from django.contrib import messages


# No.5: As a user, I want to remove room on click remove.
def room_remove(request, rid):
    try:
        room = Room.objects.get(pk=rid)
        room.delete()
        messages.success(request, f'Usunięto salę {room.name}')
    except ObjectDoesNotExist:
        messages.success(request, 'Sali nie znaleziono')  ## TODO ask Paweł about messages methods

    return render(request, 'room_remove_view.html')