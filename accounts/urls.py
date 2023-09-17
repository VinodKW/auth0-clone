from django.urls import path, re_path, include
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import LoginView, LogoutView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('registration/', RegisterView.as_view(), name='account_signup'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
        name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email'),
]