from datetime import datetime

name=input("enter your name:")
print("Hii {} welcome to market".format(name))
lists='''
Rice  :20/kg
Sugar :40/kg
oil   :90/lit
paneer:50/pack
dall  :40/pack
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
items={'rice':20,'sugar':40,'oil':90,'panner':50,'dall':40}
take=int(input("For list of items press 1:"))
if take==1:
    print(lists)
while True:
    option=int(input(''' press 1 for Buy //   press 2 for Exit :'''))
    if option==2:
        break
    if option==1:
        item=input("Enter your item:")
        if item in items.keys():
            quant=int(input("Enter quantity:"))
            price=quant*items.get(item)
            pricelist.append((item,quant,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quant)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=totalprice+gst
        else:
            print("your entered item is not available")
    else:
       print("your entered input not matched .Please enter Again")
    inp=input("I can print the Bill yes or no :")
    if inp=="yes":
        pass
        if finalprice!=0:
            print(25*"=","DP Super Market","="*25)
            print(35*" ","Razole")
            print("Name:",name,45*" ","Date:",datetime.now())
            print("s_no",5*" ","Items",5*" ","Quantity",5*" ","Price")
            for i in range(len(pricelist)):
                print(i+1,5*" ",ilist[i],5*" ",qlist[i],5*" ",plist[i])
            print(60*"-")
            print(45*" ","Total Amount: Rs ",totalprice)
            print("GST amount",45*" "," Rs",gst)
            print(60*"-")
            print(45*" ","Final Amount: Rs ",finalprice)
            print(60*"-")
            print(25*"=","Thanks for visiting",25*"=")    


            
    