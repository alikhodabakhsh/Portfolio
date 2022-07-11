from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import (
		UserProfile,
		Portfolio,
		Skill,
		Tool,
		History,
		AboutMe,
	)

from django.views.generic import TemplateView, FormView, ListView, DetailView

from . forms import ContactForm


class IndexView(TemplateView):
	template_name = "homePage.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		portfolio = Portfolio.objects.filter(is_active=True)
		skill = Skill.objects.filter(is_key_skill=True)
		tool = Tool.objects.filter(is_key_tool=True)
		about_me = AboutMe.objects.all()
		history = History.objects.all()
		context["portfolio"] = portfolio
		context["skills"] = skill
		context["tools"] = tool
		context["about_me"] = about_me
		context["history"] = history

		return context


class ContactView(FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(ListView):
	model = Portfolio
	template_name = "portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(DetailView):
	model = Portfolio	
	template_name = "portfolio-detail.html"
	
