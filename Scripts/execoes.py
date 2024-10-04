try:
    a = 10
    b = 0
    c = a / (b + k)
except (ZeroDivisionError, NameError) as error:
    print(f"{error.__class__.__name__} alguma coisa saiu errado")
