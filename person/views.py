from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth import login, logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from basket.models import Basket


def create_user(request):
    telephone = request.POST.get('telephone')
    emailu = request.POST.get('email')
    passwordu = request.POST.get('password')
    user = User.objects.create_user(username=telephone,
                                    email=emailu)
    user.set_password(passwordu)
    user.is_staff = False
    user.is_superuser = False
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.save()
    current_user = user
    this_basket = Basket.objects.create(owner=current_user)
    this_basket.save()
    return HttpResponseRedirect(reverse('Products:index'))


def newUser(request):
    c = RequestContext(request, {})
    return render_to_response('signup.html', c)


@csrf_protect
def authentication(request):
        checktel = request.POST.get("telephone")
        checkpass = request.POST.get("password")
        user = auth.authenticate(username=checktel, password=checkpass)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('Products:index'))
        else:
            return HttpResponse("Not Lol")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Products:index'))
