from math import *
import subprocess

def OKP(n): #ESTA FUNCION ES COMO "OK" SOLO QUE ADMITE EL NÚMERO "pi".
    from math import pi
    if n!=("pi"):
        try:
            n=float(n)
        except:
            n=OKP(input("Caracter no válido: "))
    else:
        n=pi
    return n


def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n


def opera_val(op,p):
    if p==("A"):
        operadores=["+","-","*","log","/","ln","R",")","exp/","exp*","exp-","exp+","exp","sqrt","sqrt+","sqrt-","sqrt*","sqrt/"]
        #while op!=("+") and op!=("-") and op!=("*") and op!=("log") and op!=("/") and op!=("ln") and op!=("R") and op!=(")") and op!=("exp/") and op!=("exp*") and op!=("exp-") and op!=("exp+") and op!=("exp") and op!=("sqrt") and op!=("sqrt+") and op!=("sqrt-") and op!=("sqrt*") and op!=("sqrt/"):
        while op not in operadores:
            op=input("Introduce un operador de la \'TABLA DE OPERADORES\': ")
    else:
        operadores=["+(","-(","*(","/(","/","log","+","-","*","sqrt","exp","C","R","=","sin","cos","tan","ln","exp+","exp-","exp*","exp/","sqrt+","sqrt-","sqrt*","sqrt/"]
        #while op!=("+(") and op!=("-(") and op!=("*(") and op!=("/(") and op!=("/") and op!=("log") and op!=("+") and op!=("-") and op!=("*") and op!=("sqrt") and op!=("exp") and op!=("C") and op!=("R") and op!=("=") and op!=("sin") and op!=("cos") and op!=("tan") and op!=("ln") and op!=("exp+") and op!=("exp-") and op!=("exp*") and op!=("exp/") and op!=("sqrt+") and op!=("sqrt-") and op!=("sqrt*") and op!=("sqrt/"):
        while op not in operadores:
            op=input("Introduce un operador válido: ")
    return op

def num(n):
    if n!=("pi"):
        n=OKP(n)
    else:
        n=pi
    return n
        
def exponent(o,VALOR):
    base=OKP(input("Indicar la base: "))
    while base==0 and o==("exp/"):
        base=OKP(input("ERROR:Nose puede dividir por 0, prueba con otro número: "))
    expo=OKP(input("Indicar exponente: "))
    resul=pow(base,expo) #"pow" ES OTRO MODO PARA ELEVAR A UNA POTENCIA (pow(n,n1)=n**n1).
    if o==("exp+"):
        VALOR+=resul
    if o==("exp-"):
        VALOR-=resul
    if o==("exp*"):
        VALOR*=resul
    if o==("exp/"):
        VALOR/=resul
    return VALOR

def exponent2(o,VALOR):
    resul=sqrt(OKP(input("Indicar número: ")))
    while resul==0 and o==("sqrt/"):
        resul=sqrt(OKP(input("ERROR:No se puede dividir por 0, prueba con otro número: ")))
    if o==("sqrt+"):
        VALOR+=resul
    if o==("sqrt-"):
        VALOR-=resul
    if o==("sqrt*"):
        VALOR*=resul
    if o==("sqrt/"):
        VALOR/=resul
    return VALOR
        
