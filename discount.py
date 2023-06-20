from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-06-20

time = datetime.now()
print(time)  # 2023-06-20 11:59:03.657571

print(type(time))  # <class 'datetime.datetime'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-06-21

print(time.hour)
print(today.day)  # 20

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 20},
    {'sku': 4, 'exp_date': today, 'price': 15.0},
    {'sku': 5, 'exp_date': today, 'price': 120},
    {'sku': 6, 'exp_date': tomorrow, 'price': 80},
    {'sku': 7, 'exp_date': today, 'price': 70.0},
]

print(products)

for product in products:
    print(product)
    if product['exp_date'] != today:
        continue  # wróci do początku pętli

    product['price'] *= 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")
