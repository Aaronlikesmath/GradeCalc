# coding=utf-8
#output_m = int(input("Welchen output mode?(standard ist 1): "))

GradeE = str(input("Exam grade: "))
GradeC = str(input("Class grade: "))
Grade = [GradeE, GradeC]
#def debug():
#    if output_m == 2:
#        print ()


#Function that uses dictionary to transform grade into Ints
def gtdict(gradesingle):
    return {
        "1" : 15,
        "1-" : 14,
        "2+" : 13,
        "2" : 12,
        "2-" : 11,
        "3+" : 10,
        "3" : 9,
        "3-" : 8,
        "4+" : 7,
        "4" : 6,
        "4-" : 5,
        "5+" : 4,
        "5" : 3,
        "5-" : 2,
        "6" : 1
    }.get(gradesingle, 1)


#Function That operate the dict funtion
def gt(Grade):
    GE, GC = Grade
    global gradesingle
    gradesingle = GE
    GEt = gtdict(gradesingle)
    gradesingle = GC
    GCt = gtdict(gradesingle)
    return GEt, GCt


GEt, GCt = gt(Grade)
#print (GEt, GCt)


#Function that average taking 60% from GCt and 40% from GEt
def average(GEt, GCt):
    AV1 = (GCt * 3) + (GEt * 2)
    FinalAV = AV1 / 5
    FinalAVRound = round(float(FinalAV))
    return FinalAVRound


#Function that transforms FinalAVRound Back into a German Grade using a Dictionary
def gut(FinalAVRound):
    return {
        15 : "1",
        14 : "1-",
        13 : "2+",
        12 : "2",
        11 : "2-",
        10 : "3+",
        9 : "3",
        8 : "3-",
        7 : "4+",
        6 : "4",
        5 : "4-",
        4 : "5+",
        3 : "5",
        2 : "5-",
        1 : "6"
    }.get(FinalAVRound, 6)


FinalAVRound = average(GEt, GCt)
FinalGrade = gut(FinalAVRound)
print ("Final grade is", FinalGrade)