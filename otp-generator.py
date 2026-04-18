# OTP Generator with Time Limit Automatically Send on Email 
 
import random  
import time 
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   

print("🥷 Welcome to Secure Login System") 

email = input("📧 Enter your Email: ") 

# Generate OTP 
otp = random.randint(100000,999999)  
expiry_time = time.time() + 120  # OTP valid for 2 minutes(120 seconds)   
attempts = 3  

# --- Email Part ---  
sender_email = "rameshgehlot2210@gmail.com" 
sender_password = "wcos fdvg xedf nvvl" 
receiver_email = email 

msg = MIMEMultipart("alternative") 
msg["From"]    = sender_email
msg["To"]      = receiver_email
msg["Subject"] ="Your OTP!"  

html_body = f"""
<html>
  <body>
    <h2 style="color: red;">Secure System! 🧑‍💻</h2>
    <p><b>Hi! Your OTP To Access Secure System is [{otp}]</b></p> 
    <p><strong>Valid for 2 Minutes. Don't Share with Anyone</strong></p>  
  </body>
</html> 
"""  
msg.attach(MIMEText(html_body, "html")) 

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())  

print("\n💬 OTP has been sent to your Email") 
# print("(Practice mode OTP:", otp )  # remove in production 

# Main loop for OTP verification 
while attempts > 0:  
    user_otp = input("Enter OTP: ") 
    
    if time.time() > expiry_time:
        print("⏰ OTP expired! Please request a new one.") 
        break 
    
    if user_otp == str(otp):
        print("✅ OTP verified! Access granted.")
        break
    
    else:
        attempts -= 1
        print(f"❌ Incorrect OTP! Attempts left: {attempts}") 
        
    if attempts == 0:
        print("🚫 No more attempts left.") 
        break 
        