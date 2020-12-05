# coding=utf-8
#output_m = int(input("Welchen output mode?(standard ist 1): "))

GradeE = str(input("Exam grade: "))
GradeC = str(input("Class grade: "))
Grade = [GradeE, GradeC]
#def debug():
#    if output_m == 2:
#        print ()


transdict = {
    "1" : 1.0,
    "1-" : 1.4,
    "2+" : 1.6,
    "2" : 2,
    "2-" : 2.4,
    "3+" : 2.6,
    "3" : 3,
    "3-" : 3.4,
    "4+" : 3.6,
    "4" : 4,
    "4-" : 4.4,
    "5+" : 4.6,
    "5" : 5,
    "5-" : 5.4,
    "6" : 6
}


#Function Transforms grades into number using transdict
def gt(Grade):
    GE, GC = Grade
    GEt = transdict.get(GE, 1)
    GCt = transdict.get(GC, 1)
    return GEt, GCt


GEt, GCt = gt(Grade)
#print (GEt, GCt)


#Function that average taking 60% from GCt and 40% from GEt
def average(GEt, GCt):
    AV1 = (GCt * 3) + (GEt * 2)
    FinalAV = AV1 / 5
    return FinalAV

FinalAV = average(GEt, GCt)
print ("Final grade is", round(FinalAV, 1))