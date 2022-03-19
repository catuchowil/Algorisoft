from django.shortcuts import render

from.models import Category

# Create your views here.
def category_list(request):
    data = {
        'title':'Listado de Categorías',
        'categories':Category.objects.all()
    }
    return render(request, 'erp/list.html',data)
