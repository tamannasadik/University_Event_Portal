from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # homepage with upcoming events
    path('events/', views.event_list, name='events'),  # list all events
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # event detail page
]
