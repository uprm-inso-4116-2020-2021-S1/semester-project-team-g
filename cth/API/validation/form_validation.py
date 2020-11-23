import datetime
from datetime import datetime as dt
import re

class FormValidation:
    def validate_all_functions(self, data):
        self.data = data
        functions = [func for func in dir(FormValidation) if callable(getattr(FormValidation, func)) and func.startswith("validate") and func != "validate_all_functions"]
        error_messages = {}
        for func in functions:
            field_name = func.split("validate_")[1]
            result = eval("self." + func + "()")
            if result != None:
                error_messages[field_name] = result

        return error_messages

    def validate_first_name(self, data=None):
        if data:
            self.data = data
        if "firstname" not in self.data: return "Error: firstname is not present on the json!"
        first_name = self.data["firstname"]
        if len(first_name) == 0 or first_name == "":
            return "Error: First name is empty"

    def validate_last_name(self, data=None):
        if data:
            self.data = data
        if "lastname" not in self.data: return "Error: lastname is not present on the json!"
        last_name = self.data["lastname"]
        if len(last_name) == 0 or last_name == "":
            return "Error: Last name is empty"

    def validate_date_of_birth(self, data=None):
        if data:
            self.data = data
        if "date_of_birth" not in self.data: return "Error: date_of_birth is not present on the json!"
        date_of_birth = self.data["date_of_birth"]
        try:
            self.is_valid_date(date_of_birth)
        except Exception as e:
            return e

        month, _, year = date_of_birth.split("/")
        if (int(month) > dt.today().month and int(year) == int(dt.today().year)) or int(year) > dt.today().year:
            return "Error: Date is not valid as it is in the future!"


    def is_valid_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, "%m/%d/%Y")
        except Exception as e:
            raise Exception("Error: " + str(e) + " | Verify that the date is valid!")


    def validate_sex(self, data=None):
        if data:
            self.data = data
        if "sex" not in self.data: return "Error: sex is not present on the json!"
        gender = self.data["sex"]
        if gender.lower() != "m" and gender.lower() != "f":
            return "Error: Sex must be 'm' or 'f'"

    def validate_address(self, data=None):
        if data:
            self.data = data
        if "address" not in self.data: return "Error: address is not present on the json!"
        address = self.data["address"]
        if not address or len(address) == 0:
            return "Error: Address is empty!"
        try:
            self.is_zipcode_present(address)
        except Exception as e:
            return str(e)

    def is_zipcode_present(self, s):
        if not re.search(r"00\d{3}|0\d{4}", s):
            raise Exception("Zip code was not found!")

    def validate_phone(self, data=None):
        if data:
            self.data = data

        if "phone" not in self.data: return "Error: phone is not present on the json!"
        phone = self.data["phone"]
        if not re.match(r"\d{3}\-\d{3}\-\d{4}", phone):
            return "Error: Phone number invalid! Phone number format must follow this example: 787-123-4567"

    def validate_ssn(self, data=None):
        if data:
            self.data = data

        if "ssn" not in self.data: return "Error: ssn is not present on the json!"
        ssn = self.data["ssn"]
        if not re.match("\d{9}", ssn):
            return "Error: SSN format invalid! SSN format must follow this example: 123456789"

    def validate_ishp(self, data=None):
        if data:
            self.data = data

        if "ishp" not in self.data: return "Error: ishp is not present on the json!"
        ishp = self.data["ishp"]
        if ishp != True and ishp != False:
            return "Error: ishp has to be 'True' or 'False'!"

    def validate_institution(self, data=None):
        if data:
            self.data = data

        if "institution_name" not in self.data: return "Error: institution_name is not present on the json!"
        institution_name = self.data["institution_name"]
        if len(institution_name) == 0 or institution_name == "":
            return "Error: Institution name is empty"

    def validate_illness(self, data=None):
        if data:
            self.data = data

        if "illness" not in self.data: return "Error: illness is not present on the json!"
        illness = self.data["illness"]
        if len(illness) == 0 or illness == "":
            return "Error: Illness field is empty"

    def validate_is_positive(self, data=None):
        if data:
            self.data = data

        if "is_positive" not in self.data: return "Error: is_positive is not present on the json!"
        is_positive = self.data["is_positive"]
        if is_positive != True and is_positive != False :
            return "Error: is_positive has to be 'True' or 'False'!"



# fv = FormValidation()
# print( fv.validate_date_of_birth({"date_of_birth":"12/1/2020"}) )
# print( fv.validate_date_of_birth({"date_of_birth":"13/1/2020"}) )
# print( fv.validate_address({"address":"Mayaguez"}) )
# print( fv.validate_address({"address":"Mayaguez 00123"}) )
# print( fv.validate_phone({"phone":"787-111-1111"}) )
# print( fv.validate_phone({"phone":"78-111-1111"}) )
# print( fv.validate_ssn({"ssn":"999-11-1234"}) )
# print( fv.validate_ssn({"ssn":"78-111-1111"}) )
# print( fv.validate_ishp({"ishp":True}) )
# print( fv.validate_ishp({"ishp":"True"}) )

# patientData = {
#       "firstname": "Jose",
#       "lastname": "Biescas",
#       "address": "Calle Manuel 00123",
#       "date_of_birth": "10/1/1999",
#       "phone": "787-555-5555",
#       "sex": "male",
#       "ssn": "123-45-6789",
#       "ishp": "alive",
#       "illness": "covid-19",
#       "is_positive": "positive",
#       "institution_name": "Hospital Mutuo",#institution_name
#       "timestamp": "11/22/2020"
#     }
# print( FormValidation().validate_all_functions(patientData) )
