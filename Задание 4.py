a = int(input("Введите 1 число:"))
c = input("Введите желаемую операцию:")
b = int(input("Введите 2 число:"))
match c:
   case "+": print(a + b)
   case "-": print(a - b)
   case "*": print(a * b)
   case "/":
      if b == 0:
         print("Ошибка!На ноль делить нельзя")
      else: print(a / b)
