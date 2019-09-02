from django.conf.urls import url
from views import month_wise_view, current_year_wise_active_account_record, account_state_category_wise

urlpatterns = [
    url(r'^current_year_view/$', current_year_wise_active_account_record),
    url(r'^category_study/$', account_state_category_wise),
    url(r'^monthly_view/$',month_wise_view)
    ]
