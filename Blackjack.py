raha=10
sentit=50
def blackjack():
    global uudelleen
    while True:
        blackjack1()
        if uudelleen!=1:
            return
def inventaario():
    print("ei mitään")


                
        
                
                
                
    
def blackjack1(): 
    global kortit,eirahaa,onpummi,deal6,uudelleen,dealer,deal5,pelaaja,ace1,ace2 ,ace3,ace4,teko,määrä,panos,sentit,raha
    ace1=0 
    pelaajavoitti=0
    uudelleen=0
    panos=0
    ace2=0
    ace3=0
    ace4=0
    pelaaja=0
    dealer=0 
    määrä=0
    onpummi=0
    eirahaa=0
    if raha == 0 and sentit == 0:
        print("sinulla ei ole rahaa")
        onpummi=1
        return
    print("alat pelaamaan")
    while True:
        teko=input("jatkatko: ")
        if teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
            print("selvä, poistutaan")
            return
        elif teko.lower() == "inventaario":
            inventaario()
        elif teko.lower() == "kyllä" or teko.lower() == "joo" or teko.lower() == "jatkan":
            print("jatkat pelaamista")
            break
        else:
            print("et voi tehdä tuota nyt")
    while True:
        while True:
            määrä = input("Kuinka monta senttiä haluat asettaa panokseksi: ")
            if määrä.isdigit():
                määrä=int(määrä)
                break
            else:
                print("Et voi tehdä tuota nyt")
        
            
        if sentit >= määrä:
            sentit-=määrä
            break
        elif raha*100+sentit<määrä:
            print("Sinulla ei ole tarpeeksi rahaa ")
        elif raha*100+sentit>=määrä:
            X=raha*100+sentit-määrä
            raha=X//100
            sentit=X%100
            break
        else:
            print("et voi tehdä tuota nyt")
    print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
    panos=määrä
            
    
    print("Pakkaa sekoitetaan...") 
    kortit = [1,2,3,4,5,6,7,8,9,10,10,10,10] 
    import random 
    deal=random.choice(kortit) 
    deal2=random.choice(kortit) 
    deal3=random.choice(kortit) 
    deal4=random.choice(kortit) 
    cards=[deal,deal2] 

    
    if 1 in cards:
        if deal == 1 and deal2 != 1:
            if 11+deal2 > 1+deal2:
                ace1=11 
            else:
                ace1=1 
            dealer=ace1+deal2 
        elif deal2==1 and deal != 1:
            if 11+deal > 1+deal:
                ace1=11
            else:
                ace1=1
            dealer=ace1+deal
        else: 
            ace1=1
            ace2=11 
            dealer=ace1+ace2
    else:
        dealer=deal+deal2
    
    Pcards = [deal3,deal4]
    if 1 in Pcards:
        if deal3 == 1 and deal4 != 1:
            if 11+deal4 > 1+deal4:
                ace3=11 
            else:
                ace3=1 
            pelaaja=ace3+deal4 
        elif deal4==1 and deal3 != 1:
            if 11+deal3 > 1+deal4:
                ace3=11
            else:
                ace3=1
            pelaaja=ace3+deal3
        else: 
            ace3=1
            ace4=11 
            pelaaja=ace3+ace4
    else:
        pelaaja=deal3+deal4
    if deal==1:
        deal="ässä"
    
    print("paljastetaan kortteja...")
    print()
    print("-----------------------------")
    print(f"Dealerin kortti on {deal}")
    print(f"Sinulla on {pelaaja}")
    print("-----------------------------")
    
    
    if dealer == 21:
        print("Dealer sai blackjackin, hävisit")
        while True:
            teko=input("Pelaatko uudelleen: ")
            if teko.lower() in ["kyllä","joo","pelaan"]:
                uudelleen=1
                return
            elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                print("poistutaan...")
                return
                
            elif teko.lower() == "inventaario":
                inventaario()
            else:
                print("et voi tehdä tuota nyt")
    
    
    if pelaaja == 21:
        print("Sait blackjackin, voitit")
        panos=panos*2.5
        raha+=panos//100
        sentit+=panos%100
        print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
        while True:
            teko=input("Pelaatko uudelleen: ")
            if teko.lower() in ["kyllä","joo","pelaan"]:
                uudelleen=1
                return
            elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                print("poistutaan...")
                return
                
            elif teko.lower() == "inventaario":
                inventaario()
            else:
                print("et voi tehdä tuota nyt")
        
    
    
    
    while True:        
        teko=input("Standäätkö,hittaatko vai doubleaatko: ")
        
        
        
        
        if teko.lower() in ["stand" , "ständään","jään","en tee mitään", "ei mitään","standaan","standään"]:
            print("paljastetaan kortteja...")
            print()
            print("-----------------------------")
            print(f"Dealerillä on {dealer}")
            print(f"Sinulla on {pelaaja}")
            print("-----------------------------")
            print()
            
            while dealer<16:
                deal5=0
                if deal=="ässä" or deal2=="ässän":
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    if dealer>21:
                        dealer-=10
                    print(f"dealerillä on nyt {dealer}")
                elif deal == "ässä" and deal2=="ässän":
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    if dealer>21:
                        dealer-=10
                    print(f"dealerillä on nyt {dealer}")
                else:    
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    print(f"dealerillä on nyt {dealer}")
            if dealer>21:
                print("Dealer bustasi")
                if pelaaja<22:
                    pelaajavoitti=1
            if dealer<=21 or pelaajavoitti == 1:
                if pelaaja>dealer or pelaajavoitti==1:
                    print("sinulla on parmmat kortit kuin dealerillä, voitit!!")
                    panos=panos*2
                    raha += panos//100
                    sentit += panos%100
                    print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                    while True:
                        teko=input("Pelaatko uudelleen: ")
                        if teko.lower() == "pelaan" or teko.lower() == "joo":
                            uudelleen=1
                            return
                        elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                            print("poistutaan...")
                            return
                            
                        elif teko.lower() == "inventaario":
                            inventaario()
                        else:
                            print("et voi tehdä tuota nyt")
                    
                elif pelaaja<dealer:
                    print("Dealer voitti")
                    while True:
                        teko=input("Pelaatko uudelleen: ")
                        if teko.lower() == "pelaan" or teko.lower() == "joo":
                            uudelleen=1
                            return
                        elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                            print("poistutaan...")
                            return
                            
                        elif teko.lower() == "inventaario":
                            inventaario()
                        else:
                            print("et voi tehdä tuota nyt")
            elif pelaaja == dealer:
                print("push, eli kukaan ei menetä mitään")
                raha += panos//100
                sentit += panos%100
                print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                while True:
                    teko=input("Pelaatko uudelleen: ")
                    if teko.lower() in ["kyllä","joo","pelaan"]:
                        uudelleen=1
                        return
                    elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                        print("poistutaan...")
                        return
                        
                    elif teko.lower() == "inventaario":
                        inventaario()
                    else:
                        print("et voi tehdä tuota nyt")
            break       
            
        
        
        
        
        
        elif teko.lower() in ["hittaan","hit","lisää","otan kortin", "hitään"]:
            while pelaaja<=21:
                deal6=random.choice(kortit)
                if deal6!="ässän":
                    deal6=int(deal6)
                if deal6 == "ässän":
                    if pelaaja <=10:
                        deal6=11
                    elif pelaaja>10:
                        deal6=1
                print(f"nostit {deal6}")
                pelaaja+=deal6
                print()
                print("-----------------------------")
                print(f"Dealerin kortti on {deal}")
                print(f"Sinulla on {pelaaja}")
                print("-----------------------------")
                print()
                
                teko=input("standäätkö, hittaatko vai doublaatko")
                
                if teko.lower() in ["stand" , "ständään","jään","en tee mitään", "ei mitään","standaan","standään"]:
                    while dealer<16:
                        deal5=0
                        if deal=="ässä" or deal2=="ässän":
                            print("Dealer nostaa kortin...")
                            deal5=random.choice(kortit)
                            if deal5!="ässän":
                                deal5=int(deal5)
                            print(f"Dealer nosti {deal5}")
                            if deal5 == "ässän":
                                if dealer <=10:
                                    deal5=11
                                elif dealer>10:
                                    deal5=1
                            dealer+=deal5
                            if dealer>21:
                                dealer-=10
                            print(f"dealerillä on nyt {dealer}")
                        elif deal == "ässä" and deal2=="ässän":
                            print("Dealer nostaa kortin...")
                            deal5=random.choice(kortit)
                            if deal5!="ässän":
                                deal5=int(deal5)
                            print(f"Dealer nosti {deal5}")
                            if deal5 == "ässän":
                                if dealer <=10:
                                    deal5=11
                                elif dealer>10:
                                    deal5=1
                            dealer+=deal5
                            if dealer>21:
                                dealer-=10
                            print(f"dealerillä on nyt {dealer}")
                        else:    
                            print("Dealer nostaa kortin...")
                            deal5=random.choice(kortit)
                            if deal5!="ässän":
                                deal5=int(deal5)
                            print(f"Dealer nosti {deal5}")
                            if deal5 == "ässän":
                                if dealer <=10:
                                    deal5=11
                                elif dealer>10:
                                    deal5=1
                            dealer+=deal5
                            print(f"dealerillä on nyt {dealer}")
                    if dealer>21:
                        print("Dealer bustasi")
                        if pelaaja<22:
                            pelaajavoitti=1
                    if dealer<=21 or pelaajavoitti==1:
                        if pelaaja>dealer or pelaajavoitti == 1:
                            print("sinulla on paremmat kortit kuin dealerillä, voitit!!")
                            panos=panos*2
                            raha += panos//100
                            sentit += panos%100
                            print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                            while True:
                                teko=input("Pelaatko uudelleen: ")
                                if teko.lower() == "pelaan" or teko.lower() == "joo":
                                    uudelleen=1
                                    return
                                elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                                    print("poistutaan...")
                                    return
                                    
                                elif teko.lower() == "inventaario":
                                    inventaario()
                                else:
                                    print("et voi tehdä tuota nyt")
                            
                        elif pelaaja<dealer:
                            print("Dealer voitti")
                            while True:
                                teko=input("Pelaatko uudelleen: ")
                                if teko.lower() == "pelaan" or teko.lower() == "joo":
                                    uudelleen=1
                                    return
                                elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                                    print("poistutaan...")
                                    return
                                    
                                elif teko.lower() == "inventaario":
                                    inventaario()
                                else:
                                    print("et voi tehdä tuota nyt")
                    elif pelaaja == dealer:
                        print("push, eli kukaan ei menetä mitään")
                        raha += panos//100
                        sentit += panos%100
                        print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                        while True:
                            teko=input("Pelaatko uudelleen: ")
                            if teko.lower() in ["kyllä","joo","pelaan"]:
                                uudelleen=1
                                return
                            elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                                print("poistutaan...")
                                return
                                
                            elif teko.lower() == "inventaario":
                                inventaario()
                            else:
                                print("et voi tehdä tuota nyt")
                    break
                
                elif teko.lower() in ["double","double down","doublaan","doublään"]:
                    while True:
                        if sentit >= määrä:
                            sentit-=määrä
                            break
                        elif raha*100+sentit<määrä:
                            print("Sinulla ei ole tarpeeksi rahaa ")
                            eirahaa=1
                        elif raha*100+sentit>määrä:
                            X=raha*100+sentit-määrä
                            raha=X//100
                            sentit=X%100
                            break
                        else:
                            print("et voi tehdä tuota nyt")
                    if eirahaa==1:
                        return
                    print("tuplaat panoksesi ja nostat kortin")
                    print("nostetaan korttia...")
                    print()
                    panos=panos*2
                    deal6=random.choice(kortit)
                    if deal6!="ässän":
                        deal6=int(deal6)
                    if deal6 == "ässän":
                        if pelaaja <=10:
                            deal6=11
                        elif pelaaja>10:
                            deal6=1
                    print(f"nostit {deal6}")
                    pelaaja+=deal6
                    
                    print("paljastetaan kortteja...")
                    
                    print("-----------------------------")
                    print(f"Dealerillä on {dealer}")
                    print(f"Sinulla on {pelaaja}")
                    print("-----------------------------")
                    print()
                    
                    while dealer<16:
                        deal5=0
                        if deal=="ässä" or deal2=="ässän":
                            print("Dealer nostaa kortin...")
                            deal5=random.choice(kortit)
                            if deal5!="ässän":
                                deal5=int(deal5)
                            print(f"Dealer nosti {deal5}")
                            if deal5 == "ässän":
                                if dealer <=10:
                                    deal5=11
                                elif dealer>10:
                                    deal5=1
                            dealer+=deal5
                            if dealer>21:
                                dealer-=10
                            print(f"dealerillä on nyt {dealer}")
                        elif deal == "ässä" and deal2=="ässän":
                            print("Dealer nostaa kortin...")
                            deal5=random.choice(kortit)
                            if deal5!="ässän":
                                deal5=int(deal5)
                            print(f"Dealer nosti {deal5}")
                            if deal5 == "ässän":
                                if dealer <=10:
                                    deal5=11
                                elif dealer>10:
                                    deal5=1
                            dealer+=deal5
                            if dealer>21:
                                dealer-=10
                            print(f"dealerillä on nyt {dealer}")
                        else:    
                            print("Dealer nostaa kortin...")
                            deal5=random.choice(kortit)
                            if deal5!="ässän":
                                deal5=int(deal5)
                            print(f"Dealer nosti {deal5}")
                            if deal5 == "ässän":
                                if dealer <=10:
                                    deal5=11
                                elif dealer>10:
                                    deal5=1
                            dealer+=deal5
                            print(f"dealerillä on nyt {dealer}")
                        
                        
                    if dealer>21:
                        print("Dealer bustasi")
                        if pelaaja<22:
                            pelaajavoitti=1
                    if dealer<=21 or pelaajavoitti==1:
                        if pelaaja>dealer or pelaajavoitti==1:
                            print("voitit dealerin kortit!!")
                            panos=panos*2
                            raha += panos//100
                            sentit += panos%100
                            print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                            while True:
                                teko=input("Pelaatko uudelleen: ")
                                if teko.lower() in ["kyllä","joo","pelaan"]:
                                    uudelleen=1
                                    return
                                elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                                    print("poistutaan...")
                                    return
                                    
                                elif teko.lower() == "inventaario":
                                    inventaario()
                                else:
                                    print("et voi tehdä tuota nyt")
                            
                        elif pelaaja<dealer:
                            print("Dealer voitti")
                            print(f"menetit panoksen ja sinulla on nyt {raha} euroa ja {sentit} senttiä")
                            while True:
                                teko=input("Pelaatko uudelleen: ")
                                if teko.lower() in ["kyllä","joo","pelaan"]:
                                    uudelleen=1
                                    return
                                elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                                    print("poistutaan...")
                                    return
                                    
                                elif teko.lower() == "inventaario":
                                    inventaario()
                                else:
                                    print("et voi tehdä tuota nyt")
                    elif pelaaja == dealer:
                        print("push, eli kukaan ei menetä mitään")
                        raha += panos//100
                        sentit += panos%100
                        print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                        while True:
                            teko=input("Pelaatko uudelleen: ")
                            if teko.lower() in ["kyllä","joo","pelaan"]:
                                uudelleen=1
                                return
                            elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                                print("poistutaan...")
                                return
                                
                            elif teko.lower() == "inventaario":
                                inventaario()
                            else:
                                print("et voi tehdä tuota nyt")
                    break
                    
                elif teko.lower() in ["hittaan","hit","lisää","otan kortin", "hitään"]:
                    continue
                
                
                
            
        
        
        
            while dealer<16:
                deal5=0
                if deal=="ässä" or deal2=="ässän":
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    if dealer>21:
                        dealer-=10
                    print(f"dealerillä on nyt {dealer}")
                elif deal == "ässä" and deal2=="ässän":
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    if dealer>21:
                        dealer-=10
                    print(f"dealerillä on nyt {dealer}")
                else:    
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    print(f"dealerillä on nyt {dealer}")
                
                
            if dealer>21:
                print("Dealer bustasi")
                if pelaaja<22:
                    pelaajavoitti=1
            if dealer<=21 or pelaajavoitti == 1:
                if pelaaja>dealer or  pelaajavoitti==1:
                    print("voitit dealerin kortit!!")
                    panos=panos*2
                    raha += panos//100
                    sentit += panos%100
                    print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                    while True:
                        teko=input("Pelaatko uudelleen: ")
                        if teko.lower() in ["kyllä","joo","pelaan"]:
                            uudelleen=1
                            return
                        elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                            print("poistutaan...")
                            return
                            
                        elif teko.lower() == "inventaario":
                            inventaario()
                        else:
                            print("et voi tehdä tuota nyt")
                    
                elif pelaaja<dealer:
                    print("Dealer voitti")
                    print(f"menetit panoksen ja sinulla on nyt {raha} euroa ja {sentit} senttiä")
                    while True:
                        teko=input("Pelaatko uudelleen: ")
                        if teko.lower() in ["kyllä","joo","pelaan"]:
                            uudelleen=1
                            return
                        elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                            print("poistutaan...")
                            return
                            
                        elif teko.lower() == "inventaario":
                            inventaario()
                        else:
                            print("et voi tehdä tuota nyt")
            elif pelaaja == dealer:
                print("push, eli kukaan ei menetä mitään")
                raha += panos//100
                sentit += panos%100
                print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                while True:
                    teko=input("Pelaatko uudelleen: ")
                    if teko.lower() in ["kyllä","joo","pelaan"]:
                        uudelleen=1
                        return
                    elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                        print("poistutaan...")
                        return
                        
                    elif teko.lower() == "inventaario":
                        inventaario()
                    else:
                        print("et voi tehdä tuota nyt")
            break
        
        
        
        
        
        
        
        
        elif teko.lower() in ["double","double down","doublaan","doublään"]:
            while True:
                if sentit >= määrä:
                    sentit-=määrä
                    break
                elif raha*100+sentit<määrä:
                    print("Sinulla ei ole tarpeeksi rahaa ")
                    eirahaa=1
                elif raha*100+sentit>määrä:
                    X=raha*100+sentit-määrä
                    raha=X//100
                    sentit=X%100
                    break
                else:
                    print("et voi tehdä tuota nyt")
            if eirahaa==1:
                continue
            print("tuplaat panoksesi ja nostat kortin")
            print("nostetaan korttia...")
            print()
            panos=panos*2
            deal6=random.choice(kortit)
            if deal6!="ässän":
                deal6=int(deal6)
            if deal6 == "ässän":
                if pelaaja <=10:
                    deal6=11
                elif pelaaja>10:
                    deal6=1
            print(f"nostit {deal6}")
            pelaaja+=deal6
            
            print("paljastetaan kortteja...")
            
            print("-----------------------------")
            print(f"Dealerillä on {dealer}")
            print(f"Sinulla on {pelaaja}")
            print("-----------------------------")
            print()
            
            while dealer<16:
                deal5=0
                if deal=="ässä" or deal2=="ässän":
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    if dealer>21:
                        dealer-=10
                    print(f"dealerillä on nyt {dealer}")
                elif deal == "ässä" and deal2=="ässän":
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    if dealer>21:
                        dealer-=10
                    print(f"dealerillä on nyt {dealer}")
                else:    
                    print("Dealer nostaa kortin...")
                    deal5=random.choice(kortit)
                    if deal5!="ässän":
                        deal5=int(deal5)
                    print(f"Dealer nosti {deal5}")
                    if deal5 == "ässän":
                        if dealer <=10:
                            deal5=11
                        elif dealer>10:
                            deal5=1
                    dealer+=deal5
                    print(f"dealerillä on nyt {dealer}")
                
                
            if dealer>21:
                print("Dealer bustasi")
                if pelaaja<22:
                    pelaajavoitti=1
            if dealer<=21 or pelaajavoitti ==1:
                if pelaaja>dealer or pelaajavoitti==1:
                    print("voitit dealerin kortit!!")
                    panos=panos*2
                    raha += panos//100
                    sentit += panos%100
                    print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                    while True:
                        teko=input("Pelaatko uudelleen: ")
                        if teko.lower() in ["kyllä","joo","pelaan"]:
                            uudelleen=1
                            return
                        elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                            print("poistutaan...")
                            return
                            
                        elif teko.lower() == "inventaario":
                            inventaario()
                        else:
                            print("et voi tehdä tuota nyt")
                    
                elif pelaaja<dealer:
                    print("Dealer voitti")
                    print(f"menetit panoksen ja sinulla on nyt {raha} euroa ja {sentit} senttiä")
                    while True:
                        teko=input("Pelaatko uudelleen: ")
                        if teko.lower() in ["kyllä","joo","pelaan"]:
                            uudelleen=1
                            return
                        elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                            print("poistutaan...")
                            return
                            
                        elif teko.lower() == "inventaario":
                            inventaario()
                        else:
                            print("et voi tehdä tuota nyt")
            elif pelaaja == dealer:
                print("push, eli kukaan ei menetä mitään")
                raha += panos//100
                sentit += panos%100
                print(f"Sinulla on nyt {raha} euroa ja {sentit} senttiä")
                while True:
                    teko=input("Pelaatko uudelleen: ")
                    if teko.lower() in ["kyllä","joo","pelaan"]:
                        uudelleen=1
                        return
                    elif teko.lower() == "en" or teko.lower() == "poistu" or teko.lower() == "sulje":
                        print("poistutaan...")
                        return
                        
                    elif teko.lower() == "inventaario":
                        inventaario()
                    else:
                        print("et voi tehdä tuota nyt")
            break
print(f"Sinulla on {raha} euroa ja {sentit} senttiä")
blackjack()
print(f"sinulle jäi {raha} euroa ja {sentit} senttiä")
print("kiitos kun pelasit...")
