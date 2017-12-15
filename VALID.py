from math import pi

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def OKP(n): #ESTA FUNCION ES COMO "OK" SOLO QUE ADMITE EL NÚMERO "pi".
    if n!=("pi"):
        try:
            n=float(n)
        except:
            n=OKP(input("Caracter no válido: "))
    else:
        n=pi
    return n

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n


def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def ER(n):#SE PUEDE RESUMIR/MEJORAR
    strn=str(n)
    lstrn=len(strn)
    if ("-") in strn:#AQUI SE TIENE EN CUENTA LA POSIBILIDAD DE LOS NUMEROS NEGATIVOS
        lstrn=len(strn)-1
        
    if lstrn>=4 and lstrn<=18:
        if lstrn>=4 and lstrn<=6:
            res=("mil"+str(lstrn-3))
        if lstrn>=7 and lstrn<=9:
            res=("millon"+str(lstrn-6))
        if lstrn>=10 and lstrn<=12:
            res=("mil millon"+str(lstrn-9))
        if lstrn>=13 and lstrn<=15:
            res=("billon"+str(lstrn-12))
        if lstrn>=16 and lstrn<=18:
            res=("trillon"+str(lstrn-15))
        return("("+res+")")
    else:
        return("")

def oop(string):
    try:
        n=eval(string)
    except:
        n=oop(input("Operación no válida: "))
    return n

def binn(n):
    num=n
    restos=[]
    while num>1:
        res=int(num%2)#PARA QUE EL RESTO SALGA SIN DECIMALES
        restos.append(str(res))#PARA QUE RES SE AÑADA A LA LISTA EN FORMATO "str".
        num=int(num/2)
    stri=str(num)
    nv=restos[::-1]
    j=("").join(nv)
    sf=stri+j
    return sf



def oper(ress):#SE PUEDE USAR EN "calculadora_cadena.py"
    operr=[]
    for i in (ress):
        if ord(i)<48 or ord(i)>57:
            operr.append(i)
            break
    if len(operr)==0:
        ress=oper(str(input("Introduce al menos un operador: ")))
    try:
        n=eval(ress)
    except:
        ress=oper(str(input("Operación no válida: ")))
    return ress

        

