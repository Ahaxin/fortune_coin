# Misc functions

def largest(p1,p2,p3):
    if (p1 > p2) and (p1 > p3):
        return p1,'StellarTerm:'
    elif (p2 > p1) and (p2 > p3):
        return p2,'Binance:    '
    else:
        return p3,'OKEX:       '

def smallest(num1, num2, num3):
    if num1 == '0':
        if (num2 < num3) and num2!='0' :
            return num2,'Binance:    '
        else:
            return num3,'OKEX:       '
    elif num2 == '0':
        if (num1 < num3) and num1 !='0':
            return num1,'StellarTerm:'
        else:
            return num3,'OKEX:       '
    elif num3 == '0':
        if (num1 < num2)and num1 !='0':
            return num1,'StellarTerm:'
        else:
            return num2,'Binance:    '
    elif (num1 < num2) and (num1 < num3):
        return num1,'StellarTerm:'
    elif (num2 < num1) and (num2 < num3):
        return num2,'Binance:    '
    else:
        return num3,'OKEX:       '
