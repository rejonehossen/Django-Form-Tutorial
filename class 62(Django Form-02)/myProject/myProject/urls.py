from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/',index,name="index"),
    path('signup/',signup,name="signup"),
    path('signout/',signout,name="signout"),
    path('',singin,name="singin"),
    
    # CRUD
    path('addcategorypage/',addcategorypage,name="addcategorypage"),
    path('categorylist/',categorylist,name="categorylist"),
    path('addtask/',addtask,name="addtask"),
    path('tasklist/',tasklist,name="tasklist"),
    path('edittask/<str:myid>',edittask,name="edittask"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
