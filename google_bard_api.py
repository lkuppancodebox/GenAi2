from bardapi import BardCookies
def send_query_to_ai (prompt):
    cookie_dict = {
        "__Secure-1PSID": "___ your key ___",
        "__Secure-1PSIDTS": "___ your key ____",
    }

    try:
        bard = BardCookies(cookie_dict=cookie_dict)
        response = bard.get_answer(prompt)
        return (response['content'])
    except:
        print("Cookie update required")
        return None
