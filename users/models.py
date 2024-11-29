from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    city = models.CharField(
        max_length=80,
        blank=True,
        null=True,
        verbose_name="Город",
        help_text="Укажите из какого вы города",
    )
    avatar = models.ImageField(
        upload_to="users/avatars", blank=True, null=True, verbose_name="Аватар"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    method_choices = [
        ("CASH", "Наличными"),
        ("TRANSFER", "Перевод на счет"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    payment_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    payment_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )

    payment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата платежа"
    )
    amount = models.PositiveIntegerField(
        verbose_name="Сумма платежа"
    )
    payment_method = models.CharField(
        max_length=50,
        choices=method_choices,
        verbose_name="Метод оплаты"
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        blank=True,
        null=True,
    )
    link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        verbose_name="Статус платежа",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.amount
