# def add_item(item, item_list=[]): # default value
#     item_list.append(item)
#     return item_list

from datetime import datetime


def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list


print(add_item('apple'))
print(add_item('Orange'))
print(add_item('banana'))


def myfun(msg, *, dt=None):
    if not dt:  # null
        dt = datetime.utcnow()
        print(f'{dt} {msg}')


myfun('text message')
