import re


def regex_email(str):
    valid_email = r'[a-z0-9_.-]+@[0a-z0-9.-]+.{3}[a-z]$'
    valid_pfx = r'^email:'
    valid_email_pfx = valid_pfx + valid_email
    pm = re.compile(valid_pfx)
    m = pm.match(str)
    if m:
        p = re.compile(valid_email_pfx, re.IGNORECASE, )
        m = p.match(str)
        if m:
            return m.group()
        else:
            return 'invalid email'

    else:
        print("No email prefix found. Searching for a valid email")
        p = re.compile(valid_email, re.IGNORECASE)
        m = p.match(str)
        if m:
            result = p.subn('email:'+m.group(), m.group())
            return result[0]
        else:
            print('invalid email')

    return 'invalid email'
