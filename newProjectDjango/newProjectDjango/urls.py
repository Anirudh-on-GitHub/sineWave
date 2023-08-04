from django.urls import include, re_path
import testApp.views

urlpatterns = [
    re_path(r'^$', testApp.views.index, name='index'),
    re_path(r'^outputsine$',testApp.views.outputsine,name='outputsine'),
    re_path(r'^home$', testApp.views.index, name='home'),
]

