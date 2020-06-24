print('The Invoice Program')

cust=input('Enter Customer Type(r/w):')
inv=float(input('Enter The Invoice Rate:'))


if cust.lower()== "r":
      if inv>0 and inv<100:
          discount=0
      elif inv>100 and inv<200:
          discount=.1
      elif inv>200 and inv<500:
          discount=.2
      elif inv>500:
          discount=.25
elif(cust.lower()== "w"):
      if inv>0 and inv<500:
          discount=.4
      elif inv>500:
          discount=.5
else :
      discount=0


discount_amt =float(inv*discount)
invoice=inv-round(discount_amt,2)
print ('The Discount Percentage:',discount)
print('The Discount Amount is:',discount_amt)
print('The Total:',invoice)
