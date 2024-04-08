from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from apps.account.forms import UserLoginForm
from django.contrib import auth


class LoginView(APIView):


    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        print(request.user)
        conext = {'form': form}
        return render(request, 'login.html', conext)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print('pltcm')
            if user and user.is_active :
                print(user)
                auth.login(request, user)
                return HttpResponseRedirect(reverse('market:index'))
        else:
            form = UserLoginForm()
            #print(request.POST['username'])
        context = {'form': form}

        return render(request, 'login.html', context)


