import time
import os
hora=int(input("Hora: "))
minuto=int(input("Minutos: "))
segundo=int(input("Segundos: "))
horas=int(hora*3600)
minutos=int(minuto*60)
total=horas+minutos+segundo
while total>0:
    horas=total//3600
    minutos=total//60
    segundos=total%60
    if horas<10:   
        print(f"0{horas}",end=":")
    else:
        print(horas,end=":")
    if minutos<10:   
        print(f"0{minutos}",end=":")
    else:
        if minutos==60:
            print("00",end=":")
        else:
            print(minutos,end=":")
    if segundos<10:   
        print(f"0{segundos}")
    else:
        print(segundos)

    total -=1
    time.sleep(1)
    os.system ("cls")

print("El tiempo termino")

