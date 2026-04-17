from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def user_register(request):
    template='registration/signup.html'
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request,template,{
                     'form':form,
                     'error_message':'Username already existed'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request,template,{
                     'form':form,
                     'error_message':'email already existed'
                })
            elif form.cleaned_data['password']!=form.cleaned_data['password_repeat']:
                return render(request,template,{
                    'form':form,
                    'error_message':'passwords is not to match.'
                })
            else:
                user=User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )    
                user.save()
                return HttpResponseRedirect('login')
    else:
        form=RegisterForm()    
           
    return render(request,template,{'form': form})
