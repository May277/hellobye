import google.generativeai as genai

genai.configure(api_key="AIzaSyCVYXfVaEUEJi4rtdoWi6_6jPRSIf3BBPk")



pip --version

model = genai.GenerativeModel("gemini-1.5-flash")

print("AI Chatbot (type 'exit' to stop)")

while True:
    user = input("You: ")
    
    if user.lower() == "exit":
        break
    
    response = model.generate_content(user)
    print("AI:", response.text)