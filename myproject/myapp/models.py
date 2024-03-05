from django.db import models
#from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    foto_of_personal = models.ImageField()
    post = models.CharField(max_length=200)
    date_created_personal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Имя: {self.name}, фамилия: {self.second_name}, отчество: {self.last_name}, должность: {self.post}"

class New(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    foto_of_new = models.ImageField()
    date_created_new = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заголовок: {self.title}, содержание: {self.description}, фото: {self.foto_of_new}, дата публикации: {self.date_created_new}"

class Сonsumer(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    personal_account = models.CharField(max_length=50)
    date_created_personal = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return f"Имя: {self.name}, фамилия: {self.second_name}, отчество: {self.last_name}, адресс: {self.address},"
    
class Vacancy(models.Model):
    profession = models.CharField(max_length=100)
    requirements = models.TextField()
    description = models.TextField()
    date_created_new = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Професиия: {self.profession}, требования: {self.requirements}, описнаие: {self.description}, дата публикации: {self.date_created_new}"

class Invocation(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    personal_account = models.CharField(max_length=50)
    date_created_personal = models.DateTimeField(auto_now_add=True)
    
"""
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    adress = models.CharField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Имя: {self.name}, почта: {self.email}, телефон: {self.phone}, адресс: {self.adress}, дата регистрации: {self.date_created}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    digits = models.IntegerField()
    image = models.ImageField(default="", blank=True)
    date_product_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Название: {self.name}, описание: {self.description}, цена: {self.price}, количество: {self.digits}, дата добавления: {self.date_product_added}"

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказчик: {self.customer}, продукты: {self.products}, общая стоимость: {self.total_price}, дата заказа: {self.date_ordered}"
"""