from django.urls import path
from django.views.generic import DetailView, ListView, UpdateView
from phonereviewsapp.models import Phone, Store
from phonereviewsapp.views import PhoneCreate, StoreCreate, PhoneDetail, review_create, review_delete
from phonereviewsapp.views import StoreEdit, PhoneEdit, phone_delete, store_delete


app_name = 'phonereviewsapp'
urlpatterns = [

    path('',
         ListView.as_view(queryset=Phone.objects.values,
                          context_object_name='phone_list',
                          template_name='phonereviewsapp/phone_list.html'),
         name='phone_list'),

    path('phonereviews/<pk>',
         PhoneDetail.as_view(),
         name='phone_detail'),

    path('phonereviews/<pkr>/stores/<pk>',
         DetailView.as_view(model=Store,
                            template_name='phonereviewsapp/store_detail.html'),
         name='store_detail'),

    path('phonereviews/create/',
         PhoneCreate.as_view(success_url="/phonereviews/"),
         name='phone_create'),

    path('phonereviews/<pk>/edit/',
         PhoneEdit.as_view(),
         name='phone_edit'),

    path('phonereviews/<pk>/store/create/',
         StoreCreate.as_view(),
         name='store_create'),

    path('phonereviews/<pkr>/store/<pk>/edit/',
         StoreEdit.as_view(),
         name='store_edit'),

    path('phonereviews/deletestore/<pk>',
         store_delete,
         name='delete_store'),

    path('phonereviews/deletephone/<pk>',
         phone_delete,
         name='delete_phone'),

    path('phonereviews/<pk>/reviews/create/',
         review_create,
         name='review_create'),

    path('phonereviews/<pk>/reviews/delete/',
         review_delete,
         name='review_delete'),


]

