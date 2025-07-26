import time
import sys
import random

def colorful_text(text):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    return random.choice(colors) + text + reset

def repeat_name():
    while True:
        print("\n🔁 Welcome to the Name Repeater Tool 🔁\n")
        
        name = input("👉 Apna naam daalo: ").strip()
        if not name.isalpha():
            print("❌ Error: Naam sirf letters me hona chahiye!")
            continue

        try:
            count = int(input("🔢 Kitni baar print karna hai? (1 se 100 ke beech): "))
            if count < 1 or count > 100:
                print("❌ Error: Sirf 1 se 100 ke beech number daalo!")
                continue
        except ValueError:
            print("❌ Error: Sirf valid digit daalo bhai!")
            continue

        print("\n✅ Repeating now...\n")
        output_lines = []
        for i in range(1, count + 1):
            line = f"{i}. {name}"
            colored = colorful_text(line)
            print(colored)
            output_lines.append(line)
            time.sleep(0.05)  # smooth output

        save = input("\n💾 Output file me save karein? (y/n): ").lower()
        if save == 'y':
            with open("repeated_names.txt", "w") as file:
                file.write("\n".join(output_lines))
            print("✅ Saved to repeated_names.txt")

        again = input("\n🔁 Phir se run karein? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Bye-bye! Shukriya tool use karne ke liye.\n")
            break

if __name__ == "__main__":
    repeat_name()
