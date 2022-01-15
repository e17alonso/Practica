n = int(input("Ingrese la nota del estudiante "))
while(n>=0):
    if(n>75):
        print("0")
    if(n<=75 and n>=60):
        print("A")
    if(n<=59 and n>=50):
        print("B")
    if(n<=49 and n>=40):
        print("C")
    if(n<=39):
        print("D")
    n = int(input("Ingrese la nota del estudiante "))