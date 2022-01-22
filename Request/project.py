# import requests
# import json
# partner_url=requests.get('http://join.navgurukul.org/api/partners')
# partner_file=partner_url.json()
# with open("partners.json","w") as file:
#     json.dump(partner_file,file,indent=4)
# Id_name={}
# for i in partner_file["data"]:
#     print(i["name"],"ID:",i["id"])
#     Id_name[i["id"]]=i["name"]
# print("")
# def sort():
#     if user_input=="a" or user_input== "A":
#         Id_list=[]
#         for i in Id_name:
#             Id_list.append(i)
#         k=0
#         while k<len(Id_list):
#             j=0
#             while j<len(Id_list)-1:
#                 if Id_list[j]>Id_list[j+1]:
#                     Id_list[j],Id_list[j+1]=Id_list[j+1],Id_list[j]
#                 j+=1
#             k+=1
#         for m in range(len(Id_list)):
#             print(Id_list[m],Id_name[Id_list[m]])
#     else:
#         Id_list=[]
#         for i in Id_name:
#             Id_list.append(i)
#         k=0
#         while k<len(Id_list):
#             j=0
#             while j<len(Id_list)-1:
#                 if Id_list[j]<Id_list[j+1]:
#                     Id_list[j],Id_list[j+1]=Id_list[j+1],Id_list[j]
#                 j+=1
#             k+=1
#         for m in range(len(Id_list)):
#             print(Id_list[m],Id_name[Id_list[m]])
# user_input=input("In which form you want to sort? Say Ascending or Descending and Enter 'A' and 'D' respectively : ")
# sort()
        



    
