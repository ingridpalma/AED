# AED
Projeto Heap - Grupo 4

O server está em: http://aedheaps.pythonanywhere.com/admin/

Ao rodar a primeira vez o servidor:
  1. Criar env para o projeto:
    python3 -m venv env
    On macOS and Linux:
    source env/bin/activate
    On Windows:
    .\env\Scripts\activate
   
  2. Instalar django e djangorestframework
  pip install ...
  
  3. Criar o banco de dados dos dispositivos
  na raiz do projeto (AED\heaps)
  python manage.py makemigrations heaps_server
  python manage.py migrate
  
  4. Colocar no ar
  python manage.py runserver

