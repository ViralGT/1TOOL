#repeat_name.py

# Naam input lo
name = input("what is your name : ")

# Digit input lo (aur ensure karo ki wo number hi ho)
try:
    count = int(input("Kitni baar print karna hai?  "))
    
    print("\n--- Output ---")
    for i in range(count):
        print(f"{i+1}. {name}")
except ValueError:
    print("❌ Error: Sirf digit hi daal le !")
