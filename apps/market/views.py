from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView

from apps.account.models import User
from apps.market.models import Category, Item


# Create your views here.

class IndexView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        context = {
            'items': Item.objects.all()

        }
        return render(request, 'index.html', context)

class LikedView(APIView):



    def post(self, request, item_pk):
        current_page = request.META.get('HTTP_REFERER')
        user = User.objects.get(id=request.user.id)  # Получаем конкретного пользователя
        print(user)
        item = Item.objects.get(id=item_pk)
        item.liked_by.add(user)

        return redirect(current_page)





