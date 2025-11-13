import os
import csv

class PersonInformation:
    def __init__(self,name,address,phoneNumber,age,gender):
        self.name=name
        self.address = address
        self.phoneNumber = phoneNumber
        self.age =age
        self.gender = gender
    
    #增加联系人
    def __str__(self):
        return f"名字: {self.name}, 性别: {self.gender}, 年龄: {self.age}, 电话: {self.phoneNumber}, 住址: {self.address}"
    
class ContactList:
    def __init__(self):
        self.contactlist = []

    #增
    def add_person(self,person):
        self.contactlist.append(person)
        print("添加完成")
    #删
    #改
    #查
    #保存
    def save_contact(self,filename="contacts.csv"):
        with open(filename,"w",newline=' ',encoding='utf-8') as f:
            write = csv.writer(f)
            write.writerow(['姓名','年龄','住址','性别','电话'])
            for person in self.contactlist:
                write.writerow
    #
