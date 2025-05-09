import google.generativeai as gen
import os

gen.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

model = gen.GenerativeModel('gemini-2.0-flash')

response = model.generate_content("Gere um código em python que o usuário digite dois números, informe a operação.")

print(response.text)