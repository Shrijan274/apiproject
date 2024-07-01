from django.urls import path
from app import views

urlpatterns = [
    path('api/signup/', views.signup, name='signup'),
    path('api/login/', views.login_view, name='login'),
    path('api/logout/', views.logout_view, name='logout'),
]


#http://127.0.0.1:8000/api/signup/
#{
#   "email":"demo@gmail.com",
#   "username":"demo",
#   "first_name":"abc",
#   "last_name":"def",
#   "password":"demo"
#}


# http://127.0.0.1:8000/api/login/
# {
#     "email":"demo@gmail.com",
#     "password":"demo"
# }