import time
from datetime import datetime
import os

# Tool banner
def banner():
    print("\n" + "="*50)
    print("      🔁 Welcome to ViralGT  🔁")
    print("="*50 + "\n")

# Color support
def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Main Function
def echomancer():
    banner()

    name = input("👤 Enter name to repeat: ").strip()
    
    try:
        count = int(input("🔢 How many times to repeat (0 = unlimited): "))
    except ValueError:
        print("❌ Invalid number!")
        return

    use_color = input("🎨 Use color? (y/n): ").strip().lower() == "y"
    save_output = input("💾 Save output to file? (y/n): ").strip().lower() == "y"
    
    if save_output:
        file_name = f"echomancer_output_{int(time.time())}.txt"
        file = open(file_name, "w")

    print("\n🔁 Repeating now...\n")
    start = time.time()
    
    try:
        if count == 0:
            print("⚠️ Press Ctrl+C to stop infinite loop.\n")
            i = 1
            while True:
                output = f"{i}. {name}"
                final_output = colored(output, "92") if use_color else output
                print(final_output)
                if save_output:
                    file.write(output + "\n")
                i += 1
                time.sleep(0.1)
        else:
            for i in range(1, count + 1):
                output = f"{i}. {name}"
                final_output = colored(output, "94") if use_color else output
                print(final_output)
                if save_output:
                    file.write(output + "\n")
                time.sleep(0.05)
    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")
    
    end = time.time()
    duration = round(end - start, 2)
    print("\n📊 Summary:")
    print(f"🧾 Name: {name}")
    print(f"🔁 Repeated: {'∞ (infinite)' if count == 0 else count} times")
    print(f"🎨 Colored: {'Yes' if use_color else 'No'}")
    print(f"💾 Saved: {'Yes, in ' + file_name if save_output else 'No'}")
    print(f"⏱️ Time taken: {duration} seconds")
    print(f"📅 Finished on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if save_output:
        file.close()

# Run the tool
if __name__ == "__main__":
    echomancer()
