from research import research_company
from email_generator import generate_email

company_name = input("Enter organisation name: ")

company_data = research_company(company_name)

email = generate_email(company_data)

print("\nGenerated Outreach Email:\n")
print(email)