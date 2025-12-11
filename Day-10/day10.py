# convert integers into string

age = 24;

#print("my age is: " + age) 
# ==> هنا هيطلع error عشان مينفعش اجمع بين Integer و String 

# وعشان نحل المشكلة دي عندنا function في python بتحول ال integer الي string
# str()

print("my age is: " + str(age)) # ==> my age is: 24;

###############################################################################

# طيب انا لو عندي متغير ومخزن فيه قيمة string وعاوز العب  في شكل النص 

name = "ahmed"
name2 = "AHMED"
sentence = "my name is ahmed, i love programming"

# capital ==> upper()
print(name.upper()) # ==> AHMED 
# دي ببساطة خلت كل الحروف ال name حروف capital

# small ==> lower()
print(name2.lower()) # ==> ahmed
# دي عكس اللي فاتت دي حولت الحروف من capital الي small

# capitalize ==> capitalize
print(sentence.capitalize()) # ==> My name is ahmed, i love programming
# دي ببساطة هتخلي اول حرف بس capital لكن باقي الجملة هتكون زي ما هي

# title ==> title ()
print(sentence.title()) # My Name Is Ahmed, I Love Programming
# ودي ببساطة هتخلي اةل حرف من كل كلمة يتحول الي capital

