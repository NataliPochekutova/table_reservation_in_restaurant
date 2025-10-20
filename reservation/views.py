from datetime import date, datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_GET
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ReservationForm
from .models import Reservation, Table
from .services import get_free_tables


class ReservationCreate(LoginRequiredMixin, CreateView):
    """Контроллер нового бронирования столика"""

    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/reservation_form.html"
    success_url = reverse_lazy("reservation:personal_account")

    def form_valid(self, form):
        reservation = form.save()
        user = self.request.user
        reservation.customer = user
        reservation.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        context["all_tables"] = Table.objects.all()
        return context


@require_GET
def get_available_tables(request):
    """AJAX-функция для получения доступных столиков"""
    date_str = request.GET.get("date_reservation")
    time_str = request.GET.get("time_reservation")

    if not date_str or not time_str:
        return JsonResponse({"error": "Не указана дата или время"}, status=400)
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        time = datetime.strptime(time_str, "%H:%M").time()
        available_tables = get_free_tables(date, time)
        tables_data = [
            {
                "id": table.id,
                "number": table.table_number,
                "capacity": table.table_capacity,
                "location": table.location or "",
            }
            for table in available_tables
        ]

        return JsonResponse({"tables": tables_data})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


class ReservationDetail(LoginRequiredMixin, DetailView):
    """Контроллер просмотра бронирования столика"""
    model = Reservation
    template_name = "reservation/reservation_detail.html"


class ReservationList(LoginRequiredMixin, ListView):
    """Контроллер просмотра всех бронирований"""
    model = Reservation
    template_name = "reservation/reservation_list.html"
    context_object_name = "reservations"
    ordering = ["-date_reservation", "-time_reservation"]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.groups.filter(name="Администратор").exists():
            return queryset
        else:
            return queryset.filter(customer=user)


class ReservationDelete(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления бронирования"""
    model = Reservation
    template_name = "reservation/reservation_delete.html"
    success_url = reverse_lazy("reservation:reservation_list")


class ReservationUpdate(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования бронирования"""
    model = Reservation
    form_class = ReservationForm
    template_name = "reservation/reservation_form.html"

    def get_success_url(self):
        return reverse("reservation:reservation_detail", args=[self.object.pk])

    def get_context_data(self, **kwargs):
        """Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        context["all_tables"] = Table.objects.all()
        context["today_date"] = date.today().isoformat()
        return context


class PersonalAccountViews(LoginRequiredMixin, TemplateView):
    """Контроллер для отображения личного кабинета пользователя"""

    model = Reservation
    template_name = "reservation/personal_account.html"

    def get_context_data(self, **kwargs):
        """Отправка формы в шаблон"""
        context = super().get_context_data(**kwargs)
        now = timezone.now().date()

        all_reservations = Reservation.objects.filter(customer=self.request.user)
        context["bookings_history"] = all_reservations.filter(
            date_reservation__lt=now
        ).order_by("-date_reservation")
        context["current_bookings"] = all_reservations.filter(
            date_reservation__gte=now
        ).order_by("date_reservation")

        return context
