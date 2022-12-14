# SDG-Reporter
The SDG Reporter app will generate report only for years but will generate report for 1 year 

## Launch Development Server

👋 Hey welcome to this readme, First the server needs to have Python 3 and Postgres 12.9 + installed. \
create a postgres database using the following instruction. 
> 'DatabaseNAME': 'sdr', \
> 'USER': 'sdruser', \
> 'PASSWORD': 'password', 

Open terminal \

- cloning the app
- create postgres database 
CREATE DATABASE sdr; \
CREATE USER sdruser WITH PASSWORD 'password'; \
ALTER ROLE sdruser SET client_encoding TO 'utf8'; \
ALTER ROLE sdruser SET default_transaction_isolation TO 'read committed'; \
ALTER ROLE sdruser SET timezone TO 'UTC'; \
GRANT ALL PRIVILEGES ON DATABASE sdr TO sdruser; \
psql -U sdruser -h localhost sdr \
(☝🏾 postgres connect to database as user)
\q
exit

- python manage.py makemigrations authentication main
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
- create country
- stop the server
- python manage.py shell < ../necessary_data.py
- python manage.py runserver
- upload all indicators as fixture
- register the country
- the dashboard will show all 17 SDG's
- click SDG-1 and it will give description and indicators plus add or update indicator

Add Indicator (value, year, description, Long-Term Objective, Reference, Source)
- click one indicator then see the data with chart
- To generate report as pdf use Ctr + p

🔐 So, these are the key features
- SDG Yearly Data Management for a country
- SDG Report Generation
- Data Visualization

🚀 You're now up and running. 
## Access Control
1. Go to localhost/admin and assign access for admin 
2. go back to localhost:8000/ 

👍🏾 Good Job.
## What you see?
![image](https://user-images.githubusercontent.com/51055556/190931783-5fc71975-004e-42e5-aff1-8a5ea5d35fe5.png)
![image](https://user-images.githubusercontent.com/51055556/193348147-6c14cfd2-5f54-4bf7-8b88-fdddb4509ba1.png)
![image](https://user-images.githubusercontent.com/51055556/190931697-69919b71-3015-4cb9-8ca9-3d1036def628.png)
![image](https://user-images.githubusercontent.com/51055556/193417632-36ccc2e7-0359-47db-a9fd-3955b09209fa.png)
![image](https://user-images.githubusercontent.com/51055556/190931717-ce8d5dca-4b67-4b2b-bc71-ab83948e8c04.png)
![image](https://user-images.githubusercontent.com/51055556/190931751-845858d6-0eaa-4d0e-9fb4-7adc4b48934f.png)
![image](https://user-images.githubusercontent.com/51055556/193347781-998108e8-1842-4bef-8593-7b8b863d3d7e.png)
![image](https://user-images.githubusercontent.com/51055556/193347873-8861ffb2-06fa-487b-bace-846c26d881da.png)


#### Used Technologies
<p align="left"> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> | <a href="https://www.djangoproject.com/" target="_blank"> <img src="https://seeklogo.com/images/D/django-logo-4C5ECF7036-seeklogo.com.png" alt="django" width="40" height="40"/> </a>  | <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> | <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>  </p>
