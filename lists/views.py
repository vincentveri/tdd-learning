from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    item_text = request.POST.get('item_text', '')
    return render(request, 'lists/home.html', {
        'items': [item_text]
    })