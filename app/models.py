# 管理する情報を設定
from django.db import models
from django.core import validators


# 管理する情報
class Information(models.Model):
    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )
    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )
    email = models.CharField(
        verbose_name='mail',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='年齢',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='メモ',
        max_length=300,
        blank=True,
        null=True,
    )
    user = models.CharField(
        verbose_name='登録ユーザー',
        max_length=200,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'メンバー'
        verbose_name_plural = 'メンバー'
