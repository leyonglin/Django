from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField('书名',max_length=50,default='',unique=True)
    pub = models.CharField('出版社', max_length=100,default='')
    price = models.DecimalField('价格',max_digits=7,decimal_places=2)
    market_price = models.DecimalField('零售价',max_digits=7,decimal_places=2,default=0.0)
    is_active = models.BooleanField('是否活跃',default=True)
    class Meta():
        db_table='book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '%s_%s_%s_%s'%(self.title,self.price,self.pub,self.market_price)
'''
Book.objects.create(title='Python',pub='清华大学出版社',price=20,market_price=25)
Book.objects.create(title='Django',pub='清华大学出版社',price=70,market_price=75)
Book.objects.create(title='JQuety',pub='机械工业出版社',price=90,market_price=85)
Book.objects.create(title='Linux',pub='机械工业出版社',price=80,market_price=65)
Book.objects.create(title='HTML5',pub='清华大学出版社',price=90,market_price=105)
'''

class Author(models.Model):
    name = models.CharField('姓名',max_length=11)
    age = models.IntegerField('年龄',default=1)
    email = models.EmailField('邮箱',null=True)
    class Meta():
        db_table='author'
'''
Author.objects.create(name='王老师',age=28,email='wangleyong@tedu.cn')
Author.objects.create(name='吕老师',age=31,email='lvze@tedu.cn')
Author.objects.create(name='祁老师',age=30,email='qitx@tedu.cn')
'''