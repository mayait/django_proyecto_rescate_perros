from django.urls import path
from extra_pages import views
urlpatterns = [
    path('starterpage',views.StarterPageView.as_view(),name='extra_pages-starterpage'),
    path('404error',views.ErrorView.as_view(),name='extra_pages-404error'),
    path('500error',views.ErrorsView.as_view(),name='extra_pages-500error'),
    path('maintenance',views.MaintenanceView.as_view(),name='extra_pages-maintenance'),
    path('comingsoon',views.ComingSoonView.as_view(),name='extra_pages-comingsoon')
]