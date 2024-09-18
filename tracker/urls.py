from django.urls import path

from tracker import views

urlpatterns = [
    path('track/', views.track_email_open, name='track_email_open'),
    path('tracking/', views.get_tracking_data, name='get_tracking_data'),
]