from django.shortcuts import render, redirect
from lists.models import Item
from django.http import HttpResponse

# Create your views here.
def home_page(request):

    new_item_text = request.POST.get('item_text', '')
    if request.method == 'POST' and new_item_text != '':
        Item.objects.create(text=new_item_text)
        return redirect('/')

    return render(request, 'lists/home.html', {
        'items': [new_item_text]
    })