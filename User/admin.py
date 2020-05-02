from django.contrib import admin
from django.apps import apps


admin.site.site_title = "MCQ Portal User"
app = apps.get_app_config('User')

for model_name, model in app.models.items():
    admin.site.register(model)