from django.conf.urls import url
from school import views
from django.urls import path
from .views import (
	CounterCreateView, 
	CounterUpdateView, 
	CounterDeleteView, 
	CounterDetailView, 
	CounterListView )


urlpatterns=[
    path('create/count/', CounterCreateView.as_view(), name='create-count'),
    path('update/count/<pk>/)', CounterUpdateView.as_view(), name='update-count'),
    path('delete/count/<pk>/)', CounterDeleteView.as_view(), name='delete-count'),
    path('detail/count/<pk>/)', CounterDetailView.as_view(), name='detail-count'),
    path('list/count/', CounterListView.as_view(), name='list-count'),

]