balance=0
print ('Enter transactions')
while True:

  s=input()
  if not s:
      break

  data=s.split(' ')
  Type=data[0]
  amt=int(data[1])
  if Type=='D':
    balance+=amt
  elif Type=='W':
    balance-=amt
  else:
    pass
  print('Your Current Balance is : ',balance) 
