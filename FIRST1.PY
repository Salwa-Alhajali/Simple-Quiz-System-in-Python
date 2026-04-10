#تطوير انه المستخدم يدخل عدد الاسئلة ونوع الاحرف الي ممكن تدخل او ارقام مثلا 

sumw=0
def answer(a):
    global sumw 
    A=input("enter the student answer")
    if a==A:
        sumw =sumw + 1
    else:
        print ("your answer is not corict")



list=[input("enter the1 answer"),input("enter the2 answer"),input("enter the3 answer"),input("enter the4 answer"),input("enter the5 answer"),input("enter the6 answer"),input("enter the7 answer")]
for i in list:
    answer(i)
print (f"the sum is {sumw}")