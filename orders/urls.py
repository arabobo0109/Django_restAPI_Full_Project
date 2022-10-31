from django.urls import path
from . import views

urlpatterns = [
    # path('',views.HelloOrdersView.as_view(),name='hello_auth'),
    path('', views.OrderCreateListView.as_view(),name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(),name='order_details'),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(),name= 'update_order_status'),
    path('user/<int:user_id>/orders/',views.UserOrderView.as_view(),name='users_orders'),
    path('user/<int:user_id>/order/<int:order_id>',views.UserOrderView.as_view(),name='user_specific_detail'),

]