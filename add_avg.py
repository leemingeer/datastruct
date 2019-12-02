#!/usr/bin/env python

#
#no input parameter ,because parameters and input by generator send method,and yield will receive this parameters
# an new input parameter method, amazing
def add_average():
    sum = 0
    count = 0
    average = None
    all_items = []
    while True:
        item = yield average, all_items
        all_items.append(item)
        sum += item
        count += 1
        average = sum / count
    


if __name__ == "__main__":
    g = add_average()
    #come to the generator code logic unit, generator will stop to execute and return when encount yield
    next(g) # return None [], no need to receive return values of generator since no data send to the generator
    while True:
        num = input("please input a integer")
        if num == 'q':
            print("calculation end!")
            break
        avg, all_items = g.send(int(num))
        print("all items %s, avg %s" %(all_items, avg))