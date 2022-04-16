"""
Name: Andrew Turner
HW11.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        readfile = open(file_name, 'r')
        for line in readfile.readlines():
            self.sales_people.append(line.removesuffix('\n'))

    def quota_report(self, quota):
        fulllist = []
        for saleman in self.sales_people:
            saleboy = saleman.split(',')
            sales = saleboy[2].split()
            theman = [int(saleboy[0]), saleboy[1].removeprefix(' ')]
            totals = 0
            for sale in sales:
                totals = totals + float(sale)
            theman.append(totals)
            if totals >= quota:
                theman.append(True)
            else:
                theman.append(False)
            fulllist.append(theman)
        return fulllist

    def top_seller(self):
        top = []
        for bro in self.sales_people:
            total = 0
            sales = bro[2].split()
            for sale in sales:
                total = total + float(sale)
            top.append([total, bro[0], bro[1]])
        top.sort()
        #TOOTIREDTODORESTSORRY :P
        return top[len(top)-1]

    def individual_sales(self, employee_id):
        for saleboy in self.sales_people:
            saleboy = saleboy.split(',')
            if employee_id == saleboy[0]:
                return saleboy[1].removeprefix(' ')
        return None

    def get_sale_frequencies(self):
        salelist = []
        dictionary = {}
        for saleboy in self.sales_people:
            sales = saleboy[2].split()
            for sale in sales:
                salelist.append(float(sale))
        for i in salelist:
            dictionary




bruh = SalesForce()
bruh.add_data('sales_data.txt')
bruh.individual_sales('123')






