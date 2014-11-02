from django.db import models
from django.template.defaultfilters import slugify
from easy_thumbnails.fields import ThumbnailerImageField


class OhterModel(models.Model):
	title = models.CharField(max_length=500)

class OneOfEverthing(models.Model):
	title = models.CharField(max_length=500)
	text = models.TextField(max_length=1000,blank=True,null=True)
	date = models.DateTimeField(blank=True,null=True)
	floater = models.FloatField(default=0,blank=True,null=True)
	url = models.URLField(blank=True,null=True)		
	many = models.ManyToManyField(OhterModel,blank=True,null=True,related_name='many_otherfield') 
	forien = models.ForeignKey(OhterModel,blank=True,null=True,related_name='foreignkey_otherfield')
	image = ThumbnailerImageField(upload_to='location')

	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(OneOfEverthing, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title	