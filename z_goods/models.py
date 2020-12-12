from django.db import models

# Create your models here.

#商品信息表
class GoodInfo(models.Model):

    state=(
        ("on","在售"),
        ("out","售空"),
    )

    gname = models.CharField(max_length=50, unique=True, verbose_name="商品名称")
    gprice = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="商品价格")
    gcount = models.IntegerField(default=1, verbose_name="库存")
    gintro = models.CharField(max_length=500, verbose_name="商品简介")
    gstate = models.CharField(max_length=10, choices=state, default="在售", verbose_name="商品状态")
    #gpicture = models.
    gtype = models.ForeignKey('GoodType', on_delete=models.CASCADE, verbose_name="类别")

    def __str__(self):
        return self.gname

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"


#商品种类表
class GoodType(models.Model):

    gtname = models.CharField(max_length=10, unique=True, verbose_name="类别")

    def __str__(self):
        return self.gtname

    class Meta:
        verbose_name = "商品类型"
        verbose_name_plural = "商品类型"