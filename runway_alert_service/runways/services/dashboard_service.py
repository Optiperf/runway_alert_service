from ..models import RunwayStatus

def get_dashboard_rows():
    timestamps = (
        RunwayStatus.objects
        .order_by('-datetimestamp')
        .values_list('datetimestamp', flat=True)
        .distinct()
    )[:10]

    runway_names = [
        "Aalsmeerbaan", "Oostbaan", "Kaagbaan",
        "Buitenveldertbaan", "Polderbaan", "Zwanenburgbaan"
    ]
    dashboard_rows = []
    for ts in timestamps:
        row = {'timestamp': ts}
        statuses = RunwayStatus.objects.filter(datetimestamp=ts)
        for runway in runway_names:
            status_obj = statuses.filter(runway_name__iexact=runway).first()
            row[runway] = status_obj.status if status_obj else ''
        dashboard_rows.append(row)
    return dashboard_rows, runway_names