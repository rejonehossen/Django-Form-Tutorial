from django.contrib import admin
from myApp.models import *

class displaycustomuser(admin.ModelAdmin):
    list_display=['username','email']
    search_fields=["username","usertype","city"]
    fieldsets=[
        (
            "Customuser Title",
            {
                "fields":[("username","password","email")],
            },
        ),
        (
            "Advance Option",
            {
                "classes":["collaps"],
                "fields":[("first_name","last_name"),"city","profile_pic"] #ব্রাকের্ট এর ভিতরে যে কয়টা ফিল্ড দেবো সেগুলো এক লাইন এ আসবে
            }
        ),
    ]
admin.site.register(customuser,displaycustomuser)


admin.site.register(categorymodel)
admin.site.register(TaskModel)