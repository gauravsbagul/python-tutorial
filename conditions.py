hasGoodCredit: bool = True
hasCriminalRecord: bool = True
temperature = 30
name = "Gaurav"
if hasGoodCredit:
    if not hasCriminalRecord:
        print('Eligible for loan')
    print('Not Eligible for loan')

if temperature == 30:
    print("It's a hot day")
else:
    print("It's not hot day")

if len(name) < 3:
    print('Name must be at least 3 character')
elif len(name) > 50:
    print("Name mush be less than 50 character")
else:
    print("Name looks good")

weight = int(input("Weight: "))
unit = input('(L)bs od (K)g: ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"You are {converted} pounds")
else:
    print("Wrong choice of unit")
i: int = 1
while i <= 5:
    print('*'*i)
    i += 1
print("Done")




