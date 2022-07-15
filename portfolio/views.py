from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import (
		Portfolio,
		Services,
		Resume,
	)

from django.views.generic import TemplateView, FormView, ListView, DetailView

from . forms import ContactForm


class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		service = Services.objects.filter(is_active=True).order_by('-id')[:3]
		portfolio = Portfolio.objects.filter(is_active=True).order_by('-id')[:6]
		resume = Resume.objects.filter(is_active=True).order_by('-id')[:3]
		context["portfolio"] = portfolio
		context["services"] = service
		context["resume"] = resume

		return context



class PortfolioView(ListView):
	model = Portfolio
	template_name = "portfolio-list.html"
	paginate_by = 9

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)[:9]


class PortfolioDetailView(DetailView):
	model = Portfolio	
	template_name = "portfolio-detail.html"
	








class ContactView(FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)