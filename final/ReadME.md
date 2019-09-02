1) create a directory : mkdir project_name

2) go to that directory : cd project_name

3) extract the tar folder here

4) create a virtual environment: virtualenv venv

5) activate virtual env: source venv/bin/activate
or (\env\Scripts\activate.bat)

6) cd project_folder

7) install the required packages:  pip install -r requirements.txt

8) run these commands:
			python manage.py makemigrations
			python manage.py migrate
			python manage.py runserver


Task 0) Loading data into database tables:
		code : populate_data.py
		run these commands:
       		cd evaluate
       		python manage.py shell
         		- from analysis.models import BusinessDetail

Task 1) To see the graph for current year wise active record
		goto this url:http://127.0.0.1:8000/analysis/current_year_view/


Task 2) To see the monthly view
		go to this url : http://127.0.0.1:8000/analysis/monthly_view/

Task 3) To see the category_study
		go to this url : http://127.0.0.1:8000/analysis/category_study/






