def diamond():

    num = int(input("Enter a number: "))

    for i in range(1, num+1):
      i = i - (num//2 +1)
      if i < 0:
        i = -i
      print(" " * i + "*" * (num - i*2) + " "*i)
diamond()