print("welcome to uber...! happy ride ")
print("....................")
import random
print("you have 5 rider")
print("..................")
print()
def place():
    i=0
    s1=0
    s2=0
    s3=0
    s4=0
    s5=0
    while i<2:
        rider_place=["huskur","electronic city","shivaji nagar","avlahalhi","sarjapur"]
        place_rider1=random.choice(rider_place)
        place_rider2=random.choice(rider_place)
        place_rider3=random.choice(rider_place)
        place_rider4=random.choice(rider_place)
        place_rider5=random.choice(rider_place)
        print(" rider1 is in",place_rider1,"\n","rider2 is in",place_rider2,"\n","rider3 is in",place_rider3,"\n","rider4 is in",place_rider4,"\n","rider5 is in",place_rider5,"\n")
        customer=input("enter your rider number which is near by you:-")
        user=input("if you want to book the ride write book and if you want to cancel the ride write cancel:- ")
        if user=="book":
            if customer=="rider1":
                print("now your rider1 is in",place_rider1)
                list=[20,30,50,45,15,70]
                list1=random.choice(list)
                list2=list1*5
                s1=s1+list2
            if customer=="rider2":
                print("now your rider2 is in",place_rider2)
                list=[20,30,50,45,15,70]
                list1=random.choice(list)
                list2=list1*5
                s2=s2+list2
            if customer=="rider3":
                print("now your rider3 is in",place_rider3)
                list=[20,30,50,45,15,70]
                list1=random.choice(list)
                list2=list1*5
                s3=s3+list2
            if customer=="rider4":
                print("now your rider4 is in",place_rider4)
                list=[20,30,50,45,15,70]
                list1=random.choice(list)
                list2=list1*5
                s4=s4+list2
            if customer=="rider5":
                print("now your rider5 is in",place_rider5)
                list=[205,300,507,45,15,70]
                list1=random.choice(list)
                list2=list1*5
                s5=s5+list2
        if user=="cancel":
            continue
        i+=1
    print("today rider1 earn",s1,"rs.")
    print("today rider2 earn",s2,"rs.")
    print("today rider3 earn",s3,"rs.")
    print("today rider4 earn",s4,"rs.")
    print("today rider5 earn",s5,"rs.")
place()