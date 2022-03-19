# Handling exceptions (errors) is crucial in python programs
# so that instead of the program stopping, it continues in some other way.
import this


game_not_ended = False
while not game_not_ended:
    try:
        weight = int(input("Enter weight(kg): "))
    except ValueError as sus:
        print(f"{sus}")
        continue
    else:
        continue
    finally:
        choice = str(input("Continue? (yes/no): ")).lower()
        if choice == "yes":
            game_not_ended = False
        elif choice == "no":
            game_not_ended = True
        else:
            raise Exception("Invalid choice!")

# You try the code that might cause an error

# try:
#     this

# If there is an error, you catch it and do something else

# except SomeError as error:
#     print(error)

# If there is no error, do this

# else:
#     continue

# After everything, no matter what, do this
# finally:
#   print('well done!')
