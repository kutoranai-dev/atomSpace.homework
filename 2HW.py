#Task 1
user_firstname_and_surname = input("Введіть свое им'я через пробіл. ")
if len (user_firstname_and_surname) > 1:
  fname_sname = user_firstname_and_surname.split() # split ділить на слова
  initials = fname_sname[0][0].upper() + "." + fname_sname[1][0].upper()  + "." #upper пише з великої літери
  print("oк, ваші ініциали:", initials)
else:
    print("ваше им'я має мати більше символів!")

#Task 2
user_email = input("Введіть свой email з закінченням .org or .com ")
if len(user_email) > 3 and "@" in user_email:
    part_email = user_email.split("@")
    name = part_email[0]
    after_name = part_email[1]
    if len(name) > 2:
        camouflage = name[0] + "*" * (len(name) -2) + name[-1]
        hidden_name = camouflage + "@" + after_name
        print(hidden_name)
    else:
      print("ваше email не підходить.")
      
#Task 3
list_of_numbers = [1, 2, 3, 4, 5]
user_number = int(input("яке число добавляємо? "))
print("список без смін: ", (list_of_numbers))
if user_number in list_of_numbers:
  print("введене число вже є в списку! ")
else:
  list_of_numbers.append (user_number)
  print("ось так виглядає список після змін:", list_of_numbers)


#Task 4
user1_interests = input("введіть свої інтереси:").split(",")
user2_interests = input("введіть свої інтереси:").split(",")
tags_user1 = set()
tags_user2 = set()
if len (user1_interests) > 0 and len(user2_interests) > 0:
  tags_user1.update(user1_interests)
  tags_user2.update(user2_interests)
  common_tags = tags_user1.intersection(tags_user2)
  all_tags = tags_user1.union(tags_user2)
    
  print("спільні інтереси:", common_tags)
  print("усі інтереси:", all_tags)
else:
    print("помилка")

#Task 5 
user_number = input("введіть числа через пробіл: ")

numbers = user_number.split()

all_numbers = True

for i in range(len(numbers)):
    if not numbers[i].isdigit():
        all_numbers = False
        break

if all_numbers:
    if len(numbers) >= 3:
        sum_three_num = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
        print("сума перших трьох:", sum_three_num)
    else:
        print("потрібно мінімум 3 числа ")
else:
    print("помилка: введено не числа ")
