import datetime
today_DT = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

# -----------handling phn number from end-user give string or symbol--------
# -----------it will run until it give valid number -----------------------
while True:
    try:
        phn = int(input("Enter the Customer Phone Number : "))  # phn no. validation
        if len(str(phn)) == 10:
            break
        else:
            print('Invalid phn number Enter again!!!!')
    except:
        print("invalid phone number!!Enter again")
    # ---- if client demand to handle customer name having digit not allow ------
# -----need another condition here for above scenario------
name = input("Enter the Customer name : ")
items = {}
total_qty = 0
# ----while loop because run until the process  is complete------
while True:
    while True:
        item_no = input("Enter the Item number : ")
        if item_no not in items:
            if ((item_no[0] >= 'a' and item_no[0] <= 'z') or (item_no[0] >= 'A' and item_no[0] <= 'Z')) and (
                    (item_no[1] >= 'a' and item_no[1] <= 'z') or (item_no[1] >= 'A' and item_no[1] <= 'Z')):
                break
            else:
                print("INVALID ITEM NUMBER!!!!! Enter again")
        else:
            print("Item number repeated check and type again!!!")

    item_name = input("Enter the Item Name : ")
    while True:
        try:
            # ----handling quantity from entering invalid input------
            qty = float(input("Enter the quantity : "))
            total_qty += qty
        except:
            print("Invalid Quantity!!Enter again")
        else:
            break
    while True:
        try:
            # --- handling amount from getting invalid input-----
            amt = float(input("Enter the Amount : "))
        except:
            print("invalid Amount!!!!Enter again")
        else:
            break
    while True:
        try:
            mrp = float(input("Enter the Actual MRP : "))
        except:
            print("Invalid MRP!!! Enter again")
        else:
            break
    items.update({item_no: [item_name, qty, amt, mrp]})
    exit = input("Press ENTER to continue or type 'exit' to generate the bill \n")
    if exit == 'exit':
        break


# this will work when invoke
class Tax:
    def __init__(self, bill_no, today_DT, phn, name, items, total_qty):
        self.bill_no = bill_no
        self.today_DT = today_DT
        self.phn = phn
        self.name = name
        self.item = items
        self.total_qty = total_qty

    def bill(self):
        while True:
            attender_name = input("Enter the Attender name : ")
            if len(attender_name) != 0:
                break
        print()
        print()
        # -------printing bill format----------------------------
        if len(self.name) != 50:
            name = self.name + ' ' * (50 - len(self.name))
        print("NAME : ", name, end="")
        if len(str(self.bill_no)) != 50:
            bill_no = str(self.bill_no) + ' ' * (50 - len(str(self.bill_no)))
        print("BILL No : ", bill_no)
        if len(str(self.phn)) != 50:
            phn = str(self.phn) + ' ' * (50 - len(str(self.phn)))
        print("Phn : ", phn, end='')
        if len(self.today_DT) != 50:
            today_DT = self.today_DT + ' ' * (50 - len(self.today_DT))
        print("Date : ", today_DT)
        print()
        print('-' * 100)
        print("Sl No", 'Item no   ', 'Description' + ' ' * 24, 'Qty      ', 'Amt (₹)      ', 'GST %   ',
              'MRP (₹)      ')
        print('-' * 100)
        sl = 0
        total_amt = 0
        total_mrp = 0

        for i, j in items.items():
            if j[1] != 0:
                if len(str(sl)) != 5:
                    sl1 = str(sl) + ' ' * (5 - len(str(sl)))
                print(sl1, end=' ')
                sl += 1
                if len(i) != 10:
                    i = i + ' ' * (10 - len(i))
                print(i, end=' ')  # ITEM NUMBER
                if len(j[0]) != 35:
                    j[0] = j[0] + ' ' * (35 - len(j[0]))
                print(j[0], end=' ')  # ITEM NAME
                if len(str(j[1])) != 8:
                    qty1 = str(j[1]) + ' ' * (8 - len(str(j[1])))
                print(qty1, end=' ')  # QUANTITY

                if len(str(j[2])) != 13:
                    amt1 = str(j[2]) + ' ' * (13 - len(str(j[2])))
                print(amt1, end=' ')  # AMOUNT
                # ---------------this let to show the gst% only at first
                if sl == 1:
                    print('  12 %  ', end=' ')
                else:
                    print(' ' * 8, end=' ')
                total_amt += j[2] * j[1]  # TOTAL AMOUNT
                if len(str(j[3])) != 13:
                    mrp1 = str(j[3]) + ' ' * (13 - len(str(j[3])))
                print(mrp1)  # MRP
                total_mrp += j[3]  # TOTAL MRP
        print('-' * 100)
        print('Attended by : ', attender_name.upper(), ' ' * (24 - len(attender_name)), 'Total Qty :', self.total_qty,
              ' ' * 13, 'Total   ', total_amt)
        print('-' * 100)
        print(' ' * 76, end=' ')
        # -------calculating discount and bill
        dis = ((15 / 100) * total_amt)
        print('discount   : ', dis)
        dis_amt = total_amt - dis
        # print(dis_amt)
        print(' ' * 76, end=' ')
        gst = (12 / 100) * dis
        print('gst        : {:.2f} '.format(gst))
        res = dis_amt + gst
        # print('res: ',res)
        print(' ' * 76, end=' ')
        round_off = res - int(res)
        print("round_off  :  {:.2f}".format(round_off))
        print(' ' * 76, end=' ')
        grand_total = res - round_off
        print('grand_total: ', grand_total)

a = Tax(bill_no, today_DT, phn, name, items, total_qty)
a.bill()