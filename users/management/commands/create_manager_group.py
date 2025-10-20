from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from restaurant.models import Employee, Restaurant, Table
from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания группы Менеджер управления данными ресторана, столами, сотрудниками"""

    def handle(self, *args, **kwargs):
        group_name = "Менеджер"
        group, created = Group.objects.get_or_create(name=group_name)

        permissions_list = []

        ct_restaurant = ContentType.objects.get_for_model(Restaurant)
        for perm_code in ["change", "add", "delete"]:
            perm_name = f"{perm_code}_restaurant"
            try:
                perm = Permission.objects.get(
                    codename=perm_name, content_type=ct_restaurant
                )
                permissions_list.append(perm)
            except Permission.DoesNotExist:
                self.stdout.write(f"Права {perm_name} не найдены.")

        # Модель User
        ct_user = ContentType.objects.get_for_model(User)
        for perm_code in ["change", "add", "delete"]:
            perm_name = f"{perm_code}_user"
            try:
                perm = Permission.objects.get(codename=perm_name, content_type=ct_user)
                permissions_list.append(perm)
            except Permission.DoesNotExist:
                self.stdout.write(f"Права {perm_name} не найдены.")

        # Модель Table
        ct_table = ContentType.objects.get_for_model(Table)
        for perm_code in ["change", "add", "delete"]:
            perm_name = f"{perm_code}_table"
            try:
                perm = Permission.objects.get(codename=perm_name, content_type=ct_table)
                permissions_list.append(perm)
            except Permission.DoesNotExist:
                self.stdout.write(f"Права {perm_name} не найдены.")

        # Модель Employee
        ct_employee = ContentType.objects.get_for_model(Employee)
        for perm_code in ["change", "add", "delete"]:
            perm_name = f"{perm_code}_employee"
            try:
                perm = Permission.objects.get(
                    codename=perm_name, content_type=ct_employee
                )
                permissions_list.append(perm)
            except Permission.DoesNotExist:
                self.stdout.write(f"Права {perm_name} не найдены.")

        group.permissions.set(permissions_list)
        group.save()

        self.stdout.write(f'Группа "{group_name}" успешно создана с правами.')
