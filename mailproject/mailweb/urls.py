from django.urls import path,re_path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/',views.detail, name='detail'),
    re_path(r'^detail/(?P<year>[0-9]{4})/$',views.detail_year),
    path('detail/<int:year>/<int:month>/',views.detail_month, name='dym')
]

