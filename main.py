import requests

print('''
██ ██████      ██       ██████   ██████  █████  ████████  ██████  ██████  
██ ██   ██     ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██ ██████      ██      ██    ██ ██      ███████    ██    ██    ██ ██████  
██ ██          ██      ██    ██ ██      ██   ██    ██    ██    ██ ██   ██ 
██ ██          ███████  ██████   ██████ ██   ██    ██     ██████  ██   ██ 
''')
print("---H3ll0---")
print("---https://github.com/Ashy2discord---")
print("---'azzshy' sur discord---")
print('''1 -> Simple IP locator
2 -> À propos     
''')

choix_utilisateur = input("Entre ton choix: ")

if choix_utilisateur == '1':
    def get_ip_info(ip_address):
        url = f"http://ipinfo.io/{ip_address}/json"
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                return {
                    "IP": data.get("ip"),
                    "Ville": data.get("city"),
                    "Région": data.get("region"),
                    "Pays": data.get("country"),
                    "Location": data.get("loc"),
                    "Organization": data.get("org"),
                    "Code Postal": data.get("postal")
                }
            else:
                return {"Erreur": "Impossible de récupérer les informations"}
        except requests.RequestException as e:
            return {"Erreur": str(e)}

    ip = input("Entrez l'adresse IP à localiser: ")
    result = get_ip_info(ip)
    for key, value in result.items():
        print(f"{key}: {value}")

elif choix_utilisateur == '2':
    print("Je ne suis pas là pour faire le pirate du web ou même l'acteur, je voulais juste partager le tool le plus simple possible... (peut-être d'autres projets plus complexes et complets à l'avenir)")
else:
    print("Choix non valide, veuillez sélectionner '1' ou '2'.")
