import pandas
import time
#For Account Balance use Dict
#
#  ###

CustomerAccount = {"Zerihun":1001,"lkl":4545}
AccountTransactions = {}
def AddAccount(ID):
    Account(ID)
def acctbalance(dep,acct,AMOUNT):
    #acc=acc
    accbal={}
    if len(accbal)==0:
         accbal[acct]=AMOUNT
         return accbal
    if dep=="+":
        accbal[acct]+=AMOUNT
        return accbal
    else:
         accbal[acct]-=AMOUNT
         return accbal
def oper():
    BankAction=input("Deposit,withdrawal,TransactionHistory")
    acct=input("Insert Acct ID")
    if BankAction =="Deposit":
        AMOUNT=input("Insert Deposit Amount")
        dep="+"
        print(acctbalance(dep,acct,AMOUNT))
    elif BankAction =="withdrawal":
        AMOUNT=input("Insert Withdrawal Amount")
        dep="-"
        print(acctbalance(dep,acct,AMOUNT))
    elif BankAction =="Transaction History":
        AMOUNT=input("Insert Withdrawal Amount")
        dep="-"
        print(acctbalance(dep,acct,AMOUNT))

print("Welcome!")
oper()
def Account(acc):
    Account_lists=["100001","100002","100003","100004","100005","100006","100007"]
    Account_lists.append(acc)
    print(Account_lists)
    return Account_lists
#print(Account(" "))
def AddAccount(ID):
    Account(ID)
def acctbalance(dep,acct,AMOUNT):
    #acc=acc
    accbal={}
    if len(accbal)==0:
         accbal[acct]=AMOUNT
         return accbal
    if dep=="+":
        accbal[acct]+=AMOUNT
        return accbal
    else:
         accbal[acct]-=AMOUNT
         return accbal
    conf()
#ID= input("Please Insert ID")
#NAME=input("INSERT CUST NAME")
AddAccount(100001)
CustomerAccount["NAME"]= 100001
print(CustomerAccount)
#AMOUNT=12.00
contt=input("Do you want to Continue")
def conf():
    contt=input("Do you want to Continue")
    if contt=="Y":
        oper()
    else:
        exit()