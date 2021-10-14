from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as userlogin, logout
from django.contrib import messages

from .models import Member
from rental.models import Order
from .user_forms import CustomUserCreationForm
from .decorators import authenticated_user, allowed_users


from .forms import UserProfileUpdateForm

# Create your views here.


def register(request):

    form = CustomUserCreationForm()

    context = {'form': form}

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='member')
            user.groups.add(group)

            Member.objects.create(
                user=user
            )

            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'register.html', context)


def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            userlogin(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or passsword is not correct!")
    return render(request, 'login.html')


@authenticated_user
def logoutUser(request):
    logout(request)
    return redirect('login')


@allowed_users(['member'])
def user_profile(request):

    req_user = request.user
    profile = req_user.member

    orders = req_user.order_set.all()
    order_delivered = req_user.order_set.filter(status='Delivered').count()
    order_count = orders.count()

    context = {'profile': profile, 'orders':  orders,
               'order_count': order_count, 'order_delivered': order_delivered}
    return render(request, 'user_profile.html', context)


def user_profile_edit(request):
    user = request.user

    form = UserProfileUpdateForm(instance=user.member)

    if request.method == 'POST':
        form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=user.member)

        if form.is_valid():
            form.save()
            return redirect('user-profile')
    context = {
        'form': form
    }

    return render(request, 'user_profile_update.html', context)
