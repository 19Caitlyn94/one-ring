from django.db import models

class PostType(models.Model):
    posttype_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    request_url = models.URLField(max_length=255)

    def _str_(self):
        return self.name
