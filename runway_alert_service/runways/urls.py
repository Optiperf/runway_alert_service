from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scrape/', views.scrape_and_display, name='scrape_and_display'),
    path('dashboard/', views.live_dashboard, name='live_dashboard'),
    path('runway-alert-setup/', views.runway_alert_setup, name='runway_alert_setup'),
]