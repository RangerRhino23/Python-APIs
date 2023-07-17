
#Version: 1.0

###SETUP###

#Import api: import assets.APIs.bard_chatbot_api as bc


'''
prompt = input('User: ')
chatbot_response = bc.get_response(prompt)
print(f'Chatbot: {chatbot_response}')
'''
def get_response(prompt):
    from bardapi import Bard
    import os
    os.environ['_BARD_API_KEY']="BARD API KEY HERE"

    input_text = prompt
    chatbot_response = Bard().get_answer(input_text)['content']

    return chatbot_response



'''
bc.chatbot_session()
'''
def chatbot_session():
    from bardapi import Bard
    import os
    import requests

    os.environ['_BARD_API_KEY']="BARD API KEY HERE"

    session = requests.Session()
    session.headers = {
                "Host": "bard.google.com",
                "X-Same-Domain": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Origin": "https://bard.google.com",
                "Referer": "https://bard.google.com/",
            }
    session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 

    bard = Bard(session=session, timeout=30)

    while True:
        input_text = input("User: ")
        if input_text.lower() == 'exit':
            break
        chatbot_response = bard.get_answer(input_text)['content']
        print(f'Chatbot: {chatbot_response}')