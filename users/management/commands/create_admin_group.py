from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from reservation.models import Reservation


class Command(BaseCommand):
    """Кастомная команда для создания группы Менеджер для управления бронированиями"""

    def handle(self, *args, **kwargs):
        group_name = "Администратор"
        group, created = Group.objects.get_or_create(name=group_name)

        permissions_list = []

        ct_reservation = ContentType.objects.get_for_model(Reservation)
        for perm_code in ["view", "add", "change", "delete"]:
            perm_name = f"{perm_code}_reservation"
            try:
                perm = Permission.objects.get(
                    codename=perm_name, content_type=ct_reservation
                )
                permissions_list.append(perm)
            except Permission.DoesNotExist:
                self.stdout.write(f"Права {perm_name} не найдены.")

        group.permissions.set(permissions_list)
        group.save()

        self.stdout.write(f'Группа "{group_name}" успешно создана и настроена.')
