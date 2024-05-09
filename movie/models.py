from django.db import models


# Create your models here.


class Actor(models.Model):
    class Meta:
        verbose_name = 'بازیگران'
        verbose_name_plural = 'بازیگران'

    name = models.CharField(max_length=100, verbose_name='نام بازیگر', null=True, blank=True)
    image = models.TextField(verbose_name='عکس بازیگر', null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    class Meta:
        verbose_name = 'ژانر فیلم'
        verbose_name_plural = 'ژانر فیلم'

    NAME = [('0', 'اکشن'), ('1', 'انیمیشن'), ('2', 'درام'), ('3', 'ماجراجویی'), ('4', 'سایر')]

    name = models.CharField(max_length=1, verbose_name='ژانر فیلم', null=False, blank=False, default='4', choices=NAME)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم ها'

    original_name = models.CharField(max_length=150, verbose_name='نام فیلم به انگلیسی', null=False, blank=False)
    persian_name = models.CharField(max_length=150, verbose_name='نام فیلم به فارسی', null=False, blank=False)
    TYPE = [('0', 'فیلم'), ('1', 'سریال')]
    type = models.CharField(max_length=1, verbose_name='نوع', null=False, blank=False, choices=TYPE, default='0')
    actors = models.ManyToManyField(Actor, verbose_name='بازیگران', related_name='movies', )
    director = models.CharField(max_length=100, verbose_name='کارگردان', null=True, blank=True)
    writer = models.CharField(max_length=100, verbose_name='نویسنده', null=True, blank=True, )
    story_line = models.TextField(verbose_name='خلاصه داستان', null=True, blank=True)
    views_count = models.CharField(max_length=10, verbose_name='تعداد بازدید', null=True, blank=True)
    tag = models.CharField(max_length=255, null=True, blank=True, verbose_name='تگ')
    imdb_rate = models.CharField(max_length=3, verbose_name='امتیاز IMDB')
    year = models.CharField(max_length=4, verbose_name='سال تولید', null=True, blank=True)
    baner = models.TextField(verbose_name='پوستر فیلم', null=True, blank=True)
    tizer = models.TextField(verbose_name='تیزر فیلم', null=True, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name='ژانر', related_name='movie_genre', )
    box_office = models.CharField(max_length=100, verbose_name='باکس افیس', null=True, blank=True)
    prices = models.TextField(verbose_name='جوایز و افتخارات', null=True, blank=True)
    users_rate = models.CharField(max_length=6, null=True, blank=True, verbose_name='امتیاز کاربران')

    def __str__(self):
        return self.persian_name


class Banner(models.Model):
    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر ها'

    image = models.TextField(verbose_name='پوستر فیلم')
    movie = models.ForeignKey(Movie, verbose_name='فیلم', null=False, blank=False, related_name='banner_movie',
                              on_delete=models.CASCADE)
