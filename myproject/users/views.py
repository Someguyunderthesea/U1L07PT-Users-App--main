import os
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def register(request):
    # posts = Post.objects.all()
    print(f"Looking for template at: {os.path.join('users', 'register.html')}")
    return render(request, "users/register.html")
