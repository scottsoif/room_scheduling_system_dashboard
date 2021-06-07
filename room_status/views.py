from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Rooms


def index(request):
    room_status_list = get_room_grid()

    return render(request, 'room_grid.html', room_status_list)

def update_status(request): # room_number):

    # get params from request
    room_id = request.GET.get("room_number", None)
    is_open = request.GET.get("is_open", None)

    # clean up name and boolean for is_open
    room_name = f"Room{room_id}"
    is_open = True if is_open=="1" else False
    print("Room name and new status  ", room_name, is_open)

    try:
        # update the object
        Rooms.objects.filter(room_name=room_name).update(is_open=is_open)

        # get the object for debugging
        obj2 = Rooms.objects.get(room_name=room_name)
        print(obj2.is_open)
    except Exception as e:
        print("error  ", e)

    room_status_list = get_room_grid()

    return redirect('/room_status', room_status_list)


def toggle(request):

    # get param from request
    room_id = request.GET.get("room_number", None)

    # clean up name
    room_name = f"Room{room_id}"
    is_open = Rooms.objects.get(room_name=room_name).is_open

    print("Room name and current status  ", room_name, is_open)

    try:

        is_open = not is_open # flip the current status

        # update the object
        Rooms.objects.filter(room_name=room_name).update(is_open=is_open)

        # get the object for debugging
        obj2 = Rooms.objects.get(room_name=room_name)
        print(obj2.is_open)
    except Exception as e:
        print("error  ", e)

    room_status_list = get_room_grid()

    return redirect('/room_status', room_status_list)


def get_room_grid():
    status_grid = {}

    for r in Rooms.objects.all():
        color = "bg-success" if r.is_open else "bg-danger"
        status_grid[r.room_name] = color

    return status_grid


