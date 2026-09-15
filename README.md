import requests
from bs4 import BeautifulSoup
import hashlib
import hmac

class NeuraX:
    def __init__(self, owner_name, master_key):
        self.name = "NEURA-X"
        self.owner_name = owner_name
        self._master_key_hash = hashlib.sha256(master_key.encode('utf-8')).hexdigest()
        self.knowledge_base = []

    def _verify_owner(self, provided_key):
        """Validação de segurança biométrica/criptográfica do proprietário."""
        input_hash = hashlib.sha256(provided_key.encode('utf-8')).hexdigest()
        return hmac.compare_digest(input_hash, self._master_key_hash)

    def learn_from_web(self, user_key, search_query):
        """Navega na web global para expandir o conhecimento autonomamente."""
        if not self._verify_owner(user_key):
            return f"[{self.name}]: ACESSO NEGADO. Apenas o proprietário autorizado pode iniciar o aprendizado."

        # Busca autônoma de dados
        url = f"https://html.duckduckgo.com/html/?q={search_query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        try:
            res = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, 'html.parser')
            snippets = [a.get_text() for a in soup.find_all('a', class_='result__snippet')]
            
            # Adiciona novos aprendizados à memória
            self.knowledge_base.extend(snippets)
            return f"[{self.name}]: Varredura concluída. {len(snippets)} novos blocos de dados absorvidos."
        except Exception as e:
            return f"[{self.name}]: Falha na conexão web: {e}"

    def query_system(self, user_key, question):
        """Responde exclusivamente se a chave mestra for validada."""
        if not self._verify_owner(user_key):
            return f"[{self.name}]: ACESSO NEGADO. Sistema bloqueado para usuários não autorizados."

        # Retorna o conhecimento acumulado
        context = "\n".join(self.knowledge_base[:3]) if self.knowledge_base else "Sem dados acumulados."
        return f"[{self.name} - Resposta Exclusiva para {self.owner_name}]:\nCom base no meu aprendizado web:\n{context}"

# --- Teste de Execução ---
# 1. Inicializa a NEURA-X vinculada a você
ia = NeuraX(owner_name="Criador", master_key="SuaChaveSecreta123")

# 2. Tentativa de uso por outra pessoa (bloqueado)
print(ia.query_system(user_key="chave_qualquer", question="Quem é você?"))

# 3. Você ordenando que ela aprenda na web
print(ia.learn_from_web(user_key="SuaChaveSecreta123", search_query="novas tecnologias de IA"))

# 4. Você consultando a NEURA-X
print(ia.query_system(user_key="SuaChaveSecreta123", question="O que você aprendeu?"))
