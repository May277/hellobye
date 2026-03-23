import google.generativeai as genai

# 🔑 Put your API key here
genai.configure(api_key="AIzaSyDqcjZ7LlKJhEZmtSoSBX5J5nMhYwShDRs")

# Create model
model = genai.GenerativeModel("gemini-pro")

# Ask something
response = model.generate_content("Explain AI in simple words")

# Print result
print(response.text)