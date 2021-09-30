from cart.models import *
from product.models import *
from justAdmin.models import *

import datetime
def createOrderItem(order,products):
    for i in products:
        product = Product.objects.all().filter(id=i["id"])[0]
        orderitem = OrderItem.objects.create(product=product,
                                             order=order,
                                             price = product.price,
                                             )
        product.amout -=i["quantity"]
        product.sold  +=i["quantity"]
        orderitem.quantity = i["quantity"]
        orderitem.size = i["size"]
        orderitem.save()
        product.save()

def countryUser(country):
    try:
        country=Country.objects.get(name=country)
    except:
        country=Country.objects.create(name=country)
        country.save()
    return country
def locationUser(order , customer,country,region):
    state = Region.objects.create(
        order =order,
        customer=customer,
        country= country,
        name =region,
    )
    state.save()

def createIncome(price):
    incom = Income.objects.all().latest('id')

    if incom.data_create.month == datetime.datetime.now().month:

        incom.total_revenue = float(price) +float(incom.total_revenue)
        print("total:",type(incom.total_revenue))
        incom.save()

    else:
        Income.objects.create(
            total_cost=float(price)
        )

