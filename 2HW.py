"""
user_firstname_and_surname = input("Введіть свое им'я через пробіл. ")
if len (user_firstname_and_surname) > 1:
  fname_sname = user_firstname_and_surname.split() # split ділить на слова
  initials = fname_sname[0][0].upper() + "." + fname_sname[1][0].upper()  + "." #upper пише з великої літери
  print("oк, ваші ініциали:", initials)
else:
    print("ваше им'я має мати більше символів!")
"""
"""
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
        """
"""
list_of_numbers = [1, 2, 3, 4, 5]
user_number = int(input("яке число добаємо? "))
print("список без смін: ", (list_of_numbers))
if user_number in list_of_numbers:
  print("введене число вже є в списку! ")
else:
  list_of_numbers.append (user_number)
  print("ось так виглядає список після змін:", list_of_numbers)
"""


