PBuy_price = float(input("Enter Buy Price of Per stock:  ") )
N = int(input("Enter The Number of Shares:  " ))
PSell_price = float(input("Enter sell Price of Per stock:  ") )
Buy_price = PBuy_price*N
Sell_price = PSell_price*N
Commission1 = 0.005*(Buy_price)
Commission2 = 0.005*(Sell_price)
Total_purchase_price = Buy_price+Commission1
Total_Sell_price = Sell_price+Commission2
Profit = Total_Sell_price-Total_purchase_price
print("******Displaying Information******")
print("Amount paid for the Stock" ,Buy_price, "BDT")
print("Commission paid for the Buying Stock" ,Commission1, "BDT")
print("Amount paid for the Stock" ,Sell_price, "BDT")
print("Commission paid for the Selling Stock" ,Commission2, "BDT")
if Profit>0 :
    print("The Profit is " ,Profit, "BDT" )
else :
    print("The Loss is ", abs(Profit), "BDT")