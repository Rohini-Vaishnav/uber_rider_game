print("Welcome to Uber🛺... Happy Ride😇...!")
print("....................")
import random
print("you have 5 rider👨🏻‍🦱")
print("..................")
print()
def place():
    ride_km1=0
    ride_km2=0
    ride_km3=0
    ride_km4=0
    ride_km5=0
    count_ride1=0
    count_ride2=0
    count_ride3=0
    count_ride4=0
    count_ride5=0
    sum_of_km_r1=0
    sum_of_km_r2=0
    sum_of_km_r3=0
    sum_of_km_r4=0
    sum_of_km_r5=0
    i=1
    while i<6:
        rider_place=["huskur","electronic city","shivaji nagar","avlahalhi","sarjapur"]
        place_rider1=random.choice(rider_place)
        place_rider2=random.choice(rider_place)
        place_rider3=random.choice(rider_place)
        place_rider4=random.choice(rider_place)
        place_rider5=random.choice(rider_place)
        print(" rider1 is in",place_rider1,"\n","rider2 is in",place_rider2,"\n","rider3 is in",place_rider3,"\n","rider4 is in",place_rider4,"\n","rider5 is in",place_rider5,"\n")
        customer=input("enter your rider number which is near by you😌:- ")
        print()
        user=input("if you want to book the ride write book✅ and if you want to cancel the ride write cancel🚫:- ")
        print()
        if user=="book":
            if customer=="rider1":
                print("now your rider1 is in",place_rider1)
                list=[206,304,507,459,151,701]
                list1=random.choice(list)
                sum_of_km_r1=sum_of_km_r1+list1
                list2=list1*5
                ride_km1=ride_km1+list2
                count_ride1+=1
            elif customer=="rider2":
                print("now your rider2 is in",place_rider2)
                list=[200,308,500,457,155,708]
                list1=random.choice(list)
                sum_of_km_r2=sum_of_km_r2+list1
                list2=list1*5
                ride_km2=ride_km2+list2
                count_ride2+=1
            elif customer=="rider3":
                print("now your rider3 is in",place_rider3)
                list=[204,301,505,458,159,707]
                list1=random.choice(list)
                sum_of_km_r3=sum_of_km_r3+list1
                list2=list1*5
                ride_km3=ride_km3+list2
                count_ride3+=1
            elif customer=="rider4":
                print("now your rider4 is in",place_rider4)
                list=[202,303,501,454,153,701]
                list1=random.choice(list)
                sum_of_km_r4=sum_of_km_r4+list1
                list2=list1*5
                ride_km4=ride_km4+list2
                count_ride4+=1
            elif customer=="rider5":
                print("now your rider5 is in",place_rider5)
                list=[205,300,507,454,156,709]
                list1=random.choice(list)
                sum_of_km_r5=sum_of_km_r5+list1
                list2=list1*5
                ride_km5=ride_km5+list2
                count_ride5+=1
        elif user=="cancel":
            continue
        i+=1
    if ride_km1!=0:
        print("today rider1 earn",ride_km1,"💰💰. and the rider ride",sum_of_km_r1,"km🛣️","today rider1 ride",count_ride1,"time")
    if ride_km2!=0:
        print("today rider2 earn",ride_km2,"💰💰. and the rider ride",sum_of_km_r2,"km🛣️","today rider2 ride",count_ride2,"time")
    if ride_km3!=0:
        print("today rider3 earn",ride_km3,"💰💰. and the rider ride",sum_of_km_r3,"km🛣️","today rider3 ride",count_ride3,"time")
    if ride_km4!=0:    
        print("today rider4 earn",ride_km4,"💰💰. and the rider ride",sum_of_km_r4,"km🛣️","today rider4 ride",count_ride4,"time")
    if ride_km5!=0:    
        print("today rider5 earn",ride_km5,"💰💰. and the rider ride",sum_of_km_r5,"km🛣️","today rider5 ride",count_ride5,"time")
place()