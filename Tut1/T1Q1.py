import os #implement clear function

student={}
student["id"]=input("Enter Student ID: ")
student["name"]=input("Enter Name: ")
student["dob"]=input("Enter Date of Birth: ")
student["height"]=input("Enter Height (cm): ")
student["weight"]=input("Enter Weight (kg): ")

clear = lambda: os.system('cls') #declare clear
clear()
print("***Welcome to the Department of Electrical Engineering***")
print("Student ID: "+student["id"])
print("Name: "+student["name"])
print("Date of Birth: "+student["dob"])
print("Height(cm): "+student["height"])
print("Weight(kg): "+student["weight"])
print("*** End ***")