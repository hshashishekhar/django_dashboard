# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def custom_logout(request):
    logout(request)  # Log the user out
    messages.success(request, 'You have been logged out successfully.')  # Add a success message
    return redirect('login')  # Redirect to the login page

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


# class CustomPasswordResetView(auth_views.PasswordResetView):
#     template_name = 'authentication/custom_password_reset_form.html'  # Custom template
#     email_template_name = 'authentication/custom_password_reset_email.html'  # Custom email template
#     subject_template_name = 'authentication/custom_password_reset_subject.txt'  # Custom email subject
#     success_url = reverse_lazy('password_reset_done')  # URL to redirect after submission

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'authentication/custom_password_reset_done.html'  # Custom template

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'authentication/custom_password_reset_confirm.html'  # Custom template
    success_url = reverse_lazy('password_reset_complete')  # URL to redirect after successful reset

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'authentication/custom_password_reset_complete.html'  # Custom template

class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'authentication/custom_password_reset_form.html'
    email_template_name = 'authentication/custom_password_reset_email.html'
    subject_template_name = 'authentication/custom_password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    from_email = settings.EMAIL_HOST_USER
    html_email_template_name = 'authentication/custom_password_reset_email.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            # Don't reveal that the user doesn't exist
            return super().form_valid(form)
        return super().form_valid(form)