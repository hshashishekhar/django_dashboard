from django.shortcuts import render, redirect

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated
    return render(request, 'dashboard/dashboard.html')

def home(request):
    return render(request, 'dashboard/home.html')

def profile(request):
    return render(request, 'dashboard/profile.html')