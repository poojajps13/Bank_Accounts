from django.urls import path
from .views import FetchUserData, ViewUserData

urlpatterns = [
    path('fetch_data/', FetchUserData.as_view(),  name='fetch-data'),
    path('view_data/', ViewUserData.as_view(), name='view-data'),
]