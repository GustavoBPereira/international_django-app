from django.urls import path

from international_app.core.views import index

urlpatterns = [
    path('', index, name='index')
]
