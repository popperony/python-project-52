from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('set_language/<str:language>/', views.set_language, name='set_language'),
    path('', views.IndexView.as_view(), name='home'),
    path('panel/', admin.site.urls),
]

handler404 = views.Error404View.as_view()
handler500 = views.Error500View.as_view()
