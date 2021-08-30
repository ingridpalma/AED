# Design and Evaluation of IoT Gateway for DataPrioritization based on Van Emde Boas Tree

The server is at: http://aedheaps.pythonanywhere.com/admin/

When running the server for the first time:

1. Create env for the project:
     python3 -m venv env
     On macOS and Linux:
     source env/bin/activate
     On Windows:
     .\env\Scripts\activate
   
2. Install django and django REST framework
  pip install ...
  
3. Create the device database
   in the project root (AED\heaps)
   python manage.py makemigrations heaps_server
   python manage.py migrate
  
4. Put on the air
  python manage.py runserver

