import datetime
ev = datetime.datetime.now().year
while True:
        try:
            szül = int(input("melyik évben születtél? "))
            kor = ev-szül
            if kor < 0 :
                print("Kérlek add meg a valódi születési évedet!")
            else:
                print("Ennyi éves vagy: ",kor)
                break
        except:
            print("Kérlek adj meg számot!")    
            
