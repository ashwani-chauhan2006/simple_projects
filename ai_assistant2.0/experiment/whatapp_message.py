import pywhatkit as pwk

# Correct phone number format
phone_number = "+91830738405"  # Replace with the recipient's phone number
message = "Hello, this is an instant message from pywhatkit."

# Send the WhatsApp message instantly
pwk.sendwhatmsg_instantly(phone_number, message)

print("Message sent successfully!")
