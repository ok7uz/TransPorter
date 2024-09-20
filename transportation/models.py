from django.db import models


class Transportation(models.Model):

    class StatusColors(models.TextChoices):
        PENDING = 'warning', 'В ожидании'
        COMPLETED = 'success', 'Выполнено'
        CANCELED = 'danger', 'Отменено'

    operator = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='transportations', verbose_name='Оператор')
    route = models.CharField(max_length=255, verbose_name='Направление', null=True, blank=True)
    transport_price = models.CharField(max_length=50, verbose_name='Цена перевозки', null=True, blank=True)
    advance_payment = models.CharField(max_length=255, blank=True, null=True, verbose_name='Аванс')
    license_plate = models.CharField(max_length=50, null=True, blank=True, verbose_name='Госномер')  # Vehicle license plate
    cargo_owner = models.CharField(max_length=255, null=True, blank=True, verbose_name='Владелец груза')  # Cargo owner name
    loading_date = models.DateField(verbose_name='Дата Погрузки', null=True, blank=True,)  # Loading date
    unloading_date = models.DateField(verbose_name='Дата Выгрузки', null=True, blank=True)  # Unloading date
    paid_to = models.CharField(max_length=255, blank=True, null=True, verbose_name='Кому Оплачен')  # Remaining payment amount
    remaining_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='Остаток')
    business_trip = models.TextField(blank=True, null=True, verbose_name='Kомандировичный')
    additional = models.TextField(blank=True, null=True, verbose_name='Дополнительный')
    status = models.CharField(max_length=7, choices=StatusColors, verbose_name='Статус', default='warning')
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'transportation'
        verbose_name = 'Transportation'
        verbose_name_plural = 'Transportations'

    def __str__(self):
        return f"{self.route} - {self.transport_price}"
