"""
Name: Andrew Turner
HW11.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
class SalesPerson:
    def __init__(self, employee_id, name):
        self.name = name
        self.employee_id = employee_id
        self.sales = []
    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        saleaccum = 0
        for sale in self.sales:
            saleaccum = saleaccum + sale
        return saleaccum

    def get_sales(self):
        return self.sales

    def met_quota(self,quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        selftotal = self.total_sales()
        othertotal = other.total_sales()
        if selftotal > othertotal:
            return 1
        elif selftotal < othertotal:
            return -1
        else:
            return 0

    def __str__(self):
        return str(self.employee_id)+'-'+str(self.name)+':' + str(self.total_sales())
