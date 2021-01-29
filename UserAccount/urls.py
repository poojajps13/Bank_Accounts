from django.urls import path
from .views import FetchUserData

urlpatterns = [
    path('fetch_data/', FetchUserData.as_view(),  name='fetch-data'),
]