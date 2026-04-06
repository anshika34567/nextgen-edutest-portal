from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)

#results
from .models import Result
admin.site.register(Result)