from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']  # Poradie podľa názvu kategórie


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        db_index=True
    )
    name = models.CharField(max_length=100, db_index=True)
    link = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'
        unique_together = ('category', 'name',)
        ordering = ['category__name', 'name']  # Zoradiť najskôr podľa kategórie a potom podľa názvu podkategórie
