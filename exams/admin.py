
from django.contrib import admin

admin.site.site_header = "EduTest Portal Administration"
admin.site.site_title = "EduTest Portal Admin"
admin.site.index_title = "Welcome to EduTest Portal"
# Register your models here.
from .models import Exam, Question, Result
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Result)

from django.contrib import admin
from .models import Student
@admin.action(
    description="Block Selected Students"
)
def block_student(
    modeladmin,
    request,
    queryset
):
    queryset.update(
        is_blocked=True
    )


@admin.action(
    description="Unblock Selected Students"
)
def unblock_student(
    modeladmin,
    request,
    queryset
):
    queryset.update(
        is_blocked=False
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'course',
        'is_blocked'
    )

    list_filter = (
        'course',
        'is_blocked'
    )

    actions = [
        block_student,
        unblock_student
    ]

