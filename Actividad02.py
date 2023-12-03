def DMS(G1,M1,S1,G2,M2,S2):
    if(G1<0):
        K1 = "° S " 
        G1 = G1*(-1)
    else:
        K1 = "° N "
    if(G2<0):
        K2 = "° W "
        G2 = G2*(-1)
    else:
        K2 = "° E "
    DD1 = G1+int(M1)/60+float(S1)/3600 
    DD2 = G2+int(M2)/60+float(S2)/3600 
    DD = "\n"+str(DD1) + K1 + str(DD2) + K2 + "\n"
    return DD

def DD (Latitud,Longitud):
    if(Latitud<0):
        X='S '
        Latitud = Latitud*(-1)
    else:
        X='N '
    if(Longitud<0):
        Y='W '
        Longitud = Longitud*(-1)
    else: 
        Y='E '
    G1 = int(Latitud)
    G2 = int(Longitud)
    M1 = int((Latitud-G1)*60)
    M2 = int((Longitud-G2)*60) 
    S1 = float((((Latitud-G1)*60)-M1)*60)
    S2 = float((((Longitud-G2)*60)-M2)*60)
    Resultado = "\n-->Las coordenadas son: >> " + str(G1)+"° "+str(M1)+"\' "+str(S1)+"\'' " + X + str(G2)+"° "+str(M2)+"\' "+str(S2)+"\'' " + Y + "\n"
    return Resultado

print("\n")
Seleccion = 0
print("     Bienvenidos al conversos de coordenadas     ")
print("       Tipos de conversión a realizar       ")
print("Seleccione el tipo de conversion que desea realizar:\n")

while(Seleccion!='1' and Seleccion!='2'):
    print("  1.Decimales a Grados, Minutos y Segundos")
    print("  2.Grados, Minutos y Segundos a Decimales")
    Seleccion= input()

    if(Seleccion!='1' and Seleccion!='2'):
        print("\nNo ha ingresado una opcion valida\n")

if(Seleccion=='1'):
    print("     Has seleccionado convertir DD a GMS     ")
    
    Latitud = float(input("\nIngrese el valor de la longitud >  "))
    Longitud = float(input("Ingrese el valor de la latitud >  "))
    print(DD(Latitud,Longitud))

if(Seleccion=='2'):
    print("     Has seleccionado convertir GMS a DD     ")
    print("Ingrese primero los valores de longitud y despues los valores de latitud")
    Texto1 = ["Latitud", "Longitud"]
    Texto2 = ["Grados", "Minutos", "Segundos"]
    for i in range(2):
        for j in range(3):
            Text = "\nIngrese los " + Texto2[j] + " de la " + Texto1[i] 
            print(Text)
            if(i==0 and j==0):
                G1 = int(input())
            if(i==0 and j==1):
                M1 = int(input())
            if(i==0 and j==2):
                S1 = float(input())
            if(i==1 and j==0):
                G2 = int(input())
            if(i==1 and j==1):
                M2 = int(input())
            if(i==1 and j==2):
                S2 = float(input())
    print(DMS(G1,M1,S1,G2,M2,S2))
    