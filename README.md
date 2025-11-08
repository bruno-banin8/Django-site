# 🌐 Meu Site em Django

Este projeto é um **site desenvolvido com Django**, utilizando **Python**, **HTML** e **CSS**.  
O objetivo foi praticar desenvolvimento web com o framework Django, explorando rotas, templates, e conexão com o banco de dados.

---

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Django**
- **HTML5**
- **CSS3**
- (Opcional) **SQLite** — banco de dados padrão do Django

---

## ⚙️ Funcionalidades

- Páginas renderizadas com **templates HTML**
- Estilos personalizados com **CSS**
- Rotas configuradas no `urls.py`
- Views em Python para controlar a lógica
- (Se aplicável) Formulários e integração com banco de dados

---

## 🧩 Estrutura básica do projeto

meu_site/
│
├── manage.py
├── meu_site/ # Configurações do projeto
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── app_principal/ # Aplicativo principal
│ ├── templates/ # Arquivos HTML
│ ├── static/ # Arquivos CSS e imagens
│ ├── views.py
│ ├── urls.py
│ └── models.py
│
└── db.sqlite3 # Banco de dados (gerado automaticamente)

---

## 🖥️ Como executar o projeto

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
2. **Entre na pasta do projeto:**
   ```bash
   cd nome-do-repositorio
3. **Crie um ambiente virtual (opcional, mas recomendo):**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # No Windows
   source venv/bin/activate  # No Linux/macOS
4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
5. **Rode as migrações e inicie o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
6. **Acesse o navegado:**
   http://127.0.0.1:8000/

---

## 👨‍💻 Autor
**Bruno Banin**  
📫 [LinkedIn](https://www.linkedin.com/in/bruno-banin)  
💻 [GitHub](https://github.com/bruno-banin8)

---

## 📝 Licença
Este projeto está sob a licença MIT - sinta-se à vontade para usar e modificar 

   


