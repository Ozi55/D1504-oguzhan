#!/usr/bin/env python
# coding: utf-8

# In[11]:


num1= float(input("Lutfen bir sayi giriniz"))
num2= float(input("Lutfen bir sayi giriniz"))
num3= float(input("Lutfen bir sayi giriniz"))
if num1>num2 and num1>num3 :
    largest=num1
    print("the largest number is:",largest)
    
elif  num2>num1 and num2>num3 :
    largest=num2
    print("the largest number is:",largest)
    
else :
    largest=num3
    print("the largest number is :",largest)
    
        
        
        


# In[16]:


score=int(input("Enter Your Score"))

if score >= 90 :
    if score >= 95 :
        score_letter="A+"
    else:
            score_letter = "A"

elif score >= 80 :
    if score >= 85 :
        
        score_letter = "B+"
    else :
            score_letter = "B"
            
else:
    score_letter = "B-"
    
    
print("Your degree is :",score_letter)
    
    


# In[18]:


age = input("enter your age please :")

while not age.isdigit():
    print("you entered incorrect(sayi girmen lazim)")
    age= input ("enter your age(sayiyla yaz sayiyla)")
    print("aferin dogru girdin!",age)


# In[ ]:



while True :
    number = int(input("sayi gir :"))
    plaka = 55
if  number < plaka :  

        print("dusuk yazdin biraz daha buyuk bir sayi dene") 
elif  number > plaka :
        print("fazla yazdin daha dusuk bir sayi dene")
else:      
        print("aferin plakayi tutturdun")
        
        break
        
        
            


# In[7]:


list1=[]

for i in range (1,6):
    list1 +=[i]

print(list1)








# In[31]:


x = input("kelime yaz:")
for i in x:
    print(i,end = "-")

    
    
    


# In[34]:


test = [(1,2),(3,4),(5,6)]
for i, j in test :
     print(test)
    


# In[42]:


test = [1,2,3,4]
for i in test :
     print(i)


# In[51]:


number=int(input("bir sayi giriniz"))
for i in range (11):
    print(number, "x", i, "=",i*number)


# In[57]:


count = 0
for i in range(1,10):
    count +=1
    print(i*str(count))


# In[91]:


evens=[]
odds=[]
for i in range(10):
    if i % 2 == 1:
        odds.append(i)
    else:
            evens.append(i)
            print(evens)
            print(odds)
    
    
    


# In[ ]:


count=0

for i in range(75):
    
     count+=i
    
     print(count)


# In[10]:


names = ["susan","tom","edward"]


mood= [ "happy","sad"]

for i in names:
    for ii in mood:
        print(i + " " +  "is" +" "  +ii)
        
        
        
       
       


# In[21]:


v= ("five",5,True)


# In[22]:


v


# In[23]:


v=(x,y,z)


# In[24]:


x


# In[27]:


p=(1,2,3)


# In[28]:


p


# In[31]:


p=("u","y","o")


# In[34]:


"u"


# In[36]:


(m,t,s,w)=tuple(range(1,5))


# In[41]:





# In[47]:


x,y,*_,t= (11,22,33,44,55,66,77)


# In[50]:


_


# # List Comprehension
# {expression for otem in iterable}
# 
# for item in iterable :
#      expression
#      

# In[55]:


sayilar = []
for i in range(5):
    sayilar.append(i)
    
sayilar


# In[58]:


[i for i in range(5)]


# In[59]:


[i**2 for i in range(1,10)]


# In[ ]:





# In[86]:


my_list=[1,2,3,4,5,6]
[i**2 for i in my_list if i % 2 ==1]
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




