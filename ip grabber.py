
import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return None

# Prompt the user to enter a website URL
website_url = input("Enter the website URL: ")

# Call the function to retrieve the IP address
ip = get_ip_address(website_url)

# Check if IP address was successfully obtained
if ip:
    print("The IP address of", website_url, "is:", ip)
else:
    print("Unable to retrieve the IP address.")
