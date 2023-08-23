import abc


#Parent Class Spotted
class Product(metaclass=abc.ABCMeta):
    def __init__(self, name="null", code="null", price=-999, is_weight=False):
        self.name = name
        self.code = code
        self.price = price
        self.is_weight = is_weight

    @abc.abstractmethod
    def product_catalog(self, prodarr):
        pass

    @abc.abstractmethod
    def insert(self, prodarr):
        pass

#Child Class #1 Spotted
class NumberedProduct(Product):
    def product_catalog(self, prodarr):
        print("Numbered Product Entered Successfully \n Your Catalog is:")
        lists = ["Products", "Code" , "price/Piece"]
        print(lists)
        for product in prodarr:
            print(product)

    def insert(self, prodarr):
        prodname = input("Enter Product Name: ")
        prodcode = input("Enter Product Code: ")
        prodprice = float(input("Enter Product Price / piece: "))

        prodlist = [prodname, prodcode, prodprice]

        prodarr.append(prodlist)

        self.product_catalog(prodarr)

#Child Class #2 Spotted
class WeightedProduct(Product):
    def product_catalog(self, prodarr):
        print("Weighted Product Entered Successfully \n Your Catalog is:")
        lists = ["Products", "Code" , "Price/Liter"]
        print(lists)
        for product in prodarr:
            print(product)

    def insert(self, prodarr):
        prodname = input("Enter Product Name: ")
        prodcode = input("Enter Product Code: ")
        prodprice = float(input("Enter Product Price / litre: "))

        
        prodlist = [prodname, prodcode, prodprice]

        prodarr.append(prodlist)

        self.product_catalog(prodarr)


if __name__ == "__main__":
    prodarr = []
    
    numbered_prod = NumberedProduct()
    weighted_prod = WeightedProduct()

    try:
        types = str(input("Enter Product Type : "))
        if types == "numbered":
            numbered_prod.insert(prodarr)
        elif types == "weighted":
            weighted_prod.insert(prodarr)
        else:
            msg = "Unknown Type Error"
            alert = TypeError(msg)
            print(alert)   
    except:
        msg = "Invalid Type Error"
        TypeError(msg)






    
    
