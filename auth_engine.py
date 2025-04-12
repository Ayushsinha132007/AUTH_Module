import bcrypt
from database import add_user, get_user
from otp_utils import generate_otp_secret, verify_otp

def register_user(username, password):
    otp_secret = generate_otp_secret()
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    if add_user(username, password_hash, otp_secret):
        print(f"[✓] User registered. Scan this OTP key in Google Authenticator: {otp_secret}")
    else:
        print("[✗] Username already exists.")

def login_user(username, password, otp_input):
    user = get_user(username)
    if not user:
        print("[✗] User not found.")
        return False

    stored_hash = user[2]
    otp_secret = user[3]

    if bcrypt.checkpw(password.encode(), stored_hash):
        if verify_otp(otp_secret, otp_input):
            print("[✓] Login successful.")
            return True
        else:
            print("[✗] Invalid OTP.")
    else:
        print("[✗] Wrong password.")
    return False
