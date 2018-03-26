from django.shortcuts import render, get_object_or_404
from .models import Pic

# Create your views here.
def allpics(request):
    pics = Pic.objects
    return render(request, 'pics/allpics.html', {'pics':pics})

def det(request, pics_id):
    detpic = get_object_or_404(Pic, pk=pics_id)
    return render(request, 'pics/det.html', {'pics': detpic})


# Create your views here.
