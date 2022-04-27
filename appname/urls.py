from django.urls import path
from appname import views

app_name = 'appname'

urlpatterns = [
    path('points/', views.postPoint, name="postPoint"),
    path('delete_post/', views.delete_point, name='delete_post'),
    path('update_points/', views.update_points, name='update_points'),
    # path('record/', views.print_pdf, name='record'),
    ]