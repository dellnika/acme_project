from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.BirthdayCreateView.as_view(), name='create'),
    # Новый маршрут.
    path('list/', views.BirthdayListView.as_view(), name='list'),  # views.birthday_list
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),  # views.birthday
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),  # views.delete_birthday
    # path('login_only/', views.simple_view),
]
