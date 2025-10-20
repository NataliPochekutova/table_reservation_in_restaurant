from datetime import datetime, timedelta

from reservation.models import Reservation
from restaurant.models import Table


def get_free_tables(
    date_reservation, time_reservation, requested_duration_hours=2, min_capacity=1
):
    """Выборка свободных столиков"""
    requested_start = datetime.combine(date_reservation, time_reservation)
    requested_end = requested_start + timedelta(hours=requested_duration_hours)

    reservations = Reservation.objects.filter(date_reservation=date_reservation)

    occupied_table_ids = set()

    for reservation in reservations:
        res_start = datetime.combine(
            reservation.date_reservation, reservation.time_reservation
        )
        res_end = res_start + timedelta(hours=reservation.long_reservation)

        # Проверка пересечения интервалов
        if (requested_start < res_end) and (res_start < requested_end):
            occupied_table_ids.add(reservation.table.id)

    # Возвращаем все столики, кроме занятых
    available_tables = Table.objects.exclude(id__in=occupied_table_ids).filter(
        table_capacity__gte=min_capacity
    )
    return available_tables
