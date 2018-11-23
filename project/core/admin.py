from django.contrib import admin
from .models import Tag, Payment
# Register your models here.

admin.site.register(Tag)

class PaymentAdmin(admin.ModelAdmin):
	list_display = (
		'description',
		'value',
		'tag',
		'initial_date',
		'final_date'
	)

admin.site.register(Payment, PaymentAdmin)