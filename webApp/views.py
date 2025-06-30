from django.shortcuts import render

# Create your views here.


from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def contact(request):
    context = {}
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            send_mail(
                subject=f"New Contact Message from {name}",
                message=message + f"\n\nEmail: {email}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['alex7490.ander@gmail.com'],
                fail_silently=False,
            )
            context['success'] = True
        except:
            context['error'] = True
    return render(request, 'index.html', context)

