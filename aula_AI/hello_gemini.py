import google.generativeai as gen
import os

gen.configure(api_key=os.environ['GEMINI_API_KEY'])

model = gen.GenerativeModel('gemini-2.0-flash')

response = model.generate_content("gen, ensine para uma criança de 9 anos como resolver multiplicação de frações.")

print(response.text)