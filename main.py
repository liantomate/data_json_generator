if __name__ == "__main__":
    print("Choose generator to use: ")
    print("[1] Island Data Generator")
    print("[2] Level Data Generator")
    print("[3] Questionnaire Round Data Generator")

    choice = input("Enter choice: ")
    if choice == "1":
        from island_data_json import call
        call()
    elif choice == "2":
        from level_data_json import call
        call()
    elif choice == "3":
        from round_data_0_json import call
        call()
    else:
        print("Invalid choice")