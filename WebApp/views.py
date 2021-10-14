from django.shortcuts import render
def inicio(request):
    return render(request, 'test-page-v2.html', {})

# Create your views here.
