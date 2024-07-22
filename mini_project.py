'''
project

continous program- while True
1. create contact
2. display contacts
3.search by name
4. search by mobile
5.update a contact
6. delete contact
7. exit

enter your choice:

'''

def createcontact():
    n= input("Enter Name: ")
    cn=n.capitalize()
    m= input("Enter Mobile Number: ")
    data=cn + "-" + m+"\n"
    print("Your data is saved to the new file")

    fp=open('con_mini_project.txt','a')
    fp.write(data)
    fp.close()

    #open file,write mode,enter detail,save
    pass
def displaycontact():
    fp=open('con_mini_project.txt','r')
    #d=fp.read()
    #d=fp.readline()
    d=fp.readlines()
    #print(d)

    for x in d:
        #print(x)
        l = x.split("-")
        print('name: ',l[0])
        print('mob number: ',l[1])
        #open file,read mode,display
    pass
def search_by_name():
    ns=input("Enter name to be searched: ")
    cns=ns.capitalize()
    fp=open('con_mini_project.txt','r')
    d=fp.readlines()
    c=0
    for x in d:
        #print(x)
        mylist = x.split("-")
        if mylist[0] == cns:
            s=mylist[0]+" - "+mylist[1]
            c+=1
    if c==1:
        print("Your Searched Details is: ",s)
        
    pass

def search_by_number():
    nm=input("Enter mobile number to be searched: ")
    fp=open('con_mini_project.txt','r')
    d=fp.readlines()
    c=0
    for x in d:
        mylist = x.split("-")
        if mylist[1].strip()==nm:
            s=mylist[0]+" - "+mylist[1]
            c+=1
    if c==1:
        print("Your Searched Details is: ",s)
        
    pass

def updatecontact():
    while True:
        print("1.what need to be updated - name")
        print("2.what need to be updated - mobile")
        #print("3.main menu")
        
        ch1=input("Enter your choice what you want to update: ")
        if ch1=="1":
            upd=input("Enter previous name: ")
            capit_upname=upd.capitalize()
            fp=open('con_mini_project.txt','r+')
            d=fp.readlines()
            c=0
            lists=[]
            for x in d:
                mylist = x.split("-")
                if mylist[0].capitalize()==capit_upname:
                    newname=input("Enter new name:")
                    capitnewname = newname.capitalize()
                    
                    updated_name=mylist[0].replace(mylist[0],capitnewname)
                    update_total = updated_name+ "-" + mylist[1]
                    c+=1
                
                    x=x.replace(x,update_total)
                #print(x)
                lists.append(x)
                    
            if c==1:
                f=open('con_mini_project.txt','w')
                for alllist in lists:                    
                    f.write(alllist)
                f.close()
                print("Name is successfully replaced")    #john-7896541230
                
        elif ch1=='2':
            upm=input("Enter previous mobile: ")
            fp=open('con_mini_project.txt','r+')
            d=fp.readlines()
            #print(d)
            c=0
            lists=[]
            for i in d:
                mylist = i.split("-")
                
                if mylist[1].strip()==upm:                    
                    newmobile=input("Enter new mobile: ")
                    
                    updated_mobile=mylist[1].replace(mylist[1],newmobile)
                    update_total = mylist[0]+ "-" + updated_mobile
                    c+=1
                    i=i.replace(i,update_total)
                #print(x)
                lists.append(i)
                #print(lists)
            if c==1:
                f=open('con_mini_project.txt','w')
                for alllist in lists:                    
                    f.write(alllist)
                f.close()
                print("Mobile Number is successfully replaced")   #Ffff-8523697410
                
            
        else:
            pass
    pass
def deletecontact():    
    fp=open('con_mini_project.txt','r+')
    d=fp.readlines()    
    upd=input("Please enter the name of the contact you wish to remove: ")
    nv=upd.capitalize()
    c=0
    
    for i in d:
        mylist = i.split("-")        
        if nv == mylist[0]:
            delitem=""
            #print(d)
            #print(d.index(i))
            delitem=d.index(i)
            c+=1
            d.pop(delitem)
    if c==1:
        f=open('con_mini_project.txt','w')
        for alllist in d:                    
            f.write(alllist)
        f.close()     
        print("This Details has now been removed")
        return d
    
    if c==0:
        print("Sorry, you have entered an invalid query.Please recheck and try again later.")
        return d
    pass
def menu():
    print("1. create contact")
    print("2. Display contact")
    print("3. search by name")
    print("4. search by mobile")
    print("5. Update contact")
    print("6. Delete contact")
    print("7. Exit") 
    ch=input("Enter your choice: ")
    return ch

ch = 1
while ch in (1, 2, 3, 4, 5, 6, 7):
    ch = menu()
    
    if ch=="1":
        createcontact()
    elif ch=="2":
        displaycontact()
    elif ch=="3":
        search_by_name()
    elif ch=="4":
        search_by_number()
    elif ch=="5":
        updatecontact()
    elif ch=="6":
        deletecontact()
    elif ch=="7":
        break
    else:
        #wrong choice
        pass
    print("---------------")




