from django.db import models

class Image(models.Model):
    uname = models.CharField(max_length=200)
    age = models.IntegerField(verbose_name = 'Age')
    gender = models.CharField(max_length=200, verbose_name = 'Gender')
    about_me = models.TextField(verbose_name='About me', blank=True,null=True)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = [ 'date_added' ]

    def __str__(self):
        return self.uname
