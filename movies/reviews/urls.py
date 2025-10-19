from django.urls import path
from . import views
from .views import ReviewListCreateAPIView,ReviewDetailAPIView
urlpatterns = [
    path('add/<str:imdb_id>/<str:movie_title>/', views.add_review, name='add_review'),
    path('edit/<int:pk>/', views.edit_review, name='edit_review'),
    path('delete/<int:pk>/', views.delete_review, name='delete_review'),
    path('api/reviews/', ReviewListCreateAPIView.as_view(), name='api-review-list-create'),
    path('api/reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='api-review-detail'),

]
