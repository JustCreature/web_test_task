from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SiteListView, SiteAddView, SiteDetailView

app_name = 'api_v1'
urlpatterns = [

    path('sites', SiteListView.as_view()),
    path('sites/<int:pk>/', SiteDetailView.as_view()),
    path('sites/add/', SiteAddView.as_view()),
]