from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import *
# Create your views here.

def error(request):
    return render(request, '404.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def index(request):

 if request.method == 'POST':
    myContact = Contact(
        name=request.POST['name'],
        email=request.POST['email'],
        subject=request.POST['subject'],
        message=request.POST['message']
    )

    myContact.save()
    return redirect('/')

 else:
    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request='starter-page.html')


def show(request):
   all = Contact.objects.all()
   return render(request, 'show.html' ,{"all" : all})

def delete(request, id):
   Contactinfo = Contact.objects.get(id=id)
   Contactinfo.delete()
   return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.subject = request.POST.get('subject')
        editappointment.message = request.POST.get('message')

        editappointment.save()
        return redirect('/show')

    return render(request, 'edit.html', {
        'editappointment': editappointment
    })

   


