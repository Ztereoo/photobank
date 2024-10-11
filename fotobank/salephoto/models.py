from django.db import models
from django.urls import reverse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from datetime import datetime

class Photo(models.Model):
    title= models.CharField(max_length=30, verbose_name='Название')
    content= models.TextField(max_length=300, verbose_name='Описание')
    keywords= models.CharField(max_length=255, verbose_name='ключевые слова')
    image_hr=models.ImageField(upload_to='photos/%Y/%m/%d',blank=True,verbose_name='Фото')
    date_taken= models.DateField(blank=True,null=True,verbose_name='Дата и время снимка')
    date_created= models.DateField(auto_now_add= True, verbose_name='Дата загрузки')
    category= models.ForeignKey('Category',on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo_detail',kwargs={'pk':self.pk})
    # def save(self, *args, **kwargs):
    #     if self.image_hr:
    #         try:
    #             img = Image.open(self.image_hr)
    #             exif_data = img._getexif()
    #             if exif_data:
    #                 for tag, value in exif_data.items():
    #                     tag_name = ExifTags.TAGS.get(tag, tag)
    #                     if tag_name == "DateTimeOriginal":
    #                         try:
    #                             self.date_taken = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    #                         except (ValueError, TypeError):
    #                             pass
    #         except Exception as e:
    #             print(f"Ошибка при обработке изображения: {e}")
    #         finally:
    #             img.close()
    #
    #     super().save(*args, **kwargs)

    class Meta():
        verbose_name='Фото'
        verbose_name_plural='Фотографии'
        ordering=['-date_taken']

class Category(models.Model):
    title=models.CharField(max_length=150,db_index=True,verbose_name='Название Категории')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['-title']
