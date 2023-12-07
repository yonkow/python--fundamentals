company = {}
while True:
    command = input().split(" -> ")
    if len(command) == 1:
        break
    current_company, current_id = command[0], command[1]
    if current_company in company:
        if current_id not in company[current_company]:
            company[current_company] += [current_id]
    elif current_company not in company:
        company[current_company] = []
        company[current_company] += [current_id]

for company_name, employee in company.items():
    print(f"{company_name}")
    for name in employee:
        print(f"-- {name}")