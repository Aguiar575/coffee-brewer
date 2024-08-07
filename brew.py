import time
import sys
import threading
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\rWaiting {remaining} seconds...")
        sys.stdout.flush()
        time.sleep(1)
    clear_sceen()

def loading_spinner():
    spinner = ['|', '/', '-', '\\']
    while not stop_loading:
        for symbol in spinner:
            sys.stdout.write(f"\rWaiting {symbol} ")
            sys.stdout.flush()
            time.sleep(0.1)

def tetsu_kasuya_pour(coffee_amount, ratio, delay_seconds):
    # Calculate the total water amount based on the ratio
    total_water = coffee_amount * ratio

    # Display total water and wait for user input
    print(f"The total water should be: {total_water} grams")

    global stop_loading
    stop_loading = False
    spinner_thread = threading.Thread(target=loading_spinner)
    spinner_thread.start()

    input("Press Enter to continue...")
    stop_loading = True
    spinner_thread.join()

    clear_screen()

    # Initial Bloom Pour (1:2 ratio)
    bloom_pour = coffee_amount * 2
    print(f"Initial Bloom Pour: {bloom_pour} grams (1:2 ratio)")
    print(f"Waiting {delay_seconds} seconds for bloom...")
    countdown(delay_seconds)

    # Second Pour (total 60% of target brew weight)
    second_pour_total = total_water * 0.6
    second_pour = second_pour_total - bloom_pour
    print(f"Second Pour: Add {second_pour} grams (total {second_pour_total} grams)")
    print(f"Waiting {delay_seconds} seconds for second pour...")
    countdown(delay_seconds)

    # Third Pour (total 80% of target brew weight)
    third_pour_total = total_water * 0.8
    third_pour = third_pour_total - second_pour_total
    print(f"Third Pour: Add {third_pour} grams (total {third_pour_total} grams)")
    print(f"Waiting {delay_seconds} seconds for third pour...")
    countdown(delay_seconds)

    # Fourth Pour (total 90% of target brew weight)
    fourth_pour_total = total_water * 0.9
    fourth_pour = fourth_pour_total - third_pour_total
    print(f"Fourth Pour: Add {fourth_pour} grams (total {fourth_pour_total} grams)")
    print(f"Waiting {delay_seconds} seconds for fourth pour...")
    countdown(delay_seconds)

    # Final Pour (total 100% of target brew weight)
    final_pour = total_water - fourth_pour_total
    print(f"Final Pour: Add {final_pour} grams (total {total_water} grams)")
    print(f"Waiting {delay_seconds} seconds for final pour...")
    countdown(delay_seconds)

def main():
    coffee_amount = 20  # Coffee amount in grams
    ratio = 16  # Water-to-coffee ratio (e.g., 1:16)
    delay_seconds = 45  # Delay in seconds between pours

    tetsu_kasuya_pour(coffee_amount, ratio, delay_seconds)

if __name__ == "__main__":
    main()


