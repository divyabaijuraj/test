# bank account verification process
class UserContact(object):

    def __init__(self, aadhar=0, PANNo='0'):
        self.aadhar = aadhar
        self.PAN = PANNo

    def getAadharNo(self):
        return self.aadhar

    def getPAN(self):
        return self.PAN

    def display(self):
        print(str(self.aadhar), ' ', self.PAN)

    def __str__(self):
        return str(self.aadhar) + ' ' + self.PAN

    def setAadharNo(self, a):
        self.aadhar = a

    def setPAN(self, p):
        self.PAN = p


class BankVerificaiton(object):

    def __init__(self, formno, mobile, emailID, cardno, userinfo):
        self.form = formno
        self.mobile = mobile
        self.emailId = emailID
        self.cardno = cardno
        self.uinfo = userinfo

    def __str__(self):
        return str(self.form) + " *** " + str(self.mobile) + " **** " + self.emailId

    def __verification(self):
        print('calling the Aadhar Card Server ')
        print('checking the Aadharcar details ', self.uinfo.getAadharNo())
        print('calling the PAN card server ....')
        print('checking the details of PAN ', self.uinfo.getPAN())
        print('verification done')
        return 100, 200

    def __sendSMS(self):
        print('sending SMS via the SMSGateway IP 10.23.177.200 ')
        print('to the mobile number ', self.mobile)

    def __sendEmail(self):
        print('sending Email via the email server Gateway IP 155.23.179.100 ')
        print('to the email ID  ', self.emailId)

    def card_status(self):
        r1, r2 = self.__verification()
        if r1 == 100 and r2 == 200:
            print('Aadhar card is successfully verified ')
            print('PAN card is successfully verified ')
            self.__sendSMS()
            self.__sendEmail()
            print()
            print('----congratulations your card ', self.cardno, ' is SUCCESSFULLY activated ')
        else:
            print('verification Failed ...issue either in Aadhar Card or PAN Card ')
            print('Please meet the Kotak Bank Staff at the nearest center ')


print('--------Main block starts here ------')
# objUser = UserContact(397788461234,'ACCPV2287W')

objUser = UserContact()
objUser.setAadharNo(456689006789)
objUser.setPAN('ACCPR3345Q')

objUser.display()
print(objUser)
print(objUser.__str__())
print('hash value is ', objUser.__hash__())
print()
objBank = BankVerificaiton(1000, 9776655123, 'prabhakar@gmail.com', 6166690789261234, objUser)
print(objBank)
# objBank._verification()
objBank.card_status()
print('--------Main block ends here --------')