from django.urls import path

from webapp.views.base import home_view
from webapp.views.information import cat_view

urlpatterns = [
    path('', home_view),
    path('information/', cat_view)
]
