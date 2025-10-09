from django.db import models


class Table(models.Model):
    """Модель Стол для бронирования"""

    GENERAL_HALL = "general hall"
    VIP_HALL = "VIP hall"
    TERRACE = "terrace"

    TABLE_LOCATION = [
        (GENERAL_HALL, "Общий зал"),
        (VIP_HALL, "VIP зал"),
        (TERRACE, "Терраса"),
    ]

    table_number = models.PositiveIntegerField(
        unique=True, verbose_name="Номер стола", help_text="Укажите номер стола"
    )
    table_capacity = models.PositiveIntegerField(
        verbose_name="Вместительность стола",
        default=1,
        help_text="Укажите сколько максимум человек может поместиться за столом",
    )
    location = models.CharField(
        max_length=50,
        choices=TABLE_LOCATION,
        default=GENERAL_HALL,
        verbose_name="Расположение стола",
        help_text="Укажите расположение стола",
    )

    def __str__(self):
        return f"{self.table_number} - вместительность {self.table_capacity} человек"

    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"


class Restaurant(models.Model):
    """Модель ресторан"""

    name = models.CharField(max_length=200, verbose_name="Название ресторана")
    logo = models.ImageField(
        upload_to="photos/",
        verbose_name="Логотип ресторана",
        blank=True,
        null=True,
    )
    story = models.TextField(verbose_name="История ресторана", null=True, blank=True)
    mission = models.TextField(verbose_name="Миссия", null=True, blank=True)
    description = models.TextField(
        verbose_name="Описание ресторана", null=True, blank=True
    )

    class Meta:
        verbose_name = "ресторан"
        verbose_name_plural = "рестораны"


class Employee(models.Model):
    """Модель сотрудники ресторана"""

    first_name = models.CharField(max_length=200, verbose_name="Имя сотрудника")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия сотрудника")
    photo_employee = models.ImageField(
        upload_to="photos/", verbose_name="Фото сотрудника"
    )
    job_title = models.CharField(max_length=200, verbose_name="Должность")
    description = models.TextField(
        verbose_name="Комментарии о сотруднике", null=True, blank=True
    )

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"
