from django.contrib import admin
from .models import Document
# Register your models here.
#giup tui fix cai nay voi
class DocAdmin(admin.ModelAdmin):
    list_filter = ['course__semester__semester_id']

admin.site.register(Document, DocAdmin)