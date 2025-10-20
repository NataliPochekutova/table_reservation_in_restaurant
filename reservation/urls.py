from django.urls import path

from reservation.apps import ReservationConfig
from reservation.views import (PersonalAccountViews, ReservationCreate,
                               ReservationDelete, ReservationDetail,
                               ReservationList, ReservationUpdate,
                               get_available_tables)

app_name = ReservationConfig.name

urlpatterns = [
    path("reservation/", ReservationList.as_view(), name="reservation_list"),
    path("reservation/create/", ReservationCreate.as_view(), name="reservation_form"),
    path(
        "reservation/<int:pk>/", ReservationDetail.as_view(), name="reservation_detail"
    ),
    path(
        "reservation/<int:pk>/update/",
        ReservationUpdate.as_view(),
        name="reservation_update",
    ),
    path(
        "reservation/<int:pk>/delete/",
        ReservationDelete.as_view(),
        name="reservation_delete",
    ),
    path(
        "reservation/personal_account",
        PersonalAccountViews.as_view(),
        name="personal_account",
    ),
    path("get-available-tables/", get_available_tables, name="get_available_tables"),
]
