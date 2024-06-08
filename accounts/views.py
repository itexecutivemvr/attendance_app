from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from geopy.geocoders import Nominatim
from .models import Log

# Create your views here.
def dashboard(request):
    total_users = User.objects.count()
    total_logs = Log.objects.count()

    # Retrieve attendance data for display on the dashboard
    attendance_data = Log.objects.all().order_by('-current_date', '-current_time')[:10]

    return render(request, 'dashboard.html', {
        'total_users': total_users,
        'total_logs': total_logs,
        'attendance_data': attendance_data,
    })
def attend(request):
    if request.method == "POST":
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        geolocator = Nominatim(user_agent="attendance_app", timeout=10)
        location = geolocator.reverse(f"{latitude}, {longitude}")

        if location:
            place_name = location.address
        else:
            place_name = "Unknown location"

        # Create a new Log object and save it to the database
        log = Log(username=username, current_time=time, current_date=date, location=place_name)
        log.save()

        # Optionally, you can add a success message
        messages.success(request, 'Attendance marked successfully')

        # Redirect to the same page or to a different page
        return redirect('attend')

    return render(request, "attendance.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('attend')
        else:
            messages.info(request, 'Invalid details')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password1)
            user.save()
        else:
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')
