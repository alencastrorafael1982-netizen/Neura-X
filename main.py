import os
import time
import hashlib
import hmac
import requests
from bs4 import BeautifulSoup

class NeuraXEngine:
    def __init__(self, owner_name, master_key):
        self.name = "NEURA-X"
        self.owner_name = owner_name
        self._master_key_hash = hashlib.sha256(master_key.encode('utf-8')).hexdigest()
        self.memory_db = []

    def _verify_owner(self, provided_key):
        input_hash = hashlib.sha256(provided_key.encode('utf-8')).hexdigest()
        return hmac.compare_digest(input_hash, self._master_key_hash)

    def autonomous_web_scan(self, user_key, query):
        if not self._verify_owner(user_key):
            return f"[{self.name}]: ACESSO NEGADO."

        url = f"https://html.duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            snippets = [a.get_text() for a in soup.find_all('a', class_='result__snippet')]
            self.memory_db.extend(snippets)
            return f"[{self.name}]: {len(snippets)} novos dados absorvidos."
        except Exception as e:
            return f"[{self.name}]: Erro na conexão: {e}"

if __name__ == "__main__":
    OWNER = os.getenv("NEURA_OWNER", "Criador")
    MASTER_KEY = os.getenv("NEURA_MASTER_KEY", "ChavePadraoTrocar123")

    agent = NeuraXEngine(owner_name=OWNER, master_key=MASTER_KEY)
    print(f"[{agent.name}]: Ativo e operante.")

    topics = ["inteligencia artificial avançada", "tecnologias espaciais xAI"]
    for topic in topics:
        print(agent.autonomous_web_scan(MASTER_KEY, topic))
        time.sleep(5)
