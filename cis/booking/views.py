from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservationTimeForm
from .models import Shelf, Reservation
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

@login_required
def reservation_view(request):
    form = ReservationTimeForm(request.POST or None)
    available_shelves = None
    selected_start = None
    selected_end = None
    if form.is_valid():
        selected_start = form.cleaned_data['start_time']
        selected_end = form.cleaned_data['end_time']

        # Retrieve all shelves
        all_shelves = Shelf.objects.all()

        # Retrieve reservations overlapping with the selected interval
        overlapping_reservations = Reservation.objects.filter(
            Q(start_time__lt=selected_end) & Q(end_time__gt=selected_start)
        )
        reserved_shelf_ids = overlapping_reservations.values_list('shelf_id', flat=True)

        # Available shelves – those not included in the overlapping reservations
        available_shelves = all_shelves.exclude(id__in=reserved_shelf_ids)

    context = {
        'form': form,
        'available_shelves': available_shelves,
        'selected_start': selected_start,
        'selected_end': selected_end,
    }
    return render(request, 'booking/reservation.html', context)

@login_required
def book_shelf(request, shelf_id):
    if request.method == 'POST':
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        
        if not start_time_str or not end_time_str:
            messages.error(request, "Time values are missing.")
            return redirect('reservation')
        
        # Replace time designations: "a.m." to "AM" and "p.m." to "PM"
        cleaned_start_time = start_time_str.replace("a.m.", "AM").replace("p.m.", "PM")
        cleaned_end_time = end_time_str.replace("a.m.", "AM").replace("p.m.", "PM")
        
        try:
            # Try parsing the string with the month abbreviation including a dot
            start_time = datetime.strptime(cleaned_start_time, "%b. %d, %Y, %I:%M %p")
            end_time = datetime.strptime(cleaned_end_time, "%b. %d, %Y, %I:%M %p")
        except ValueError as e:
            # If that fails, try parsing without the dot in the month abbreviation
            try:
                start_time = datetime.strptime(cleaned_start_time, "%b %d, %Y, %I:%M %p")
                end_time = datetime.strptime(cleaned_end_time, "%b %d, %Y, %I:%M %p")
            except ValueError as e:
                messages.error(request, f"Error converting date/time: {e}")
                return redirect('reservation')
        
        shelf = get_object_or_404(Shelf, id=shelf_id)
        
        # Now filter reservations by comparing datetime objects
        overlapping = Reservation.objects.filter(
            shelf=shelf,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping.exists():
            messages.error(request, "This shelf is already booked for the selected time.")
        else:
            Reservation.objects.create(
                teacher=request.user,
                shelf=shelf,
                start_time=start_time,
                end_time=end_time
            )
            messages.success(request, f"Shelf {shelf} has been successfully booked.")
    return redirect('reservation')

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, teacher=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Booking cancelled.")
    return redirect('reservation')


def parse_custom_datetime(dt_str):
    """
    Converts a string of the form 'Feb. 6, 2025, 12:50 a.m.' or 'March 5, 2025, 12:02 AM'
    to a datetime object.
    """
    dt_str = dt_str.strip()
    # Заменяем обозначения времени
    dt_str = dt_str.replace("a.m.", "AM").replace("p.m.", "PM")
    
    # Список форматов для попытки парсинга
    formats = [
        "%b. %d, %Y, %I:%M %p",  # с точкой в сокращённом названии месяца, например "Feb."
        "%b %d, %Y, %I:%M %p",   # без точки, например "Feb"
        "%B %d, %Y, %I:%M %p"    # с полным названием месяца, например "March"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(dt_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"time data {dt_str!r} does not match any supported format")

@login_required
def book_multiple(request):
    if request.method == "POST":
        start_time_str = request.POST.get("start_time")
        end_time_str = request.POST.get("end_time")
        selected_shelves_str = request.POST.get("selected_shelves")

        if not (start_time_str and end_time_str and selected_shelves_str):
            messages.error(request, "Time interval not specified or no laptops selected.")
            return redirect("reservation")

        try:
            start_time = parse_custom_datetime(start_time_str)
            end_time = parse_custom_datetime(end_time_str)
        except ValueError as e:
            messages.error(request, f"Error converting date/time: {e}")
            return redirect("reservation")

        shelf_ids = selected_shelves_str.split(",")
        if not shelf_ids or shelf_ids == ['']:
            messages.error(request, "No laptops selected for booking.")
            return redirect("reservation")

        success_count = 0
        for shelf_id in shelf_ids:
            shelf = get_object_or_404(Shelf, id=shelf_id)
            # Check for overlapping reservations
            overlapping = Reservation.objects.filter(
                shelf=shelf,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if overlapping.exists():
                messages.warning(request, f"Laptop {shelf} is already booked for the selected time.")
                continue
            Reservation.objects.create(
                teacher=request.user,
                shelf=shelf,
                start_time=start_time,
                end_time=end_time
            )
            success_count += 1

        if success_count:
            messages.success(request, f"Booking for {success_count} laptop(s) has been successfully created.")
        return redirect("reservation")
    return redirect("reservation")

def custom_logout(request):
    # Завершаем сессию пользователя
    logout(request)
    # Перенаправляем на главную страницу
    response = redirect('/')
    # Удаляем cookie с именем 'sessionid'
    response.delete_cookie('sessionid')
    return response

@login_required
@require_POST
def cancel_reservation_group(request):
    # Получаем список ID бронирований из POST-запроса
    reservation_ids = request.POST.getlist('reservation_ids')
    
    # Фильтруем бронирования, принадлежащие текущему пользователю и входящие в переданный список
    reservations = Reservation.objects.filter(id__in=reservation_ids, teacher=request.user)
    
    # Удаляем найденные бронирования
    reservations.delete()
    messages.success(request, "Booking cancelled!")
    # Перенаправляем пользователя на страницу с бронированиями (например, на 'reservation_view')
    return redirect('reservation')
