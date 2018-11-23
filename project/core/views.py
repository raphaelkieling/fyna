from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from graphos.sources.model import ModelDataSource
from graphos.renderers import highcharts
from django.db.models import Sum
import datetime

today = datetime.date.today()
now   = datetime.datetime.now()

def home(request):
	initial_date = '{}-{}-{}'.format(today.year, today.month, '01')
	final_data   = '{}-{}-{}'.format(today.year, today.month, '30')

	payment_filter = Payment.objects.filter(initial_date__gte=initial_date, final_date__lte=final_data)

	total_gastos_value = payment_filter.filter(is_renda=False).aggregate(Sum('value'))
	total_renda_value  = payment_filter.filter(is_renda=True).aggregate(Sum('value')) 

	payments = payment_filter.filter(is_renda=False).order_by('initial_date')

	data_source =  ModelDataSource(payments, fields=['initial_date','value'])
	chart = highcharts.LineChart(data_source, width='100%', height='100%')

	return render(request, 'core/home.html', {
		'data_atual': today.month,
		'payments': payments,
		'total_gastos_value': total_gastos_value['value__sum'],
		'total_renda_value': total_renda_value['value__sum'],
		'line_chart': chart
	})

def payment_new(request):
	
	if request.method == "POST":
		form = PaymentForm(request.POST)
		if form.is_valid():
			payment = form.save(commit=False)
			payment.save()
			return redirect('home')
	else:
		form = PaymentForm()
		
	return render(request, 'core/payment_new.html', {'form': form})