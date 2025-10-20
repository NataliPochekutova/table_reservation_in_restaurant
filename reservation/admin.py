from django.contrib import admin

from reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели бронирование"""

    list_display = (
        "id",
        "date_reservation",
        "time_reservation",
        "customer",
        "table",
    )
    list_filter = (
        "date_reservation",
        "customer",
    )
    search_fields = (
        "date_reservation",
        "customer",
        "table",
    )
