from django.db import models

# Create your models here.

from accounts.models import CustomUser

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリ',max_length=20)

    def __str__(self):
        return self.title
    
class PhotoPost(models.Model):
# CustomUserモデル(のuser_id)とPhotoPostモデルを
# 1対多の関係で結び付ける
# CustomUserが親でPhotoPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )

# Categoryモデル(のtitle)とPhotoPostモデルを
# 1対多の関係で結び付ける
# Categoryが親でPhotoPostが子の関係となる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    title = models.CharField(verbose_name='タイトル',max_length=200)

    comment = models.TextField(verbose_name='コメント',)

    image1 = models.ImageField(verbose_name='イメージ1',upload_to = 'photos')

    image2 = models.ImageField(verbose_name='イメージ2',upload_to='photo',blank=True,null=True)

    posted_at = models.DateTimeField(verbose_name='投稿日時',auto_now_add=True)

    def __str__ (self):
        return self.title