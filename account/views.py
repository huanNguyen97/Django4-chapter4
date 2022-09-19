import profile
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (
  LoginForm,
  UserRegistrationForm,
  UserEditForm,
  ProfileEditForm
)
from .models import Profile


# Create your views here.
@login_required
def edit(request):
  if request.method == 'POST':
    user_form = UserEditForm(
      instance=request.user,
      data=request.POST,
    )
    profile_form = ProfileEditForm(
      instance=request.user.profile,
      data=request.POST,
      files=request.FILES
    )

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(
        request=request,
        message='Profile updated successfully.'
      )
    else:
      messages.error(
        request=request,
        message='Error updating your profile.'
      )
  else:
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)

  return render(
    request=request,
    template_name='account/edit.html',
    context={'user_form': user_form, 'profile_form': profile_form}
  )


@login_required
def dashboard(request):
  return render(
    request=request,
    template_name='account/dashboard.html',
    context={'section': 'dashboard'}
  )


def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(
        request=request,
        username=cd['username'],
        password=cd['password']
      )

    if user is not None:
      if user.is_active:
        login(request=request, user=user)
        return HttpResponse('Authenticated successfully')
      else:
        return HttpResponse('Disable account')
    else:
      return HttpResponse('Invalid login')
  else:
    form = LoginForm()

  return render(
    request=request,
    template_name='account/login.html',
    context={'form': form}
  )


def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)

    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(
        user_form.cleaned_data['password']
      )
      new_user.save()

      Profile.objects.create(user=new_user)

      return render(
        request=request,
        template_name='account/register_done.html',
        context={'new_user': new_user}
      )
  else:
    user_form = UserRegistrationForm()

  return render(
    request=request,
    template_name='account/register.html',
    context={'user_form': user_form}
  )
