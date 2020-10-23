def faktorial(n):
    """ Used for count faktorial value. Used in get_combination_count function """
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def get_multiplier_view(variable, pow):
    """ Return view of multiplier. Used in for cycle, __main__ function """
    multiplier = ""
    if pow == 1:    
        multiplier += variable
    elif pow != 0:
        multiplier += "{v}^{p}".format(p=pow, v=variable)
    return multiplier

def get_combination_count(quanity, _from):
    """ Returns count of combination. Used for count coefficients """
    return int(faktorial(_from) / (faktorial(quanity) * (faktorial(_from - quanity))))    

def get_formule(n):
    """ Returns a formule string """
    formule = "(a + b)^{n} = ".format(n=n)
    terms = []
    for i in range(n + 1):
        c = get_combination_count(i, n)
        p1 = n - i
        p2 = i
        if c == 1:
            c = ""
        term = "{c}{m1}{m2}".format(c=c, m1=get_multiplier_view("a", p1), m2=get_multiplier_view("b", p2))
        terms.append(term)
    
    formule += " + ".join(terms)
    return formule
if __name__ == "__main__":
    n = int(input("[>] Please enter n for finding Binominal Theoreme formule: "))
    print(get_formule(n))
