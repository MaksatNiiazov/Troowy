from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class WelcomeBase(SingletonModel):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    content = models.TextField(verbose_name=_('Контент'))

    class Meta:
        abstract = True


class ImageBase(models.Model):
    content_object = models.ForeignKey(WelcomeBase, on_delete=models.CASCADE, verbose_name=_('Объект'))
    image = models.ImageField(upload_to='images/', verbose_name=_('Изображение'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Время обновления'))

    class Meta:
        abstract = True
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')


class WelcomeProperty(WelcomeBase):
    pass


class WelcomeCars(WelcomeBase):
    pass


class WelcomeTours(WelcomeBase):
    pass


class WelcomeInternationalTours(WelcomeBase):
    pass


class WelcomeMedicalTours(WelcomeBase):
    pass


class MainPage(SingletonModel):
    pass


class WelcomePropertyImage(ImageBase):
    content_object = models.ForeignKey(WelcomeProperty, on_delete=models.CASCADE, verbose_name=_('Объект'),
                                       related_name='images')


class WelcomeCarsImage(ImageBase):
    content_object = models.ForeignKey(WelcomeCars, on_delete=models.CASCADE, verbose_name=_('Объект'),
                                       related_name='images')


class WelcomeToursImage(ImageBase):
    content_object = models.ForeignKey(WelcomeTours, on_delete=models.CASCADE, verbose_name=_('Объект'),
                                       related_name='images')


class WelcomeInternationalToursImage(ImageBase):
    content_object = models.ForeignKey(WelcomeInternationalTours, on_delete=models.CASCADE, verbose_name=_('Объект'),
                                       related_name='images')


class WelcomeMedicalToursImage(ImageBase):
    content_object = models.ForeignKey(WelcomeMedicalTours, on_delete=models.CASCADE, verbose_name=_('Объект'),
                                       related_name='images')


class StaticPage(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=_('Заголовок'))
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name=_('Слаг'))
    content = models.TextField(verbose_name=_('Контент'))
    image = models.ImageField(upload_to='static_pages/', blank=True, null=True, verbose_name=_('Изображение'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Время создания'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Время обновления'))

    class Meta:
        verbose_name = _('Статическая страница')
        verbose_name_plural = _('Статические страницы')


class Banner(models.Model):
    TYPE_CHOICES = (
        ("all", _("Везде")),
        ("properties", _("Нудвижимость")),
        ("cars", _("Автомобили")),
        ("tours", _("Туры")),
        ("medical_tours", _("Медицинские туры")),

    )

    title = models.CharField(
        verbose_name="Заголовок", max_length=123, blank=True, null=True
    )
    image_desktop = models.ImageField(
        verbose_name="Картинка круп", upload_to="images/banners/desktop/%Y/%m/"
    )
    image_mobile = models.ImageField(
        verbose_name="Картинка моб", upload_to="images/banners/mobile/%Y/%m/"
    )
    page_for = models.CharField(
        verbose_name="Страница",
        choices=TYPE_CHOICES,
        max_length=200,
        blank=False,
        null=False,
        default="provider",
    )
    link = models.URLField(verbose_name="ссылка", max_length=200, blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Активный", default=True)
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, blank=True, null=True
    )

    def get_image_desktop(self):
        if self.image_desktop:
            return mark_safe(
                f'<img src="{self.image_desktop.url}" width="300px" height="auto" />'
            )
        return ""

    def get_image_mobile(self):
        if self.image_mobile:
            return mark_safe(
                f'<img src="{self.image_mobile.url}" width="300px" height="auto" />'
            )
        return ""

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ["is_active", "-created_at"]
