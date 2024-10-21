from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма транзакции
    category = models.CharField(max_length=100)  # Категория (например, еда, транспорт)
    date = models.DateField()  # Дата транзакции
    description = models.TextField(null=True, blank=True)  # Описание транзакции (необязательно)

    def __str__(self):
        return f'{self.category}: {self.amount}'
