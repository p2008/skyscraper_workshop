from django.shortcuts import render

from rooms.models import Room, Reservation


def all_rooms(request):
    rooms = Room.objects.order_by('pk')

    return render(request, 'all_rooms_view.html', {'rooms': rooms})
