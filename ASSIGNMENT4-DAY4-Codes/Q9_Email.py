# Write a Python program that extracts all email addresses from a string 
# using a regular expression. Test it with the input: "Contact us at 
# support@example.com or info@company.org". 
import re

STRING="Contact us at support@example.com or info@company.org"


EMAIL=re.findall(r"\w+@\w+.\w+", STRING)
print(f"Here are your extracted email {EMAIL}")