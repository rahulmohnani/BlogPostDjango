from django.urls import path
# from . import views

from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView,\
DeletePostView, AddCategoryView, category_view, like_view, search, comment_post

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', category_view, name='category'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('search', search, name='search'),
    path('comment/<int:pid>', comment_post, name='comment'),
]
