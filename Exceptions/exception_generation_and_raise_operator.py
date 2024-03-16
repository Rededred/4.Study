try:
    age = int(input("input age there: "))
    if not 1 < age < 110:
        raise Exception("Wrong age! -------------")
    print("Your age: ", age)
except ValueError:
    print("Wrong data input")
except Exception as e:
    print(e)
print("That's all")
