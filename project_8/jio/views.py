from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import WebsiteForm
from .models import Website

# Create your views here.


def Website_image_view(request):

	if request.method == 'POST':
		form = WebsiteForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = WebsiteForm()
	return render(request, 'website_image_form.html', {'form': form})


def success(request):
	return render(request,'success.html')
# Python program to view
# for displaying images


def website_display(request):

	if request.method == 'GET':

		# getting all the objects of hotel.
		Websites = Website.objects.all()
		return render(request, 'website_display.html', {'website_images': Websites})

