# django2-pythonclub

Tutorial de Django 2.x para o pythonclub.com.br

Como contribuir?
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
```
git clone https://github.com/rg3915/django2-pythonclub.git
cd django2-pythonclub
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```