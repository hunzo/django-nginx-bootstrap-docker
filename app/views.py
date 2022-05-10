from django.shortcuts import render

# Create your views here.

def index(request):
    x_forwarded_for = request.META.get('X-Forwarded-For')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    context = {
        "ip": ip
    }
    return render(request, 'contents.html', context)
