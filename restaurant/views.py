from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from restaurant.forms import EmployeeForm, RestaurantForm, TableForm
from restaurant.models import Employee, Restaurant, Table


class HomeViews(TemplateView):
    """Контроллер для отображения главной страница сайта"""

    model = Restaurant
    template_name = "restaurant/home.html"
    success_url = reverse_lazy("restaurant:home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["restaurant"] = Restaurant.objects.get(id=1)
        return context


class AboutRestaurantViews(TemplateView):
    """Контроллер для отображения страницы о ресторане"""

    model = Restaurant
    template_name = "restaurant/restaurant.html"

    def get_context_data(self, **kwargs):
        """Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        context["restaurant"] = Restaurant.objects.get(id=1)
        context["employees"] = Employee.objects.all()
        return context


class ServicesViews(TemplateView):
    """Контроллер для отображения страницы услуги"""

    model = Restaurant
    template_name = "restaurant/services.html"


class ContactsViews(TemplateView):
    """Контроллер для отображения страницы контакты"""

    model = Restaurant
    template_name = "restaurant/contacts.html"


class FeedbackViews(TemplateView):
    """Контроллер для отображения страницы обратной связи"""

    model = Restaurant
    template_name = "restaurant/feedback.html"


def feedback_submit(request):
    """Отправка письма обратной связи"""
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Обратная связь от {name}"
        message_body = f"Имя: {name}\nEmail: {email}\n\nСообщение:\n{message}"
        recipient_list = [settings.EMAIL_HOST_USER]

        try:
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                recipient_list,
                fail_silently=False,
            )
            messages.success(request, "Ваш отзыв отправлен. Спасибо!")
        except Exception as e:
            messages.error(request, "Ошибка при отправке письма. Попробуйте позже.")

        return redirect("restaurant:feedback")
    else:
        return redirect("restaurant:feedback")


class SiteManagementViews(TemplateView):
    """Контроллер для отображения страниц редактирования сайта"""

    model = Restaurant
    template_name = "restaurant/site_management.html"

    def get_context_data(self, **kwargs):
        """Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        context["restaurant"] = Restaurant.objects.get(id=1)
        context["employees"] = Employee.objects.all()
        context["table"] = Table.objects.all()
        return context


class RestaurantUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Контроллер изменения информации о ресторане"""

    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurant/restaurant_form.html"
    success_url = reverse_lazy("restaurant:home")
    permission_required = "restaurant.change_restaurant"


class EmployeeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Контроллер детализации сотрудника"""

    model = Employee
    template_name = "employee/employee_detail.html"
    context_object_name = "employee"
    permission_required = "restaurant.view_employee"


class EmployeeList(ListView):
    """Контроллер вывода списка сотрудников"""

    model = Employee
    template_name = "employee/employee_list.html"
    context_object_name = "employees"


class EmployeeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Контроллер создания нового сотрудника"""

    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("restaurant:employee_list")
    permission_required = "restaurant.add_employee"


class EmployeeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер удаления сотрудников"""

    model = Employee
    template_name = "employee/employee_delete.html"
    success_url = reverse_lazy("restaurant:employee_list")
    context_object_name = "employee"
    permission_required = "restaurant.delete_employee"


class EmployeeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Контроллер изменения сотрудников"""

    model = Employee
    form_class = EmployeeForm
    template_name = "employee/employee_form.html"
    success_url = reverse_lazy("restaurant:employee_list")
    permission_required = "restaurant.change_employee"


class TableDetail(LoginRequiredMixin, DetailView):
    """Контроллер детализации стола"""

    model = Table
    template_name = "table/table_detail.html"
    context_object_name = "table"


class TableList(ListView):
    """Контроллер вывода списка столов"""

    model = Table
    template_name = "table/table_list.html"
    context_object_name = "tables"


class TableCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Контроллер создания нового стола"""

    model = Table
    form_class = TableForm
    template_name = "table/table_form.html"
    success_url = reverse_lazy("restaurant:table_list")
    permission_required = "restaurant.add_table"


class TableDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Контроллер удаления стола"""

    model = Table
    template_name = "table/table_delete.html"
    success_url = reverse_lazy("restaurant:table_list")
    context_object_name = "table"
    permission_required = "restaurant.delete_table"


class TableUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Контроллер изменения стола"""

    model = Table
    form_class = TableForm
    template_name = "table/table_form.html"
    success_url = reverse_lazy("restaurant:table_list")
    permission_required = "restaurant.change_table"
