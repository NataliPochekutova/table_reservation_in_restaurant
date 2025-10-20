from django.contrib import admin

from restaurant.models import Employee, Restaurant, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели столов"""

    list_display = (
        "id",
        "table_number",
        "table_capacity",
        "location",
    )
    list_filter = (
        "table_capacity",
        "location",
    )
    search_fields = (
        "table_number",
        "table_capacity",
        "location",
    )


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели ресторана"""

    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели сотрудников"""

    list_display = (
        "id",
        "first_name",
        "last_name",
        "job_title",
    )
    list_filter = ("last_name",)
    search_fields = (
        "first_name",
        "last_name",
        "job_title",
    )
