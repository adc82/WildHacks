from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic.base import TemplateView


class HomePageView (TemplateView):
	template_name = 'wild_hacks/homepage.html'

class AboutUsView(TemplateView):
	#sjkflashdfkjahsf
	template_name = 'wild_hacks/about_us.html'





