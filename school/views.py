# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from .forms import ContactForm
# from django.views.generic.base import TemplateView, RedirectView
# # Create your views here.
# class MyView(View):
#     def get(self, request):
#         return HttpResponse('<h1>Class based View</h1>')

# class HomeclassView(View):
#     def get(self, request):
#         return render(request, 'school/home.html')

# class AboutView(View):
#     def get(self, request):
#         context = {'msg': 'Welcome to club'}
#         return render(request, 'school/about.html', context)

# class ContactView(View):
#     def get(self, request):
#         form = ContactForm()
#         return render(request, 'school/contact.html', {'form': form})

#     def post(get, request):
#         form = ContactForm()
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#         return HttpResponse('Thanku for submitted!!')


# class NewsView(View):
#     def get(self, request):
#         context = {'Info': 'CBI enquiry'}
#         return render(request, 'school/news.html', context)



from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Counter
# Create your views here.

class CounterCreateView(CreateView):
	model = Counter
	template_name = 'create_counter.html'
	fields = '__all__'
	success_url = reverse_lazy('list-count')


class CounterUpdateView(UpdateView):
	model = Counter
	template_name = 'create_counter.html'
	fields = '__all__'
	success_url = reverse_lazy('list-count')
	# template_name_suffix = '_update_form'

class CounterDeleteView(DeleteView):
	model = Counter
	success_url = reverse_lazy('list-count')
	template_name = 'confirm_counter_delete.html'

class CounterDetailView(DetailView):
	model = Counter
	template_name = 'counter_details.html'

	def get_context_data(self, **kwargs):
		context = super(CounterDetailView, self).get_context_data(**kwargs)
		return context


class CounterListView(ListView):
	model = Counter
	template_name = 'counter_list.html'

	def get_context_data(self, **kwargs):
		context = super(CounterListView, self).get_context_data(**kwargs)
		return context
