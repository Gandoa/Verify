from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Verify_Code
from .models import User_verify
from django.conf import settings

# Create your views here.

def verify(request):
	if request.method == "POST":
		# form = Verify_Code(request.POST or None)
		# if form.is_valid():
		# 	form.save()
			code = request.POST.get('code')
			number = request.POST.get('number')
			User_verify.objects.create(code=code, number=number)
			
			messages.success(request, "Votre demande a biien été pris en compte ! vous serez bientôt notifier")
			return redirect('verify')
		   
	return render(request, 'verify.html')