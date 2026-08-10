'''
#table
tab_ = int(input('enter a num:'))
for j in range (1,11):
    print (f'{tab_} x {j} = {tab_*j}')

#Amstrong number
num=156    
length_ =len(str(num))
am_= 0
for j in str(num):
     am_= int(j) ** length_+am_
if am_ == num:
     print (f' {num} is Amstrong')
else:
      print( f' {num} is not')

      
#febinocci number
limit_ = input(input('enter limit: '))
num = 0
num_2 = 1
print(num,num_2,end='')
for j in range(1,limit+1):
    all_add=num + num_2
    num = num_2
    num_2 = all_ad
    print(all_ad,end=' ')

#CALCULATOR
num_1  = int(input('enter a num: '))
num_2  = int(input('enter a num: '))
opt_ = int(input('enter \n1.add \n2.sub: '))
if opt_ == 1:
    print(num_1 + num_2)
elif opt_ == 2:
    print(num_1 - num_2)
elif opt_ == 3:
    print(num_1 + num_2)
    

'''
#ATM
SBI_Rama = {'name':'Rama',
            'Adr': "799349488116",
            'pan': 'pra4567shu',
            'ATM PIN':'2005',
            'Balance': '3500',
            'transcations history':[]}
remain_A = 3
while remain_A >0:
    pin_ = input("Enter your 4 digit pin: ")
    if len(pin_) == 4:
        if pin_ in SBI_Rama['ATM PIN']:
            opt_ = int(input( 'Enter \n1.withdraw \n2.Balance \n3.deposit \n4.transcations : '))
            if opt_ == 1:
                withdraw_m = int(input('enter amount you want to withdraw: '))
                if withdraw_m <= SBI_Rama['Balance'] and withdraw_m % 100 ==0:
                   SBI_Rama['Balance'] -= withdraw_m
                   print(f'you have withdraw {withdraw_m} and the total Balance{SBI_Rama['Balance']}')
                   user_1 = int(input('enter \n1. home page \n2. Exit \n3.transcations history \nselect your option:'))
                   if user_ == 1:
                       print('home page')
                else:
                     print(' Thankyou Rama')
                    
                break
            else:
                print('can not provide change or no balance')
                break
        elif opt_ ==2:
            deposite_m = int(input('Enter the money you want to deposite'))
            if deposite_m % 100 == 0:
                SBI_Rama['Balance'] += deposite_m
                print(f'you have deposited {deposite_m} and the total balance is {SBI_Rama['Balance']}')
                user_ = int(input('Enter \n1. home page \n2. Exit transcations history \nselect your option: '))
                if user_ == 1:
                    print('home page')
                else:
                    print('Thank you')
                    
            else:
               print('change can not be deposite')
        elif opt_ == 3:
            pass
               
        
            
        else:
            remain_A -= 1
            if remain_A >0:
                print(f'Incorrect pin and you have only {remain_A}')
            else:
                print('card is block')
                break
    else:
        print('pls enter only 4 digit atm pin ')


































