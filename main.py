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
