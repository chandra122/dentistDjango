from django.shortcuts import render
from django.template import Context
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        send_email(
            message_name, # subject
            message, # message
            message_email, # from email
            ['sekharchandu474@gmail.com'] # To email
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def pricing(request):
    return render(request, 'pricing.html')

def appointment(request):
    if request == 'POST':
        your_name = request.post['your-name']
        your_phone = request.post['your-phone']
        your_email = request.post['your-email']
        your_address = request.post['your-address']
        your_schedule = request.post['your-schedule']
        your_time = request.post['your-time']
        your_message = request.post['your-message']
        context = Context({'your_schedule' : your_schedule})
        return render(request, 'appointment.html', context)
    else:
        return render(request, 'appointment.html', {})

def csrf_failure(request, reason=""):
    ctx = {'message': 'Lets see how this works'}
    return render('home.html', ctx)