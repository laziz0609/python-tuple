emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))

def cut_domain(eamils: tuple) -> list:
    domains = []
    
    for email in emails:
        inx = email[1].find("@")
        
        domains.append(email[1][inx:])
    
    return domains

print(cut_domain(emails))