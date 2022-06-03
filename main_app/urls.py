from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('collections/', views.collections.as_view(), name = "collections"),
    path('collections/new/', views.AddChibi.as_view(), name="chibi_add"),
    path('collections/<int:pk>/', views.ChibiDetail.as_view(), name = "chibi_detail"),
    path('collections/<int:pk>/update', views.ChibiUpdate.as_view(), name="chibi_update"),
    path('collections/<int:pk>/delete', views.ChibiDelete.as_view(), name = "chibi_delete")
]