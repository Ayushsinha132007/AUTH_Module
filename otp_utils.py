import pyotp
import qrcode

def generate_otp_secret():
    secret = pyotp.random_base32()
    print("Scan this QR in Google Authenticator App:")
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name="YourApp", issuer_name="SecureLogin")
    img = qrcode.make(uri)
    img.show()
    return secret

def verify_otp(secret, otp_input):
    totp = pyotp.TOTP(secret)
    return totp.verify(otp_input)
