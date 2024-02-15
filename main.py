while True:
        try:
                print()
                val1 = float(input("Enter decmal value 1: "))
                val2 = float(input("Enter decmal value 2: "))
                val3 = float(input("Enter decmal value 3: "))
                print()
                
                avg = val1 + val2 + val3
                
                if avg < 200000:
                    print("average")
                elif avg >= 200000 and avg < 400000:
                    print("rich")
                elif avg >= 400000 and avg < 600000:
                    print("super rich")
                else:
                    print("crazy rich")
        except ValueError:
                print("Invalid input")
                break

