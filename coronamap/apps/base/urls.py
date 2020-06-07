from django.conf.urls import url
from django.urls import path
from .views import HomepageView, NewCasesView


urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='homepage'),
    path('new_cases/<str:date>',
         NewCasesView.as_view(),
         kwargs={'field': 'new_cases'}),
    path('new_deaths/<str:date>',
         NewCasesView.as_view(),
         kwargs={'field': 'new_deaths'}),
]
