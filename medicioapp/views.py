from django.shortcuts import render, redirect
from medicioapp.models import Contact, Appointment, Member, ImageModel
from medicioapp.forms import AppointmentForm, ImageUploadForm


# Create your views here.
def index(request):
    if request.method=='POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'] ).exists():
             members = Member.objects.get(
                 username=request.POST['username'],
                 password=request.POST['password'])
             return render(request,'index.html',{'members':members})
        else:
             return render(request,'login.html')
    else:
        return render(request,'login.html')





def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def department(request):
    return render(request, 'department.html')


def contact(request):
    if request.method == 'POST':
        all = Contact(name=request.POST['name'],
                      email=request.POST['email'],
                      phone=request.POST['phone'],
                      message=request.POST['message']
                      )
        all.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def Appoint(request):
    if request.method == 'POST':
        myappointments = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointments.save()
        return redirect('/show')

    else:
        return render(request, 'appointment.html')


def show(request):
    information = Appointment.objects.all()
    return render(request, 'show.html', {'data': information})


def delete(request, id):
    myappointment = Appointment.objects.get(id=id)
    myappointment.delete()
    return redirect('/show')


def edit(request, id):
    appointment = Appointment.objects.get(id=id)
    return render(request, 'edit.html', {'x': appointment})


def update(request, id):
    if request.method == 'POST':
        appointment = Appointment.objects.get(id=id)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
            return render(request, 'edit.html')
    else:
        return render(request, 'edit.html')

def register(request):
    if request.method=='POST':
        members= Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request,'register.html')

def login(request):
    return render(request,'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

