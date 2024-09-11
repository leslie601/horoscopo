print("ingresar los datos en formato numerico")

#declaramos variables
dia=int(input("ingresa tu dia de nacimiento: "))
mes=int(input("ingresa tu mes: "))

#se realiza la logica del programa
if(mes==3 and dia>=21 or mes==4 and dia<=19):
    signos="tu eres aries"
elif(mes==4 and dia>=20 or mes==5 and dia<=20):
    signos="tu eres tauro"
elif(mes==5 and dia>=21 or mes==6 and dia<=20):
    signos="tu eres geminis"
elif(mes==6 and dia>=21 or mes==7 and dia<=22):
    signos="tu signo es cancer"
elif(mes==7 and dia>=23  or mes==8 and dia<=22):
    signos="tu signo es leo"
elif(mes==8 and dia>=23 or mes==9 and dia<=22):
    signos="tu signo es virgo"
elif(mes==9 and dia>=23 or mes==10 and dia<=22):
    signos="tu signo es libra"
elif(mes==10 and dia>=23 or mes==11 and dia<=21):
    signos="tu signo es escorpio"
elif(mes==11 and dia>=22 or mes==12 and dia<=21):
    signos="tu signo es sagitario"
elif(mes==12 and dia>=22 or mes==1 and dia<=19):
    signos="tu signo es capricornio"
elif(mes==1 and dia>=20 or mes==2 and dia<=18):
    signos="tu signo es acuario"
elif(mes==2 and dia>=19 or mes==3 and dia<=20):
    signos="tu signo es picis"

print(signos)
