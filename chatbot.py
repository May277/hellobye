import google.generativeai as genai

genai.configure(api_key="PASTE_YOUR_NEW_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")

print("AI Chatbot (type 'exit' to stop)")

while True:
    user = input("You: ")
    
    if user.lower() == "exit":
        break
    
    response = model.generate_content(user)
    print("AI:", response.text)