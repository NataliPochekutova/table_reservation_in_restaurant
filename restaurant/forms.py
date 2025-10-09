from django import forms

from restaurant.models import Employee, Restaurant, Table
from users.forms import StyleFormMixin


class TableForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования столиков"""

    class Meta:
        model = Table
        fields = "__all__"


class EmployeeForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования сотрудников"""

    class Meta:
        model = Employee
        fields = "__all__"


class RestaurantForm(StyleFormMixin, forms.ModelForm):
    """Форма для создания и редактирования ресторана"""

    class Meta:
        model = Restaurant
        fields = "__all__"
