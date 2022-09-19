from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
  # Dashboard view
  path('', views.dashboard, name='dashboard'),
  path('', include('django.contrib.auth.urls')),
  path('register/', views.register, name='register'),
  path('edit/', views.edit, name='edit'),

  # # Login, Logout
  # path('login/', auth_views.LoginView.as_view(), name='login'),
  # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

  # # Change password url
  # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
  # path('password-change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

  # # Reset password
  # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  # path('password-reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  # path('password-reset/complete', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_complete'),
]

