from django.db import models


from django.contrib.auth.models import User

# Create your models here.

class IndexModel(models.Model):

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

class Brand(IndexModel):

    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 
    

class Size(IndexModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    

class Category(IndexModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    


class Tag(IndexModel):

    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name 
    


class Product(IndexModel):

    title=models.CharField(max_length=200)

    description=models.TextField()

    price=models.PositiveIntegerField()

    image=models.ImageField(upload_to="product_images",null=True,blank=True)

    brand_object=models.ForeignKey(Brand,on_delete=models.CASCADE)

    category_object=models.ForeignKey(Category,on_delete=models.CASCADE)

    stock=models.IntegerField()

    size_objects=models.ManyToManyField(Size)

    tag_objects=models.ManyToManyField(Tag)


    def __str__(self):
        return self.title 
    

class Cart(IndexModel):

    owner=models.OneToOneField(User,on_delete=models.CASCADE)



#query to fecth Cart of authenticated user

#Cart.Object.get(owner=request.user) > normally calling

#request.user.cart/.all()getting logined user cart


class CartItems(IndexModel):

    Product_object=models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)

    Size_object=models.ForeignKey(Size,on_delete=models.CASCADE)

    is_order_placed=models.BooleanField(default=False)

    Cart_Object=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_item") #reverse reverense

#query to fecth Cart of authenticated user

#Cartitems.objects.filter(Cart_object__owner=request.user)

#request.user.cart.cart_item.filter(is_order_placed=false)











    








    




    

             
    






