from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('category/<int:pk>/', views.CategoryViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}
    )),
    path('item/', views.ItemViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('item/<int:pk>/', views.ItemViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}
    )),
    path('category/<int:category_id>/item', views.ItemListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:item_id>/order/', views.OrderListCreateAPIView.as_view()),
    path('category/<int:category_id>/item/<int:item_id>/order/<int:order_id>/'),
        views.OrderRetrieveUpdateDestroyAPIView.as_view())
]