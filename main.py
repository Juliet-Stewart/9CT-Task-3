import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
climate_data = pd.read_csv("climate_data.csv")

#Give the user options
while True:
    print("\n=== Climate Data Viewer ===")
    print("1. View full dataset")
    print("2. View temperature graph")
    print("3. Exit")

    choice = input("Choose an option (1–3): ")

    if choice == "1":
        print(climate_data)

    elif choice == "2":
        plt.plot(aus_data["Year"], aus_data["Australia Avg Temp (°C)"], label="Australia")
        plt.plot(global_data["Year"], global_data["Global Avg Temp (°C)"], label="Global")
        plt.xlabel("Year")
        plt.ylabel("Temperature (°C)")
        plt.title("Australia vs Global Temperatures")
        plt.legend()
        plt.grid(True)
        plt.show()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
