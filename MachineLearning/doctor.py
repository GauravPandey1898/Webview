class Doctor:
    def __init__(self,id,name,specialize,fees):
        self.doctorid=id
        self.doctorName=name
        self.specialization=specialize
        self.consultationFee=fees

class Hospital(Doctor):
    def __init__(self,doctorD):
        self.doctorDB=doctorD
    def searchByDoctorName(self,name):
        obj_list=[]
        for x in self.doctorDB:
            obj=self.doctorDB[x]
            if(obj.doctorName==name):
                obj_list.append(obj)
        if(len(obj_list)==0):
            return 0
        else:
            return obj_list
    def calculateConsultationFeeBySpecialization(self,special):
        total=0
        for x in self.doctorDB:
            obj=self.doctorDB[x]
            if(obj.specialization==special):
                total=total+obj.consultationFee
        if(total==0):
            return 0
        else:
            return total

item=int(input())
doctorDB=dict()
for i in range(item):
    id=int(input())
    name=input()
    special=input()
    fees=int(input())
    obj=Doctor(id,name,special,fees)
    doctorDB[id]=obj
docname=input()
obj=Hospital(doctorDB)
doctor_list=obj.searchByDoctorName(docname)
specialization=input()
consultationFeesTotal=obj.calculateConsultationFeeBySpecialization(specialization)
if(doctor_list==0):
    print("No Doctor Exists with the given DoctorName")
else:
    for x in doctor_list:
        print(x.doctorid)
        print(x.doctorName)
        print(x.specialization)
        print(x.consultationFee)
if(consultationFeesTotal==0):
    print("No Doctor with the given specialization")
else:
    print(consultationFeesTotal)

