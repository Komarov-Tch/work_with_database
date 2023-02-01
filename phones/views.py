from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    s = request.GET.get('sort', '')
    if s == 'name':
        phones = Phone.objects.all().order_by(s)
    elif s == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif s == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.filter(slug=slug).first()
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
