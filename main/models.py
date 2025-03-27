from django.db import models

class categories(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category/')

   

    class Meta:
         verbose_name_plural = 'category'

    def __str__(self):     
        return self.title

class News(models.Model):
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    title = models.CharField(max_length = 250)
    description = models.TextField()
    image = models.ImageField(upload_to='News/')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News' 


 


