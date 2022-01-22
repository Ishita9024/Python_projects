import requests
import json
res=requests.get('http://saral.navgurukul.org/api/courses')
a=res.json()
with open("courses.json","w") as b:
    json.dump(a,b,indent=4)
serial_no=0
for i in a.values():
    for j in i:
        print(serial_no+1,":",j["name"],"ID:",j["id"])
        serial_no+=1
print("")
course_id=int(input("enter the course no. :-"))
print(course_id,":",a["availableCourses"][course_id-1]["name"],a["availableCourses"][course_id-1]["id"])
user_input1=input("Do you want to go previous or next? (1) : ")
if user_input1=="p" or user_input1=="P":
    serial_no=0
    for i in a.values():
        for j in i:
            print(serial_no+1,j["name"],"ID:",j["id"])
            serial_no+=1
    print("")
    course_id=int(input("enter the course no. :-"))
    print(course_id,a["availableCourses"][course_id-1]["name"])
res1=requests.get('http://saral.navgurukul.org/api/courses/'+str(a["availableCourses"][course_id-1]["id"])+'/exercises')
d=res1.json()
with open("parents.json","w") as e:
    json.dump(d,e,indent=4)
serial_no=0
for j in d["data"]:
    print(serial_no+1,j["name"])
    serial_no+=1
    if j["childExercises"]==[]:
        print("     ",j["slug"])
    else:
        serial_num=0
        for i in j["childExercises"]:
            print("     ",serial_num+1,":",i["name"])
            serial_num+=1
parent_id=int(input("enter the parent no. :- "))
print(parent_id,d["data"][parent_id-1]["name"])
user_input2=input("Do you want to go previous or next Enter your choice ? (2) : ")
if user_input2=="p" or user_input2=="P":
    serial_no1=0
    for k in d["data"]:
        print(serial_no1+1,k["name"])
        serial_no1+=1
        if k["childExercises"]==[]:
            print("     ",k["slug"])
        else:
            serial_num1=0
            for l in k["childExercises"]:
                print("     ",serial_num1+1,":",l["name"])
                serial_num1+=1
    parent_id=int(input("enter the parent no. :- "))
    print(parent_id,d["data"][parent_id-1]["name"])

if d["data"][parent_id-1]["childExercises"]==[]:
    print(d["data"][parent_id-1]["slug"])
    pid=d["data"][parent_id-1]["id"]
    pslug=d["data"][parent_id-1]["slug"]
    parent_api='http://saral.navgurukul.org/api/courses/'+str(pid)+'/exercise/getBySlug?slug='+pslug
    slug_url=requests.get(parent_api)
    slug_file=slug_url.json()
    print(slug_file["content"])
else:
    k=0
    while k<len(d["data"][parent_id-1]["childExercises"]):
        print("     ",k+1,":",d["data"][parent_id-1]["childExercises"][k]["name"])
        k+=1
    list=[]
    for i in range(len(d["data"][parent_id-1]["childExercises"])):
        z=d["data"][parent_id-1]["childExercises"][i]["slug"]
        r=d["data"][parent_id-1]["childExercises"][i]["id"]
        t='http://saral.navgurukul.org/api/courses/'+str(r)+'/exercise/getBySlug?slug='+z
        res2=requests.get(t)
        g=res2.json()
        list.append(g["content"])
    child_id=int(input("enter the child no.:- "))
    print(list[child_id-1])
    while child_id>0:
        user_input3=input("Do you want to go previous or next Enter your choice ? : ")
        if user_input3=="p":
            if child_id==1:
                print("no more")
                break
            elif child_id>0:
                print(list[child_id-2])
                child_id-=1
        elif user_input3=="n":
            if child_id<len(list):
                print(list[child_id])
                child_id+=1
            elif child_id==len(list):
                    print("next page")
                    break
            

