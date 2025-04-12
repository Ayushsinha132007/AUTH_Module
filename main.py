from auth_engine import register_user, login_user
from database import create_user_table

def main():
    create_user_table()
    while True:
        print("\n--- Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            username = input("Choose username: ")
            password = input("Choose password: ")
            register_user(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            otp = input("Enter OTP from app: ")
            login_user(username, password, otp)

        elif choice == '3':
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
