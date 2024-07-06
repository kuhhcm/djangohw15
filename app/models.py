from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
