from ..models import RunwayStatus
from django.utils import timezone

def save_runways_to_db(runways, timestamp=None):
    if timestamp is None:
        timestamp = timezone.now()
    for runway in runways:
        RunwayStatus.objects.create(
            datetimestamp=timestamp,
            runway_name=runway['name'],
            status=runway['activity']
        )