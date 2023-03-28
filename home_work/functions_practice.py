def hello():
    print("Hello User")

def pack(car, brand, year):
    print[car, brand, year]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunch box is empty")
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"First I eat {list[0]}")
            else: 
                print(f"Next I eat {list[i]}")

    