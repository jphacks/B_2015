from django.urls import path
from django.conf.urls import url
from polls import views
from django.urls import include, path   # includeを追加
from django.views.generic import TemplateView   # 追加

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('inquiry/', views.calc, name="calc"),
    path('login/', views.login, name='login'),
    path("ajax/", views.call_bungou, name="call_bungou"),
    # path('login/', views.DiaryListView.as_view(), name="login"),
    # path('login/', views.login, name='login'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')), # 不要
]