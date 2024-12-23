from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.

STATE_CHOICES =(


        ('BAG', 'Bagerhat'),
        ('BAN', 'Bandarban'),
        ('BAR', 'Barguna'),
        ('BRS', 'Barishal'),
        ('BHO', 'Bhola'),
        ('BOG', 'Bogra'),
        ('BRA', 'Brahmanbaria'),
        ('CHA', 'Chandpur'),
        ('CHT', 'Chattogram'),
        ('CHU', 'Chuadanga'),
        ('COM', 'Comilla'),
        ('COX', 'Cox\'s Bazar'),
        ('DHA', 'Dhaka'),
        ('DIN', 'Dinajpur'),
        ('FAR', 'Faridpur'),
        ('FEN', 'Feni'),
        ('GAI', 'Gaibandha'),
        ('GAZ', 'Gazipur'),
        ('GOP', 'Gopalganj'),
        ('HAB', 'Habiganj'),
        ('JAM', 'Jamalpur'),
        ('JES', 'Jashore'),
        ('JHA', 'Jhalokati'),
        ('JHN', 'Jhenaidah'),
        ('JOY', 'Joypurhat'),
        ('KHA', 'Khagrachari'),
        ('KHU', 'Khulna'),
        ('KIS', 'Kishoreganj'),
        ('KUR', 'Kurigram'),
        ('KUS', 'Kushtia'),
        ('LAK', 'Lakshmipur'),
        ('LAL', 'Lalmonirhat'),
        ('MAD', 'Madaripur'),
        ('MAG', 'Magura'),
        ('MAN', 'Manikganj'),
        ('MAU', 'Maulvibazar'),
        ('MEH', 'Meherpur'),
        ('MUN', 'Munshiganj'),
        ('MYM', 'Mymensingh'),
        ('NAO', 'Naogaon'),
        ('NAR', 'Narail'),
        ('NAR2', 'Narayanganj'),
        ('NRS', 'Narsingdi'),
        ('NAT', 'Natore'),
        ('NET', 'Netrokona'),
        ('NIL', 'Nilphamari'),
        ('NOA', 'Noakhali'),
        ('PAB', 'Pabna'),
        ('PAN', 'Panchagarh'),
        ('PAT', 'Patuakhali'),
        ('PIRO', 'Pirojpur'),
        ('RAJB', 'Rajbari'),
        ('RAJS', 'Rajshahi'),
        ('RAN', 'Rangamati'),
        ('RAN2', 'Rangpur'),
        ('SAT', 'Satkhira'),
        ('SHA', 'Shariatpur'),
        ('SHER', 'Sherpur'),
        ('SIR', 'Sirajganj'),
        ('SUN', 'Sunamganj'),
        ('SYL', 'Sylhet'),
        ('TAN', 'Tangail'),
        ('THA', 'Thakurgaon'),
)


CATEGORY_CHOICES=(

    ('CR','Curd'),
       ('ML','Milk'),
          ('LS','Lassi'),
             ('MS','Milkshake'),
                ('PN','Panner'),
                   ('GH','Ghee'),
                      ('CZ','Cheese'),
                        ('IC','Ice-Creams'),
     
)

class Product(models.Model):
    title =models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price =models.FloatField()
    description = models.TextField()
    composition =models.TextField(default='')
    prodapp =models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image =models.ImageField(upload_to='product')
def __str__(self):
    return self.title



class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    locality =models.CharField(max_length=200)
    city =models.CharField(max_length=200)
    mobile =models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state =models.CharField(choices=STATE_CHOICES,max_length=100)
def __str__(self):
    return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
