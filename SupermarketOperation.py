#HİLAL SÖYLEMEZ 22100001004 BİLGİSAYAR PROGRAMCILIĞI
from SupermarketInformation import *

market1 = Market()

print("read all product 1\nquery according to name for 2\nquery according to brand for 3\nadd new product for 4\ndelete product for 5\nupdate price for 6\nupdate quantitiy for 7")


while True:
    process = int(input("to exit for 0"))

    if process == 0:
        break
    
    elif process == 1:
        market1.readAllProduct()
    
    elif process == 2:
        name = input("name: ")
        market1.queryAccordingToName(name)
    
    elif process == 3:
        brand = input("brand: ")
        market1.queryAccordingToBrand(brand)
    
    elif process == 4:
        name = input("product name: ")
        brand = input("product brand: ")
        type = input("product type: ") 
        quantitiy = int(input("product quantity: "))
        price = int(input("product price: "))
        product = Product(name, brand, type, quantitiy, price)
        market1.addNewProduct(product)

    elif process == 5:
        name = input("product name: ")
        market1.deleteProduct(name)

    elif process == 6:
        name = input("product whose price will be changed: ")
        changePrice = int(input("how much will be changed to the price: "))
        market1.updatePrice(changePrice, name)
       
    elif process == 7:
        name = input("product whose quantitiy will be changed: ")
        changeQuantity = int(input("how much will be chnaged yo the quantity: "))
        market1.updateQuantity(changeQuantity, name)

    else:
        print("please choose process")



conection=sqlite3.connect("information.db")
cursor=conection.cursor()

with open("sale.txt", "r", encoding="utf-8") as s:
    sales = s.readlines()
    for i in sales:
        productName, productQuantity, = i.strip().split(' ')
        cursor.execute("UPDATE information SET  productQuantity = productQuantity - ? WHERE productQuantity = ?", (productQuantity, productName))

cursor.execute("SELECT productName, productQuantity FROM information")

newSale = cursor.fetchall()
newSale.sort()
with open("updateSale.txt", "r+", encoding="utf-8") as update:
    for i in newSale:
        update.write(f"{i[0]}, {i[1]}" + "\ n")

conection.commit()
conection.close()