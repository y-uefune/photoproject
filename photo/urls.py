from django.urls import path
from . import views

app_name = 'photo'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('post/',views.CreatePhotoView.as_view(),name='post'),#投稿
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),#投稿完了
    path('photos/<int:category>',views.CategoryView.as_view(),name = 'photos_cat'),

    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',views.UserView.as_view(),name = 'user_list'),

    path('photo-detail/<int:pk>',views.DetailView.as_view(), name = 'photo_detail'),
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),
    # 投稿写真の削除
    # photo/<Photo postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name = 'photo_delete'),
]