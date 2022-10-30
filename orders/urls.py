from django.urls import path
from . import views

urlpatterns = [
    # path('',views.HelloOrdersView.as_view(),name='hello_auth'),
    path('', views.OrderCreateListView.as_view(),name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(),name='order_details')

]