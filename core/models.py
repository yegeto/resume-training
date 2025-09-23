from django.db import models


# Create your models here.
class AbstractModel(models.Model):
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
        help_text="This is variable of setting",
    )
    description = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text="",
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date",
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date",
    )

    def __str__(self):
        return f"{self._meta.verbose_name}: {self.name}"

    class Meta:
        abstract = True
        ordering = ("name",)

class GeneralSetting(AbstractModel):
    parameter = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Parameter",
        help_text="",
    )

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"


class ImageSetting(AbstractModel):
    file = models.ImageField(
        default="",
        verbose_name="Image",
        help_text="",
        blank=True,
        upload_to="images/",
    )

    class Meta:
        verbose_name = "Image Setting"
        verbose_name_plural = "Image Settings"

