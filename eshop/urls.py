from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    #path('jet/', include('jet.urls', 'jet')), 
    path('pdf/', include('pdf_convert.urls')),
    path("",include("des.urls")),
   
]

    
