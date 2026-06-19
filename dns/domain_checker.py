blacklist = [
    "malicious-site.com",
    "fakebank.com"
]

def check_domain(domain):
    return domain in blacklist
