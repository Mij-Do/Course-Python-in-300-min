#طيب انا حاليا عايز ال user يكتب data معينة - او اخد منه data زي الاسم او العمر او غيره 
# بعمل ده عن طريق امر input()
# input();

#طيب انا لو عندي اكتر من input وعايز اوضح لل user انت هنا المفروض تكتب اسمك او هنا المفروض تكتب سنك وهكذا 
# الرسالة دي اقدرابعتها لل user ازاي ؟
# input("Enter Your Name: ");
# هكذا هيظهر لل user الرسالة دي وهيبدأ يكتب أسمه

# طيب ال data دي انا اقدر ابعتهالل user تاني ازاي ؟
# عن طريق اني احفظ ال input + value اللي هيكتبها ال user في variable
userName = input("Enter Your Name: "); # => 1

# واطبعها عن طريق امر print
print ("Your Name is: "+userName); # => 2

################################################

# ملحوظة مهمة 
# اي حاجة بيكتبها ال user في ال input تلقائيا بتتخزن ك string type 
# طيب لو انا عاوز العمر مثلا اللي دخله ال user يبقي integer زي ما هو اعمل ايه ؟
# هنا يجي دور int()
# وهي function بتحول اي string الي integer
userAge = int(input("Enter your Age: ")); # => 1
print("Your Age is: "+ str(userAge)) # هنا انا مينفعش اسيب ال userAge تبقي integer زي ما هي 
# كان لازم ارجعها string عشان مينفعش اجمع بين string و integer 
# هيرجع Error 
# بس الفرق هنا عن الاول ان ال useraAge محتفظ ب integer type زي ما هو 
# والتغير بس تم في حالة الطباعة 
