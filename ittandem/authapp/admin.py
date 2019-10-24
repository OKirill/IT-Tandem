from django.contrib import admin

from .models import User, Contact, Deal

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Deal)
