grader = int(input("HVor mange grader er det ute? "))

if grader < 15:
    print("Ta på jakke!")
    type = input("Regner det?")
    if type.lower() == "ja":
        print("Ta med paraply")
else:
    print("Ha en fin dag i varmen!")

