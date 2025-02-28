from django.shortcuts import render, redirect

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated
    return render(request, 'dashboard/dashboard.html')

def home(request):
    return render(request, 'dashboard/home.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def settings(request):
    return render(request, 'dashboard/settings.html')

def invoice(request):
    return render(request, 'dashboard/invoice.html')

def crm(request):
    return render(request, 'dashboard/crm.html')

def kanban(request):
    return render(request, 'dashboard/kanban.html')