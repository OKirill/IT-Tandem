from django.contrib import admin
from mainapp import models


admin.site.register(models.User)
admin.site.register(models.Tag)
admin.site.register(models.Project)
admin.site.register(models.Contact)
admin.site.register(models.Skill)
admin.site.register(models.Desire)
admin.site.register(models.RelatedTag)