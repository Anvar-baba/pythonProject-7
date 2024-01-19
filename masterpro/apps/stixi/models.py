from django.db import models

class Stixi(models.Model):
    stixi_title = models.CharField('название стихотворения', max_length = 20)
    stixi_text = models.TextField('текст стихотворения')
    pub_date = models.DateTimeField('год написания')

    def __str__(self):
        return self.stixi_title
    class Meta:
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'

class Comment(models.Model):
    stixi = models.ForeignKey(Stixi, on_delete = models.CASCADE)
    author_comment = models.TextField('комментарии автора')

    def __str__(self):
        return self.author_comment

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
