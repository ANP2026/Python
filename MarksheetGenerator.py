english = int(input("Enter your english marks"))
coding = int(input("Enter your coding marks"))
math = int(input("Enter your math marks"))
science = int(input("Enter your science marks"))
social_studies = int(input("Enter your social studies marks"))

total=(english+coding+math+science+social_studies)
per=(total/500)*100
print("Total out of 500 is equal to :", total)
print("Percentage is :", per)
if per >= 90:
    print("Grade is equal to A1")
elif per>=80:
    print("Grade is equal to A2")
elif per>=70:
    print("Grade is equal to B1")
elif per>=60:
    print("Grade is equal to B2")
elif per>=50:
    print("Grade isi equal to C1")
elif per>=40:
    print("Grade is equal to C2")
elif per>=30:
    print("Grade is equal to D1")
elif per>=20:
    print("Grade is equal to D2")