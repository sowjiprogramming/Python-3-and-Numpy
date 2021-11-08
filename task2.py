def mark_grade(a):
    if a >= 90:
        print("you got A grade congratulations.")
        
    elif a >= 80:
        print("yougot B grade congratulations.")
        
    elif a >=50:
        print("you got C grade congratulations")
           
    else:
        print("sorry you r failed")

target_grade = input("what grade you r expecting a,b,c : ")
percentage = int(input("please enter yout percentage:"))
 
mark_grade(percentage)
 
comment_list = ["you exceeded expectation","you reached your expectation","work hard to reach your expectation"]
if percentage >=90:
    
    if target_grade == "a":
        print(comment_list[1])
    elif target_grade == "b" or "c":
            print(comment_list[0])
elif percentage >= 80:
    if target_grade == "b":
       print(comment_list[1])
    elif target_grade == "a":
        print(comment_list[2]) 
    elif  target_grade == "c":     
          print(comment_list[0])
elif percentage >= 50:
    if target_grade == "c":
      print(comment_list[1])
    elif target_grade == "a" or "b":                
         print(comment_list[2])    
