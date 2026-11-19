Tamrin 2


my_text = "International"

thetext = my_text[0] + my_text[6] + my_text[-1]

print(thetext)

first_text = "python"
second_text "progeram"

thetext = first_text[:3] + second_text[:3] + second_text[3:] + first_text[3:]

print(thetext)

my_text = """Throughout its run, The Vampire Diaries was generally well received by critics, who praised its acting, character development, emotional depth, and thematic elements. The concepts and characters developed in the series served to launch a media franchise that includes other television series, web series, novels and comic books. The television series The Originals (2013–2018) – which also aired on the CW – was the first major entry in this collection of connected works, followed by a spin-off of The Originals entitled Legacies (2018–2022), which aired on the CW as well. The Vampire Diaries significantly influenced the supernatural teen drama genre, contributing to a surge in vampire-themed media during the late 2000s and early 2010s.[6]"""

my_text = my_text.replace("(", " ")
my_text = my_text.replace(")", " ")
my_text = my_text.replace("[", " ")
my_text = my_text.replace("]", " ")
my_text = my_text.replace(".", " ")
my_text = my_text.replace(",", " ")
my_text = my_text.replace("–", " ")
my_text = my_text.replace("-", " ")

print(my_text)

print("Number of characters:", len(my_text))


Tamrin 3


my_list = [1,5,50,3,8,90]

number_index = my_list.index(8)

my_list[number_index] = 80

print(my_list)

my_list = [10,20,[300,400,[5000,6000],500],30,40]

my_list[2][2].append(7000)

print(my_list)

my_number = input("Enter number: ")

my_number = my_number.replace("0", "۰")
my_number = my_number.replace("1", "۱")
my_number = my_number.replace("2", "۲")
my_number = my_number.replace("3", "۳")
my_number = my_number.replace("4", "۴")
my_number = my_number.replace("5", "۵")
my_number = my_number.replace("6", "۶")
my_number = my_number.replace("7", "۷")
my_number = my_number.replace("8", "۸")
my_number = my_number.replace("9", "۹")

print(my_number)

username = "amirali"
password = "1245"

voroodi_user = input("Enter username: ")
voroodi_pass = input("Enter password: ")

if voroodi_user == username and voroodi_pass == password:
    print("Login successful! Dorost ast")

else:
    print("Username or password is wrong! Ghalat ast")


Tamrin 4


nomre_daneshjo = float(input("Enter your grade: "))

if nomre_daneshjo < 0 or nomre_daneshjo > 20:
    print("Wrong grade")

elif nomre_daneshjo < 10:
    print("Between 0 and 10")

elif nomre_daneshjo < 12:
    print("Between 10 and 12")

elif nomre_daneshjo < 16:
    print("Between 12 and 16")

elif nomre_daneshjo < 18:
    print("Between 16 and 18")

else:
    print("Between 18 and 20")

adad_aval = int(input("Enter first number: "))
adad_dovom = int(input("Enter second number: "))
adad_sevom = int(input("Enter third number: "))
adad_chaharom = int(input("Enter fourth number: "))
adad_panjom = int(input("Enter fifth number: "))

bozorgtarin = adad_aval
koochaktar = adad_aval

if adad_dovom > bozorgtarin:
    bozorgtarin = adad_dovom

if adad_sevom > bozorgtarin:
    bozorgtarin = adad_sevom

if adad_chaharom > bozorgtarin:
    bozorgtarin = adad_chaharom

if adad_panjom > bozorgtarin:
    bozorgtarin = adad_panjom

if adad_dovom < koochaktar:
    koochaktar = adad_dovom

if adad_sevom < koochaktar:
    koochaktar = adad_sevom

if adad_chaharom < koochaktar:
    koochaktar = adad_chaharom

if adad_panjom < koochaktar:
    koochaktar = adad_panjom

print("Biggest number:", bozorgtarin)
print("Smallest number:", koochaktar)

adad = int(input("Enter a number: "))

majmo = 0

for i in range(1, adad):
    if adad % i == 0:
        majmo = majmo + i

if adad > 0 and majmo == adad:
    print("Perfect Number")

else:
    print("Not Perfect Number")
