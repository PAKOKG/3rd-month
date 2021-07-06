from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"
    def __str__(self):
        return self.name

class Exam(models.Model):
    score = models.CharField(max_length=100, verbose_name="Балы")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    Language = models.ForeignKey(Language,
                                 on_delete=models.CASCADE, verbose_name="Языки")

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"

    def __str__(self):
        return self.score


class Feedback(models.Model):
    text = models.TextField(verbose_name="Текст")
    language = models.ForeignKey(Language,
                                on_delete=models.CASCADE, verbose_name="Предметы")

    class Meta:
        verbose_name = "Обзор"
        verbose_name_plural = "Обзоры"

    def __str__(self):
        return self.text

