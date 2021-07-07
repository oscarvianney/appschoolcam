from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.

#3rd apps field
from ckeditor.fields import RichTextField


def user_directory_path(instance, filename):
	#THis file will be uploaded to MEDIA_ROOT /the user_(id)/the file
	return 'user_{0}/{1}'.format(instance.user.id, filename)

class PostFileContent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField(upload_to=user_directory_path)
	posted = models.DateTimeField(auto_now_add=True)

	def get_file_name(self):
		return os.path.basename(self.file.name)

def save_lesson_files(instance, filename):
	upload_to = 'img/'
	ext = filename.split('.')[-1]
	# get filename
	if instance.page_id:
		filename = 'lesson_files/{}/{}.{}'.format(instance.page_id, instance.page_id, ext)
		if os.path.exists(filename):
			new_name = str(instance.lesson_id) + str('1')
			filename = 'page_images/{}/{}.{}'.format(instance.page_id, new_name, ext)
	return os.path.join(upload_to, filename)

class Page(models.Model):
	page_id = models.CharField(max_length=100, null=True, unique=True)
	title = models.CharField(max_length=150)
	content = RichTextField()
	files = models.ManyToManyField(PostFileContent)
	video = models.FileField(upload_to=save_lesson_files, verbose_name="Media", blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_owner')

	def __str__(self):
		return self.title

