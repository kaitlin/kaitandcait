from django.db import models
from django.contrib.auth.models import User
from articles.models import Article

class Podcast(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    description = models.TextField()
    file = models.FileField(upload_to='podcasts')
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField('Date Published')
    related_articles = models.ManyToManyField(Article)
    url = models.URLField(verify_exists=True)
    
    def __unicode__(self):
        return self.title
