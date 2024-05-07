#HİLAL SÖYLEMEZ 22100001004 BİLGİSAYAR PROGRAMCILIĞI
import sqlite3

class Product():
    def __init__(self, productName, productBrand, productType, productQuantity, productPrice):
        self.productName = productName
        self.productBrand = productBrand
        self.productType = productType
        self.productQuantity = productQuantity
        self.productPrice = productPrice
    
    def __str__(self):
        return f"product name is {self.productName}\nproduct brand is {self.productBrand}\nproduct type is {self.productType}\nproduct price is {self.productPrice}\nproduct quantitiy is {self.productQuantity}"

class Market():
    def __init__(self):
        self.connection()
    
    def connection(self):
        self.conn = sqlite3.connect("information.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS information(productName TEXT, productBrand TEXT, productType TEXT, productQuantity INT, productPrice INT)")
        self.conn.commit()

    def disconnection(self):
        self.conn.close()

    def readAllProduct(self):
        self.cur.execute("SELECT * FROM information")
        fetc = self.cur.fetchall()
        for i in fetc:
            prod = Product(i[0], i[1], i[2], i[3], i[4])
            print(prod, "\n***************")

    def queryAccordingToName(self, productName):
        self.cur.execute("SELECT * FROM information WHERE productName = ? ", (productName,))
        fetc = self.cur.fetchall()
        prod = Product(fetc[0][0], fetc[0][1], fetc[0][2], fetc[0][3], fetc[0][4])
        print(prod, "\n***************")

    def queryAccordingToBrand(self, productBrand):
        self.cur.execute("SELECT * FROM information WHERE productBrand = ? ", (productBrand,))
        fetc = self.cur.fetchall()
        for i in fetc:
             prod = Product(i[0], i[1], i[2], i[3], i[4])
             print(prod, "\n***************")

    def addNewProduct(self, prod):
        self.cur.execute("INSERT INTO information VALUES(?,?,?,?,?)", (prod.productName, prod.productBrand, prod.productType, prod.productQuantity, prod.productPrice ))
        self.conn.commit()

    def deleteProduct(self, productName):
        self.cur.execute("DELETE FROM information where productName = ?", (productName,))
        self.conn.commit()

    # bu kısımlarda üzerine ekleme kısımları ekle sil onları kullanman lazım.

    def updatePrice(self, changePrice, name,):
        question = input("will the price increase? (yes/no)")
        if question == "yes":
                self.cur.execute("Select productPrice From information where productName = ?", (name,))
                result = self.cur.fetchone()
                currentPrice = result[0] 
                newPrice = currentPrice +  changePrice
                self.cur.execute("UPDATE information SET productPrice = ? where productName = ? ", (newPrice, name))
                self.conn.commit()

        elif question == "no":
                self.cur.execute("Select productPrice From information where productName = ?", (name,))
                result = self.cur.fetchone()
                currentPrice = result[0] 
                newPrice2 = currentPrice -  changePrice
                self.cur.execute("UPDATE information SET productPrice = ? where productName = ? ", (newPrice2, name))
                self.conn.commit()
            
        
    def updateQuantity(self, changeQuantity, name):
        question = input("will the quantity increase? (yes/no)")
        if question == "yes":
                self.cur.execute("Select productQuantity From information where productName = ?", (name,))
                result = self.cur.fetchone()
                currentQuantity = result[0] 
                newQuantity = currentQuantity +  changeQuantity
                self.cur.execute("UPDATE information SET productQuantity = ? where productName = ? ", (newQuantity, name))
                self.conn.commit()

        elif question == "no":
                self.cur.execute("Select productQuantity From information where productName = ?", (name,))
                result = self.cur.fetchone()
                currentQuantity = result[0] 
                newQuantity2 = currentQuantity -  changeQuantity
                self.cur.execute("UPDATE information SET productQuantity = ? where productName = ? ", (newQuantity2, name))
                self.conn.commit()
            
    
