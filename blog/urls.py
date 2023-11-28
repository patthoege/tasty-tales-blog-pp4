from . import views
from .views import AddPost, SearchResults, Tagged, draft_list, EditDraft, DeleteDraft, about_me, CategoryView
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about_me/', about_me, name='about_me'),
    path('category/', views.CategoryView.as_view(), name='category_list'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('search/', views.SearchResults.as_view(), name='search_results'),
    path('drafts/', draft_list, name='draft_list'),
    path('drafts/edit/<slug:slug>/', EditDraft.as_view(), name='edit_draft'),
    path('publish_draft/<slug:slug>/', EditDraft.as_view(), name='publish_draft'),
    path('drafts/delete/<slug:slug>/', DeleteDraft.as_view(), name='delete_draft'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('tag/<slug:slug>/', views.Tagged.as_view(), name='tagged'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('edit/<slug>/', views.EditPost.as_view(), name='edit_post'),
    path('delete/<slug>/', views.DeletePost.as_view(), name='delete_post'),
]

# handling the 404 error
handler404 = 'blog.views.error_404_view'