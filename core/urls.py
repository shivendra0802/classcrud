from django import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school.urls')),
    # path('', views.MyView.as_view()),
    # # path('homecl/', views.HomeclassView.as_view(), name='home'),
    # path('aboutcl/', views.AboutView.as_view(), name='about'),
    # path('contactcl/', views.ContactView.as_view(), name='contact'),
    # path('newscl/', views.NewsView.as_view(), name='news'),
    # path('home/', views.TemplateView.as_view(template_name='school/home.html'), name='home'),

]
