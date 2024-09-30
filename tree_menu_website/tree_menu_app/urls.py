from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:menu_item_slug>', views.HomeView.as_view(), name='menu_item_detail'),
]
# Not really named url, but for ease of testing only/not production version
