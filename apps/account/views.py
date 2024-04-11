from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.views import APIView


from apps.account.models import User
from apps.market.models import Item



class ProfileView(APIView):

    def get(self, request):
        user = request.user.id
        context = {'profile': User.objects.filter(id=user),
                   'items': Item.objects.filter(owner=user)}
        return render(request, 'profile.html', context)






