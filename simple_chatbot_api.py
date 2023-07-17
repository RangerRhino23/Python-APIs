import openai

#Version: 1.0

###SETUP###
#REQUIREMENTS: user_input = input("User Input: ")

#Import api: import assets.APIs.simple_chatbot_api as sca

#When needed: chatbot_response = sca.chatbot(user_input)
#After chatbot_response = sca.chatbot(user_input): print(chatbot_response)

def chatbot(user_input):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt = user_input
    )
    return response.choices[0].text