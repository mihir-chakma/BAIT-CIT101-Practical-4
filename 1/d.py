# Input your mail address and display the user name and the domain separately 

email = input("Enter Your Mail Address: ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
result = (f"Your user name is '{user_name}' and your domain is '{domain_name}'")
print(result)

