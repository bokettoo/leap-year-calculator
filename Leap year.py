def leapyear(year):
    if year%100 != 0:
        if year%4==0:
            return True
        else:
            return False
    else:
        if year%400==0:
            return True
        else:   
            return  False

def leapscentury(century): 
 for i in range((century*100)-99, (century*100)) :
        if i%100 != 0:
            if i%4==0:
                return True
            else:
                return False
        else:
            if i%400==0:
             return True
            else:   
                return  False