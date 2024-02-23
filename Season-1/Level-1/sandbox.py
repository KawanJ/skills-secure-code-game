import code as c

# tv_item = c.Item(type='product', description='tv', amount=1000.00, quantity=1)
# payment = c.Item(type='payment', description='invoice_4', amount=1e19, quantity=1)
# payback = c.Item(type='payment', description='payback_4', amount=-1e19, quantity=1)
# order_4 = c.Order(id='4', items=[payment, tv_item, payback])
# print(c.validorder(order_4))

# small_item = c.Item(type='product', description='accessory', amount=3.3, quantity=1)
# payment_1 = c.Item(type='payment', description='invoice_5_1', amount=1.1, quantity=1)
# payment_2 = c.Item(type='payment', description='invoice_5_2', amount=2.2, quantity=1)
# order_5 = c.Order(id='5', items=[small_item, payment_1, payment_2])
# print(c.validorder(order_5))

num_items = 12
items = [c.Item(type='product', description='tv', amount=99999, quantity=num_items)]
for i in range(num_items):
    items.append(c.Item(type='payment', description='invoice_' + str(i), amount=99999, quantity=1))
order_1 = c.Order(id='1', items=items)
print(c.validorder(order_1))

# Put payments before products
items = items[1:] + [items[0]]
order_2 = c.Order(id='2', items=items)
print(c.validorder(order_2))