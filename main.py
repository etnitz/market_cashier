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

def getDiscount(bill, member):
    discount = 0
    if bill >= 25:
        if member == 'Gold':
            bill = bill * .8
            discount = 20
        elif member == 'Silver':
            bill = bill * .9
            discount = 10
        elif member == 'Bronze':
            bill = bill * .95
            discount = 5
        print(str(discount) + '% off for ' + member + ' membership on total: $' + str(bill))
    else:
        print('No discount on amount less than $25')
    return bill

def makeBill (buyingData, member):
    bill = 0
    for key, value in buyingData.items():
        bill += getPrice(key, value)
    bill = getDiscount(bill, member)
    print('The discounted amount is $' + str(bill))

