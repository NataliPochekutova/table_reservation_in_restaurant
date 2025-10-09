from django.core.validators import MaxValueValidator
from django.db import models

from restaurant.models import Table
from users.models import User


class Reservation(models.Model):
    """Модель Бронирование столиков"""

    date_reservation = models.DateField(
        verbose_name="Дата бронирования столика",
        help_text="Выберите число, на которое хотите забронировать столик",
    )
    time_reservation = models.TimeField(
        verbose_name="Время бронирования столика",
        help_text="Выберите время, на которое хотите забронировать столик",
    )
    count_people = models.PositiveIntegerField(
        default=2,
        verbose_name="Количество человек",
        help_text="Введите количество человек",
        validators=[MaxValueValidator(20)],
    )
    customer = models.ForeignKey(
        User,
        verbose_name="Заказчик брони",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reservations_customer",
    )
    table = models.ForeignKey(
        Table,
        verbose_name="Номер стола",
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    wishes = models.TextField(
        verbose_name="Особые пожелания",
        blank=True,
        null=True,
        help_text="Напишите Ваши пожелания",
    )

    def __str__(self):
        return (
            f"Заказчик {self.customer} забронировал столик {self.table}"
            f" на {self.date_reservation} {self.time_reservation}"
        )

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
