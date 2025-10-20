from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from restaurant import views
from restaurant.apps import RestaurantConfig
from restaurant.views import (AboutRestaurantViews, ContactsViews,
                              EmployeeCreate, EmployeeDelete, EmployeeDetail,
                              EmployeeList, EmployeeUpdate, FeedbackViews,
                              HomeViews, RestaurantUpdate, ServicesViews,
                              SiteManagementViews, TableCreate, TableDelete,
                              TableDetail, TableList, TableUpdate)

app_name = RestaurantConfig.name


urlpatterns = [
    path("home", HomeViews.as_view(), name="home"),
    path("restaurant/", AboutRestaurantViews.as_view(), name="restaurant"),
    path(
        "restaurant/<int:pk>/update/",
        RestaurantUpdate.as_view(),
        name="restaurant_update",
    ),
    path("restaurant/services/", ServicesViews.as_view(), name="services"),
    path("restaurant/contacts/", ContactsViews.as_view(), name="contacts"),
    path("restaurant/feedback/", FeedbackViews.as_view(), name="feedback"),
    path("restaurant/feedback/submit/", views.feedback_submit, name="feedback_submit"),
    path(
        "restaurant/site_management/",
        SiteManagementViews.as_view(),
        name="site_management",
    ),

    path("employee/", EmployeeList.as_view(), name="employee_list"),
    path("employee/<int:pk>/", EmployeeDetail.as_view(), name="employee_detail"),
    path("employee/create/", EmployeeCreate.as_view(), name="employee_create"),
    path("employee/<int:pk>/delete/", EmployeeDelete.as_view(), name="employee_delete"),
    path("employee/<int:pk>/update/", EmployeeUpdate.as_view(), name="employee_update"),

    path("table/", TableList.as_view(), name="table_list"),
    path("table/<int:pk>/", TableDetail.as_view(), name="table_detail"),
    path("table/create/", TableCreate.as_view(), name="table_create"),
    path("table/<int:pk>/delete/", TableDelete.as_view(), name="table_delete"),
    path("table/<int:pk>/update/", TableUpdate.as_view(), name="table_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
