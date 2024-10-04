from langchain_groq import ChatGroq

import warnings
warnings.filterwarnings('ignore')

api_key = "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"
chat = ChatGroq(temperature=1, groq_api_key=api_key, model_name="mixtral-8x7b-32768")

def generate_blog_titles(content):
    try:
        print("Generating titles...")
        query = f"Suggest 3 creative blog titles for the following content:\n\n{content}"
        response = chat.invoke(query)
        titles = response.content
        return titles.split("\n")
    except Exception as e:
        print(f"Error: {e}")
        return ["An error occurred while generating the titles."]

##If you want to try the application locally.
# content = """NEW DELHI: External affairs minister S Jaishankar will be visiting Pakistan for the Shanghai Cooperation Organisation (SCO) meeting scheduled to take place on October 16 and 17.
# "The external affairs minister will lead our delegation to Pakistan to participate in the SCO summit which will be held in Islamabad on 15 and 16 October," said Randhir Jaiswal, external affairs ministry spokesperson."""

# titles = generate_blog_titles(content)
# print("Suggested Titles:")
# for title in titles:
#     print("- ", title)
