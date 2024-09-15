from django.db import models


class Transportation(models.Model):
    operator = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='transportations', verbose_name='Оператор')
    route = models.CharField(max_length=255, verbose_name='Направление')
    transport_price = models.CharField(max_length=50, verbose_name='Цена перевозки')
    advance_payment = models.CharField(max_length=255, blank=True, null=True, verbose_name='Аванс')
    license_plate = models.CharField(max_length=50, verbose_name='Госномер')  # Vehicle license plate
    cargo_owner = models.CharField(max_length=255, verbose_name='Владелец груза')  # Cargo owner name
    loading_date = models.DateField(verbose_name='Дата Погрузки')  # Loading date
    unloading_date = models.DateField(verbose_name='Дата Выгрузки')  # Unloading date
    remaining_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='Кому Оплачен')  # Remaining payment amount
    business_trip = models.TextField(blank=True, null=True, verbose_name='Kомандировичный')
    additional = models.TextField(blank=True, null=True, verbose_name='Дополнительный')

    class Meta:
        db_table = 'transportation'
        verbose_name = 'Transportation'
        verbose_name_plural = 'Transportations'

    def __str__(self):
        return f"{self.route} - {self.transport_price}"
