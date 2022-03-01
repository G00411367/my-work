# This program stores in a dict a student name,
# courses and grades 

student = {
    "name" : "Mary",
    "modules" : [
        {
            "courseName" : "Programming", 
            "grade" : 45
        },
        {   
            "courseName" : "Hystory",
            "grade" : 99
        }
    ]
}
print("Student : {}" .format(student["name"]))
for m in student["modules"]:
    print("\t{} \t{}" .format(m["courseName"], m["grade"]))



