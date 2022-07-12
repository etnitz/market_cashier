def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to add items and Q to quit:')
        if details.upper() == 'A':
            item = input("Enter Item:")
            quantity = int(input('Enter quantity:'))
            buyingData.update({item: quantity})
        elif details.upper() == 'Q':
            enterDetails = False
        else:
            print('Did not get that, A to add items or Q to quit')
    return buyingData

def getPrice(item, quantity):
    priceData = {
        'Biscuit' : 3,
        'Chicken' : 5,
        'Egg' : 1,
        'Coke' : 2,
        'Bread' : 2,
        'Apple' : 3,
        'Onion' : 3
    }
    subtotal = priceData[item] * quantity
    print(item + ': $' + str(priceData[item]) + ' x ' + str(quantity) + ' = ' + '$' + str(subtotal))
    return subtotal
