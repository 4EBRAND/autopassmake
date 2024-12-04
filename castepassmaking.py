def generate_sindh_caste_passwords():
    # List of Sindhi castes (expandable)
    sindh_castes = [
        "rind", "mallah", "magsi", "solangi", "khaskheli", "jamali",
        "sial", "chandio", "brohi", "kalhoro", "qazi", "khoso",
        "laghari", "jatoi", "baloch", "pirzado", "rajput", "lashari",
        "shah", "syed", "abbasi", "samoon", "memon", "zardari",
        "gabol", "mehr", "panhwar", "mahar", "burdi", "leghari",
        "umrani", "bhutto", "shar"
    ]

    # Define 20 high-probability password patterns
    patterns = [
        "{caste}123", "{caste}786", "{caste}007", "{caste}000", "{caste}999",
        "786{caste}", "123{caste}", "pak{caste}", "sindh{caste}", "{caste}sindh",
        "{caste}1122", "{caste}555", "{caste}2024", "{caste}123456", "{caste}king",
        "{caste}786786", "{caste}111", "{caste}pak", "786786{caste}", "{caste}boss"
    ]

    # Generate passwords for all castes
    all_passwords = set()
    for caste in sindh_castes:
        caste_passwords = [pattern.format(caste=caste) for pattern in patterns]
        all_passwords.update(caste_passwords)

    # Save all passwords to a file
    with open("sindh_caste_passwords.txt", "w") as file:
        for password in sorted(all_passwords):
            file.write(password + "\n")
    
    print(f"Generated {len(all_passwords)} caste-based passwords and saved to 'sindh_caste_passwords.txt'.")
    
    # Interactive mode: Generate passwords for a specific caste
    while True:
        user_input = input("Enter a caste name to generate 20 passwords (or type 'exit' to quit): ").strip().lower()
        if user_input == "exit":
            break
        if user_input:
            specific_passwords = [pattern.format(caste=user_input) for pattern in patterns]
            print(f"\nPasswords for '{user_input}':")
            for password in specific_passwords:
                print(password)
            print("\n")

# Run the function
generate_sindh_caste_passwords()