#TABLA DE OPERADORES
while True:
    print("CALCULADORA BASICA")
    print("")
    print("""*******************TABLA DE OPERADORES********************
**********************************************************
OPERACION SUMA                             OPERADOR("+")
OPERACION RESTA                            OPERADOR("-")
OPERACION MULTIPLICACION                   OPERADOR("*")
OPERACION DIVISION                         OPERADOR("/")
RAIZ CUADRADA                              OPERADOR("sqrt")
EXPONENCIACION                             OPERADOR("exp")
CALCULO SENO                               OPERADOR("sin")
CALCULO COSENO                             OPERADOR("cos")
CALCULO TANGENTE                           OPERADOR("tan")
LOGARITMO                                  OPERADOR("log")
LOGARITMO NATURAL                          OPERADOR("ln")
REDONDEAR CIFRA                            OPERADOR("R")
NUMERO "PI"                                OPERADOR("pi")
HACER VALOR IGUAL A 0                      OPERADOR("C")
ABRIR PARENTESIS                           OPERADOR("(")
CERRAR PARENTESIS                          OPERADOR(")")
VISUALIZAR RESULTADO                       OPERADOR("=")
**********************************************************
**********************************************************
""")

    r=ns(input("¿Desea ir visualizando los resultados según se generan?: "))
    VALOR=OKP(input("Introduce número: "))
    if r==("s"):
        print(VALOR)
    o=opera_val(input("Introduce operador: "),"B")
    while o!=("="):
        if o==("sqrt"):
            VALOR=sqrt(VALOR)
            if r==("s"):
                print(VALOR)
        if o==("+"):
            n=OKP(input("Introduce número: "))
            VALOR+=n
            if r==("s"):
                print(VALOR)
        if o==("-"):
            n=OKP(input("Introduce número: "))
            VALOR-=n
            if r==("s"):
                print(VALOR)
        if o==("*"):
            n=OKP(input("Introduce número: "))
            VALOR*=n
            if r==("s"):
                print(VALOR)
        if o==("/"):
            n=OKP(input("Introduce número: "))
            while n==0:
                n=OKP(input("ERROR:No se puede dividir por 0, prueba con otro número: "))
            VALOR/=n
            if r==("s"):
                print(VALOR)
        if o==("exp"):
            n=OKP(input("Indicar valor del exponente: "))
            try:
                VALOR**=n
            except:
                print("Operación no soportada")
            if r==("s"):
                print(VALOR)
        if o==("sin"):
            VALOR=sin(VALOR)
            if r==("s"):
                print(VALOR)
        if o==("cos"):
            VALOR=cos(VALOR)
            if r==("s"):
                print(VALOR)
        if o==("tan"):
            VALOR=tan(VALOR)
            if r==("s"):
                print(VALOR)
        if o==("ln"):
            VALOR=log(VALOR)
            if r==("s"):
                print(VALOR)
        if o==("log"):
            base=OKP(input("Indique la base del logaritmo: "))
            VALOR=log(VALOR)/log(base)
            if r==("s"):
                print(VALOR)
        if o==("exp+") or o==("exp-") or o==("exp*") or o==("exp/"):
            VALOR=exponent(o,VALOR)
            if r==("s"):
                print(VALOR)
        if o==("sqrt+") or o==("sqrt-") or o==("sqrt*") or o==("sqrt/"):
            VALOR=exponent2(o,VALOR)
            if r==("s"):
                print(VALOR)
        if ("(") in o:
            VAL=OKP(input("Introduce número: "))
            operad=opera_val(input("Introduce operador: "),"A")
            while operad!=(")"):
                if operad==("+"):
                    n=OKP(input("Introduce número: "))
                    VAL+=n
                if operad==("-"):
                    n=OKP(input("Introduce número: "))
                    VAL-=n
                if operad==("*"):
                    n=OKP(input("Introduce número: "))
                    VAL*=n
                if operad==("R"):
                    VAL=round(VAL)
                if operad==("log"):
                    base=OKP(input("Indique la base del logaritmo: "))
                    VAL=log(VAL)/log(base)
                if operad==("ln"):
                    VAL=log(VAL)
                if operad==("sqrt+") or operad==("sqrt-") or operad==("sqrt*") or operad==("sqrt/"):
                    VAL=exponent2(operad,VAL)#REVISAR
                if operad==("sqrt"):
                    VAL=sqrt(VAL)
                if operad==("/"):
                    n=OKP(input("Introduce número: "))
                    while n==0:
                        n=OKP(input("ERROR:No se puede dividir por 0, prueba con otro número: "))
                    VAL/=n
                if operad==("exp+") or operad==("exp-") or operad==("exp*") or operad==("exp/"):
                    VAL=exponent(operad,VAL)#REVISAR
                if operad==("exp"):
                    expo=OKP(input("Introduce el exponente: "))
                    VAL=VAL**expo
                operad=opera_val(input("Introduce operador: "),"A")
            if ("+") in o:
                VALOR+=VAL
            if ("-") in o:
                VALOR-=VAL
            if ("*") in o:
                VALOR*=VAL
            if ("/") in o:
                if VAL!=0:
                    VALOR/=VAL
                else:
                    print("ERROR:La operación entre parantesis no se ha efectuado ya que no es posible dividir por 0")
                    VALOR/=1
            if r==("s"):
                print(VALOR)
        if o==("R"):
            VALOR=round(VALOR)
            if r==("s"):
                print(VALOR)
        if o==("C"):
            VALOR=0
            if r==("s"):#CONVIENE ELIMINAR ESTA DUPLICIDAD
                print(VALOR)
            VALOR=OKP(input("Introduce número: "))
            if r==("s"):
                print(VALOR)
    
        o=opera_val(input("Introduce operador: "),"B")
    print("RESULTADO FINAL: ",VALOR)
    continu=ns(input("¿Desea efectuar mas operaciones?: "))
    if continu==("n"):
        break
    else:
        subprocess.call(["cmd.exe","/C","cls"])
