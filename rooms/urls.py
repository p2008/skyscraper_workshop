from django.urls import path
from .view import (all_rooms_view,
                   room_remove_view,
                   edit_room_view,
                   room_details_view,
                   room_reservation_view)

# import all_rooms_view, rooms_remove, edit_room_view

urlpatterns = [
    # Paweł
    path('', all_rooms_view.all_rooms, name='all_rooms'),
    path('edit_room/', edit_room_view.EditRoom.as_view(),
         name='edit_room'),

    # Mateusz
    # place your code here

    # Kewin
    path('reservation/<int:rid>/', room_reservation_view.room_reservation, name='room_reservations'),

    # Artem
    path('remove/<int:rid>/', room_remove_view.room_remove, name='room_remove'),
    path('details/<int:rid>/', room_details_view.room_details, name='room_details'),
]
