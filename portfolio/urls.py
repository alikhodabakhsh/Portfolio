from django.urls import path
from .views import (
	IndexView,
	ContactView,
	PortfolioView,
	PortfolioDetailView,
)


app_name = "portfolio"

urlpatterns = [
	path('', IndexView.as_view(), name="home"),
	path('contact/', ContactView.as_view(), name="contact"),
	path('portfolio/', PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>/', PortfolioDetailView.as_view(), name="portfolio-detail"),
	]