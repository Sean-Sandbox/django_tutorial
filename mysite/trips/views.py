from django.shortcuts import render
from datetime import datetime

# Create your views here.
def hello_world(request):
    test_list = [1,3,5,7,9]
    return render(request, 'hello_world.html', {
        'current_time':str(datetime.now()),
        'test_list':test_list,
    })

def home(request):
    return render(request, 'home.html', {
        'say_hi':'Hello, this is our home page!',
    })
