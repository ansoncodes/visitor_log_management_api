from django.urls import path
from .views import check_in, check_out, visitors_inside, visitors_by_date

urlpatterns = [
    path('check-in/', check_in),
    path('check-out/', check_out),
    path('inside/', visitors_inside),
    path('by-date/', visitors_by_date),
]
