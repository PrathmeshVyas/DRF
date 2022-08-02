from django.urls import path
from .views import CompanySignupview, CustomerSignupview, CustomAuthToken

urlpatterns = [
    path('signup/company/', CompanySignupview.as_view()),
    path('signup/customer/', CustomerSignupview.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('customer/dashboard', CustomAuthToken.as_view(), name='customer-dashboard'),
    path('company/dashboard', CustomAuthToken.as_view(), name='company-dashboard'),
]
