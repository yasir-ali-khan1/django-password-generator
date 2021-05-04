from django.shortcuts import render

# Create your  fvjn views here.
def all_blogs(request):
    return render(request, 'all_blogs.html')