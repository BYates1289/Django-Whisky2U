from django.db import models
from django.utils.translation import gettext_lazy as _

TYPE = (
    ("monthly_pick", "monthly pick"),
    ("most_popular", "most popular"),
    ("latest_arrival", "latest arrival"),
)


class Review(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=60, null=False, blank=False)
    message = models.TextField(max_length=300, null=False, blank=False)
    review_date = models.DateField(auto_now=True)


class HomeProduct(models.Model):
    product = models.ForeignKey(
        "product.Product", verbose_name=_("Product"), on_delete=models.CASCADE
    )
    type = models.CharField(
        _("Type"),
        max_length=50,
        choices=TYPE,
        unique=True,
    )

    class Meta:
        verbose_name = _("Home Product")
        verbose_name_plural = _("Home Products")

    def __str__(self):
        return f"{self.type}"
