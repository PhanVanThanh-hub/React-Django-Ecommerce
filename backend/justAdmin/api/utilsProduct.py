from justAdmin.models import *
from product.models import *
import datetime

def createBill(data,product):

    Bill.objects.create(
        product=product,
        amount=data["amout"],
        cost=data["purchasePrice"],
    )

def createIncome(purchasePrice,amout):
    incom = Income.objects.all().latest('id')

    if incom.data_create.month == datetime.datetime.now().month:
        print("type:",type(incom.total_cost))
        incom.total_cost = float(purchasePrice) * amout + float(incom.total_cost)
        print("total:",type(incom.total_cost))
        incom.save()

    else:
        Income.objects.create(
            total_cost=float(purchasePrice) * amout
        )


def createNewProduct(getData):
    product = Product.objects.create(
        title=getData["title"],
        image=getData["images"],
        price=getData["price"],
        amout=getData["amout"]
    )
    product.save()
    try:
        sizes = getData["size"]
        for size1 in sizes:
            size = Size.objects.get(name=size1)
            product.size.add(size)
    except:
        print("ohno")
    try:
        category = Category.objects.get(name=getData["category"])
    except:
        category = Category.objects.create(name=getData["category"])
        category.save()
    product.category = category
    product.save()