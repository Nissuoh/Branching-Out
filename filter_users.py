import json


def filter_users_by_name(name):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        filtered = [u for u in users if u["name"].lower() == name.lower()]
        if not filtered:
            print("Kein Benutzer gefunden.")
        for user in filtered:
            print(user)
    except FileNotFoundError:
        print("Datei users.json nicht gefunden.")


def filter_by_age(age):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        filtered = [u for u in users if u["age"] >= age]
        for user in filtered:
            print(user)
    except FileNotFoundError:
        print("Datei nicht gefunden.")


def filter_by_email(email_query):
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        filtered = [u for u in users if email_query.lower() in u["email"].lower()]
        for user in filtered:
            print(user)
    except FileNotFoundError:
        print("Datei nicht gefunden.")


def main():
    filter_option = input("What would you like to filter by? (name, age, email): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            age_to_filter = int(input("Enter minimum age: "))
            filter_by_age(age_to_filter)
        except ValueError:
            print("Bitte eine Zahl für das Alter eingeben.")

    elif filter_option == "email":
        email_to_search = input("Enter email or domain: ").strip()
        filter_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()