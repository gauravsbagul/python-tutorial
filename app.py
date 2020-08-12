price = 1000000
isGoodCredit = True

if isGoodCredit:
    print('You need to put down 10%')
    downPayment = price * 0.1
else:
    print('You need to pud down 20%')
    downPayment = price * 0.2

print(f'Down Payment: {downPayment}')
