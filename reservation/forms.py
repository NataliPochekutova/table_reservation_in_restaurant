from django import forms

from reservation.models import Reservation
from users.forms import StyleFormMixin

class ReservationForm(StyleFormMixin, forms.ModelForm):
    """Форма для бронирования столиков"""

    class Meta:
        model = Reservation
        exclude = ("customer",)