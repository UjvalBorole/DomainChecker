from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,passwordchange,setpasswordconfirm
from .forms import PasswordReset


urlpatterns = [
    path('home/',views.home ,name="home"),
    path('profile/',views.profile ,name="profile"),
    path('vdata/',views.valid_data ,name="vdata"),
    path('Ivdata/',views.Invalid_data ,name="Indata"),
     path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='auth/changepassword.html',form_class=passwordchange,success_url='/changepassworddone/'), name='changepassword'),
    path('changepassworddone/', auth_view.PasswordChangeDoneView.as_view(template_name='auth/changepassworddone.html'), name='changepassworddone'),
    # path('changepass/',views.changepass,name='changepassword'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='auth/password_reset.html',form_class=PasswordReset),name='passwordreset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html',form_class=setpasswordconfirm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),name='password_reset_complete'),

    
    path('', auth_view.LoginView.as_view(template_name='auth/login.html',authentication_form=LoginForm), name='login'),
    path('logout/',views.custom_logout ,name='logout'),

    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
]
