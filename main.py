from LQ import*
from listor import*


class Syntaxerror(Exception):
    pass
class Klar(Exception):
    pass

def Syntaxen(molekyl):
    try:
        try:
            syntax=delaupp(molekyl)
            readformel(syntax)
        except Klar as fel:
            return str(fel)
    except Syntaxerror as fel:
        return str(fel)

def delaupp(ordet):
    w=list(ordet)
    q=LinkedQ()
    for z in w:
        q.enqueue(z)
    q.enqueue("\n")
    return q

def readformel(q):
    readmol(q)
    empty = q.isEmpty()
    if empty is False:
        nästa=q.peek()
        if nästa=="\n":
            raise Klar("Formeln är syntaktiskt korrekt")
        elif nästa==")":
            readmol(q)
        else:
            raise Klar("Formeln är syntaktiskt korrekt")
    else: 
        pass

def readmol(q): 
    readgroup(q)
    nästa=q.peek()
    if nästa == "\n":
        return
    elif nästa == ")":
        return
    readmol(q)


def readgroup(q):
    första=q.peek()
    if första =="(":
        q.dequeue()
        readmol(q)
        andra=q.peek()
        if andra!=")":
            f=write(q)
            raise Syntaxerror("Saknad högerparentes vid radslutet "+f)
        if andra==")":
            q.dequeue()
            tredje=q.peek()
            if siffra(tredje) is True:
                readnum(q)
                return
            else:
                f=write(q)
                raise Syntaxerror("Saknad siffra vid radslutet "+f)
    else:
        readatom(q)
    empty=q.isEmpty()
    if empty is False:
        readnum(q)

def readnum(q):
    första=q.peek()
    if siffra(första) is True:
        if första in siffror:
            if första== siffror[0]:
                q.dequeue()
                f=write(q)
                raise Syntaxerror("För litet tal vid radslutet "+f)
            if första == siffror[1]:
                q.dequeue()
                andra=q.peek()
                if siffra(andra) is True:
                    tal=första+andra
                else:
                    f=write(q)
                    raise Syntaxerror("För litet tal vid radslutet "+f)
        q.dequeue()
        morenum(q)

def morenum(q):
    while siffra(q.peek()) is True:
        q.dequeue()
    if q.isEmpty():
        return

def readatom(q):
    första=q.peek()
    if StorB(första) is True:
        q.dequeue()
        empty=q.isEmpty()
        if empty is False and LitenB(q.peek()) is True:
            andra=q.dequeue()
            första+=andra
    elif LitenB(första) is True:
        f=write(q)
        raise Syntaxerror("Saknad stor bokstav vid radslutet "+f)
    else:
        f=write(q)
        raise Syntaxerror("Felaktig gruppstart vid radslutet "+f)

    if första in Atomerlista:
        return True
    else:
        f=write(q)
        raise Syntaxerror("Okänd atom vid radslutet "+f)

def write(q):
    str1=""
    while q.isEmpty() is False:
        x=q.dequeue()
        if x == "\n":
            break
        else:
            str1=str1+x
    return str1

def StorB(bokstav):
    if bokstav in storaA:
        return True
    else:
        return False
def LitenB(bokstav):
    if bokstav in lillaA:
        return True
    else:
        return False
def siffra(x):
    if x in siffror:
        return True
    else:
        return False



#applicering för kattis med while loop och # 
def main():
    while True:
        molekyl = input("")
        if '#' in molekyl:
            return False
        else:
            resultat=Syntaxen(molekyl)
            print(resultat)

main()