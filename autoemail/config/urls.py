
from django.contrib import admin
from django.urls import path
from account.views import add_accounts_view, cafe_search_view, cafe_list_view, account_list_view, email_send_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cafe_search_view , name='cafe-search'),
    path('list', cafe_list_view, name='cafe-list'),
    path('list/send', email_send_view, name='email-send'),
    path('list/<int:pk>', account_list_view, name='account-list'),
    path('crawl/', add_accounts_view , name='add-accounts'),
]
