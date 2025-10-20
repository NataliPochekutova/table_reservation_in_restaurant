from datetime import date, time

from django import forms
from django.core.exceptions import ValidationError

from reservation.models import Reservation
from users.forms import StyleFormMixin


class ReservationForm(StyleFormMixin, forms.ModelForm):
    """Форма для бронирования столиков"""

    class Meta:
        model = Reservation
        exclude = ("customer",)

    def clean_date_reservation(self):
        """Валидация даты бронирования"""
        date_reserved = self.cleaned_data.get("date_reservation")
        today = date.today()

        if date_reserved < today:
            raise ValidationError(
                "Дата бронирования не может быть раньше сегодняшнего дня"
            )

        return date_reserved

    def clean_time_reservation(self):
        """Валидация времени бронирования"""
        time_reserved = self.cleaned_data.get("time_reservation")
        if time_reserved is None:
            return time_reserved

        if time_reserved < time(9, 0) or time_reserved > time(23, 0):
            raise ValidationError(
                "Время бронирования должно быть в диапазоне с 09:00 до 23:00"
            )

        return time_reserved
