from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItems(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    """ 
    Generic Relationship
    1. type(video, article, ...) 
    2. ID   
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_id = models.PositiveIntegerField()
    # object
    content_object = GenericForeignKey()
