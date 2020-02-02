from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_sentinel_user))
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('last time modified', auto_now=True)

    def __str__(self):
        return self.title
    
    @classmethod
    def get_with_shape(cls, shape, order_by='-last_modified'):
        """ return (shape[0], shape[1]) list of articles """
        articles = Article.objects.order_by('-last_modified')[:shape[0] * shape[1]]
        return [[articles[i*shape[1]+j]for j in range(0, shape[1])] for i in range(0, shape[0])]