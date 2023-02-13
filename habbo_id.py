import requests
import pyperclip as clipboard



habbo_id = input("Escribe el nombre del keko: ")

habbo_keko = requests.get(f"https://www.habbo.es/api/public/users?name={habbo_id}")


id = habbo_keko.json()['uniqueId']


clipboard.copy(id)

clipboard.paste()


print("ID Copiado al portapapeles")
