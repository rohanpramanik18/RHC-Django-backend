from django.urls import path
from .import apis, views


urlpatterns = [
      path("register/", apis.RegisterApi.as_view(), name="register"),
      path("login/", apis.LoginApi.as_view(), name="login"),
      path("self/", apis.UserApi.as_view(), name="self"),
      path("logout/", apis.LogoutApi.as_view(), name="logout"),
      path("create/", views.add_users, name="add_users"),
      path('all/', views.view_users, name='view_users'),
      path('update/<int:pk>/', views.update_users, name='update_users'),
      path('user/<int:user_id>/delete', views.delete_users, name='delete_users'),
      
#     path('home/', views.home, name="home"),
#     path('login/', views.loginPage, name="login"),
#     path('logout/', views.logoutUser, name="logout"),
#     path('register/', views.registerPage, name="register"),
#     path('adminpage/', views.adminPage, name="adminpage"),
      
      path("asha_register/", apis.AshaRegisterApi.as_view(), name="asharegister"),
      path("asha_login/", apis.AshaLoginApi.as_view(), name="ashalogin"),
      path("asha_details/", apis.AshaUserApi.as_view(), name="ashaself"),
      path("asha_logout/", apis.AshaLogoutApi.as_view(), name="ashalogout"),
      path("asha_create/", views.add_ashausers, name="add_ashausers"),
      path('asha_all/', views.view_ashausers, name='view_ashausers'),
      path('asha_update/<int:pk>/', views.update_ashausers, name='update_ashausers'),
      path('asha_user/<int:asha_id>/delete', views.delete_ashausers, name='delete_ashausers'),
      
      
      path("patient_register/", apis.PatientRegisterApi.as_view(), name="patientregister"),
      path("patient_login/", apis.PatientLoginApi.as_view(), name="patientlogin"),
      path("patient_details/", apis.PatientUserApi.as_view(), name="patientself"),
      path("patient_logout/", apis.PatientLogoutApi.as_view(), name="patientlogout"),
      path("patient_create/", views.add_patients, name="add_patients"),
      #path('patient_all/', views.view_patients, name='view_patients'),
      path('patient_update/<int:pk>/', views.update_patients, name='update_patients'),
      path('patient_user/<int:patient_id>/delete', views.delete_patients, name='delete_patients'),
      
]
