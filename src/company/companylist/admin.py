from django.contrib import admin
from .models import Company
# Register your models here.
admin.site.register(Company)

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	#list_editable = ["title"]
	#list_filter = ["updated", "timestamp"]

	search_fields = ["company_name", "content"]
	class Meta:
		model = Company


admin.site.register(Company, PostModelAdmin)