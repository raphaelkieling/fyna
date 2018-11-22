from django.shortcuts import render, redirect
from .forms import PaymentForm
from .models import Payment
from graphos.sources.model import ModelDataSource
from graphos.renderers import highcharts
import datetime

today = datetime.date.today()
now   = datetime.datetime.now()

def home(request):
	print(today)
	queryset = Payment.objects.filter(initial_date__gte='2005-01-05', final_date__lte=today).order_by('initial_date')
	data_source =  ModelDataSource(queryset, fields=['initial_date','value'])
	chart = highcharts.LineChart(data_source)

	return render(request, 'core/home.html', {
		'data_atual': now.month,
		'payments': queryset,
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