import google.generativeai as genai
import PIL.Image
import pyttsx3


genai.configure(api_key="sua-api-key")

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')
img = PIL.Image.open('exemplo-livro.jpeg')
response = model.generate_content(img)

print("Resposta 1:", response.text)

response = model.generate_content(["Descreva todo texto e informações da foto para pessoa com cegueira total ter acesso", img])
# response.resolve()

description = response.text
print("Resposta: ", description)


def vocalizar_descricao():    
    if description:
        engine = pyttsx3.init()
        
        engine.setProperty('rate', 150)
        
        engine.say(description)
        engine.runAndWait()

vocalizar_descricao()