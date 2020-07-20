#2.2.3
#using formatting
#string: %s
#character: %c
#integer: %d
#floating_point: %f

print("I eat %d apples"%3)
print("I eat %s apples"%"Three")
number=3
print("I eat %d apples"%number)

print("I ate %s apples for %d days"%("Three",5))
print("There is %d%% chance of success"%88)

print("%10s"%"hi")  #using 10 characters but written from right
print("%-10s"%"hello")  #using 10 characters but written from left
print("%0.4f"%2.355234)
print("%10.4f"%3.24524124)

print("I eat {0} apples a day".format(2))
print("I ate {0} apples for a day".format("five"))
number=5
print("I ate {0} apples for a day".format(number))
print("I ate {0} apples for {1} days".format("seven","three"))

print("{0:<10}".format("hi"))  #hi________
print("{0:>10}".format("hi"))  #________hi
print("{0:^10}".format("hi"))  #____hi____
print("{0:=^10}".format("hi"))  #====hi====
print("{0:!<10}".format("hi"))  #!!!!hi!!!!
