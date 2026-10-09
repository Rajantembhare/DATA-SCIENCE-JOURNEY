# 10. Password strength
pwd = "abc123"
if len(pwd) >= 8 and any(ch.isdigit() for ch in pwd) and any(ch.isalpha() for ch in pwd):
    print("Strong password")
else:
    print("Weak password")