from django.views.generic import TemplateView


class Testpage(TemplateView):
    template_name = 'test.html'


class Thankspage(TemplateView):
    template_name = 'thanks.html'


class Homepage(TemplateView):
    template_name = 'index.html'