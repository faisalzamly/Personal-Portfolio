from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == "POST":
        subject = request.POST['subject']
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        subjectfrom = "My name is "+ name +"User Email is : " + email +" Subject : "
        Massage1 = subjectfrom+message
        send_mail(
            subject,
            Massage1,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        # Contact.objects.create(email=email, subject=subject, message=message)
        return render(request, "thank-you.html")
    return render(request, "index.html")

