# coding=utf-8
#output_m = int(input("Welchen output mode?(standard ist 1): "))

noteS = str(input("Schriftliche Note: "))
noteM = str(input("Mündliche Note: "))
Note = [noteS, noteM]
def debug():
    if output_m == 2:
        print (NEt)


def nt(Note):
    NS, NM = Note
    if NS == str("1"):
        NSt = 16

    if NS == str("1-"):
        NSt = 15
    
    if NS == str("2+"):
        NSt = 14

    if NS == str("2"):
        NSt = 13

    if NS == str("2-"):
        NSt = 12

    if NS == str("3+"):
        NSt = 11

    if NS == str("3"):
        NSt = 10

    if NS == str("3-"):
        NSt = 9

    if NS == str("4+"):
        NSt = 8

    if NS == str("4"):
        NSt = 7

    if NS == str("4-"):
        NSt = 6

    if NS == str("5+"):
        NSt = 5

    if NS == str("5"):
        NSt = 4

    if NS == str("5-"):
        NSt = 3

    if NS == str("6+"):
        NSt = 2

    if NS == str("6"):
        NSt = 1
    

    if NM == str("1"):
        NMt = 16

    if NM == str("1-"):
        NMt = 15
    
    if NM == str("2+"):
        NMt = 14

    if NM == str("2"):
        NMt = 13

    if NM == str("2-"):
        NMt = 12

    if NM == str("3+"):
        NMt = 11

    if NM == str("3"):
        NMt = 10

    if NM == str("3-"):
        NMt = 9

    if NM == str("4+"):
        NMt = 8

    if NM == str("4"):
        NMt = 7

    if NM == str("4-"):
        NMt = 6

    if NM == str("5+"):
        NMt = 5

    if NM == str("5"):
        NMt = 4

    if NM == str("5-"):
        NMt = 3

    if NM == str("6+"):
        NMt = 2

    if NM == str("6"):
        NMt = 1
    
    return NSt, NMt

NSt, NMt = nt(Note)

Num1 = NSt + NSt + NMt + NMt + NMt
NEt = Num1 / 5
NEtr = round(NEt)
def Ndt(NEtr):
    if NEtr == 16:
        NE = str("1")

    if NEtr == 15:
        NE = str("2+")

    if NEtr == 13:
        NE = str("2")

    if NEtr == 12:
        NE = str("2-")

    if NEtr == 11:
        NE = str("3+")

    if NEtr == 10:
        NE = str("3")  

    if NEtr == 9:
        NE = str("3-")  

    if NEtr == 8:
        NE = str("4+")

    if NEtr == 7:
        NE = str("4")

    if NEtr == 6:
        NE = str("4-")

    if NEtr == 5:
        NE = str("5+")

    if NEtr == 4:
        NE = str("5")

    if NEtr == 3:
        NE = str("5-")

    if NEtr == 2:
        NE = str("6+")

    if NEtr == 1:
        NE = str("6")

    return NE

NE = Ndt(NEtr)
print ("Endnote ist:", NE)
#debug()
