from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

# Create your models here.

class Category(models.Model):
    name = models.CharField(_('Nome'), max_length=100)
    description = models.TextField(_('Descrição'), blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(_('Título'), max_length=100)
    post_text = models.TextField(_('Texto'))
    photo = models.ImageField(_('Foto'), upload_to='images')
    category = models.ForeignKey(Category, verbose_name=_('Categoria'))
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
    
    def __str__(self):
        return self.title