from django.shortcuts import render
from .models import Twitt
from .forms import TwittForm , UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

# Create your views here.



@login_required
def twitt_list(request):
    twitts = Twitt.objects.all().order_by('-created_at')
    for twitt in twitts:
        if not twitt.photo:
            twitt.photo = 'path/to/default-image.jpg'
    return render(request , 'twitt_list.html' , {'twitts' : twitts})

@login_required
def twitt_create(request):
    if request.method == "POST":
        form = TwittForm(request.POST , request.FILES)
        if form.is_valid():
            twitt = form.save(commit=False)
            twitt.user = request.user
            twitt.save()
            return redirect('twitt_list')
    else:
        form = TwittForm()
    return render(request , 'twitt_form.html' , {'form' : form})

@login_required
def twitt_edit(request , twitt_id):
    twitt = get_object_or_404(Twitt , pk = twitt_id , user = request.user)
    if request.method == "POST":
        form = TwittForm(request.POST , request.FILES , instance=twitt)
        if form.is_valid():
            twitt = form.save(commit=False)
            twitt.user = request.user
            twitt.save()
            return redirect('twitt_list')
    else:
        form = TwittForm(instance=twitt)
    return render(request , 'twitt_form.html' , {'form' : form})

@login_required
def twitt_delete(request , twitt_id):
    twitt = get_object_or_404(Twitt , pk = twitt_id ,user = request.user)
    if request.method == "POST":
        twitt.delete()
        return redirect('twitt_list')
    return render(request , 'twitt_confirm_delete.html' , {'twitt' : twitt})



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('twitt_list')
    else:
        form = UserRegistrationForm()
    return render(request , 'registration/register.html' , {'form' : form})


                