from django.shortcuts import render
from .models import RunwayStatus
from datetime import datetime
from django.utils import timezone
from django.db.models import F
from .services.scraping_service import scrape_runway_status
from .services.email_service import send_email
from .services.dashboard_service import get_dashboard_rows
from .services.runway_db_service import save_runways_to_db

def index(request):
    return render(request, 'runways/index.html')

def scrape_and_display(request):
    runways = scrape_runway_status()
    send_email(runways, request)
    save_runways_to_db(runways)
    context = {'runways': runways}
    return render(request, 'runways/scrape_results.html', context)

def live_dashboard(request):
    dashboard_rows, runway_names = get_dashboard_rows()
    context = {
        'dashboard_rows': dashboard_rows,
        'runway_names': runway_names,
    }
    return render(request, 'runways/live_dashboard.html', context)

def runway_alert_setup(request):
    return render(request, 'runways/runway_alert_setup/index.html')