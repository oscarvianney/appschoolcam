from django.contrib import admin
from classroom.models import Course, Category, Classes, Matiere

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class ClassesAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

class MatiereAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Course)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Matiere, MatiereAdmin)