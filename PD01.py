#1.uzd

#2.uzd

x=int(input("Enter x:"))
y=int(input("Enter y:"))

#3.uzd
def skaitli(skaitlis):
    if skaitlis > 0:
        return "Pozitīvs skaitlis"
    elif skaitlis < 0:
        return "Negatīvs skaitlis"
    else:
        return "0"
    
#4.uzd
x=int(input("Enter x: 5"))
y=int(input("Enter y: 10"))

result1= 4 * x ( y + 3 ) + 15 * y
 
print(result1)

result2= 5 * y * x - 144 * x + 2 / (x + y)*2
 
print(result2)
 
result3= 2 + x - 2 * x * y / y / x + y
 
print(result3)

#5.uzd
atzime = int(input("Lūdzu, ievadi savu atzīmi (veselu skaitli no 1 līdz 10): "))

if 1 <= atzime <= 10:

    if atzime >= 9:
        limenis = 'A'
    elif atzime >= 7:
        limenis = 'B'
    elif atzime >= 5:
        limenis = 'C'
    elif atzime >= 4:
        limenis = 'D'
    elif atzime >= 1:
        limenis = 'E'
    else:
        limenis = 'F'

    print(f"Tava atzīme: {atzime} - Līmenis: {limenis}")
else:
    print("Nepareiza atzīme! Lūdzu, ievadi skaitli no 1 līdz 10.")