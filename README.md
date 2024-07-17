# Bootcamp_July_MAD2

### Technologies Used : 

- VueJS - Used for User Interface 

- Flask RestFul API - Used to develop the RESTful API for the app

- Jinja2 - Used for rendering templates for sending emails

- Bootstrap - Used for HTML and CSS styling

- SQLite - Used for data storage

- Flask SQLAlchemy - Used as an ORM (Object-Relational Mapping) tool to interact with the database

- Flask Celery - Used for asynchronous background jobs at the backend.

- Flask Caching - Used for caching API outputs and increasing performance.

- Redis - Used as an in-memory database for the API cache and as a message broker for celery.


## Getting Started

### Prerequisites

- Python 3.x
- pip


### Installation

1. Clone the repo.

```
git clone https://github.com/ShubhamYadav9416/Bootcamp_July_MAD2.git
```

2. Navigate to the root folder of the application.

3. Open two separate terminals and execute the following commands in each:

- To install Redis and run(after running each line close the terminal and run next line new terminal.)
  
```
Install flatpak: pip insatll flatpak
add flatpak repo: sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
Install RedisInsight using flatpak: flatpak install flathub com.redis.RedisInsight
REDIS SERVER : flatpak run com.redis.RedisInsight
```

-To install and run Mailhog

```
Install go: sudo apt-get -y install golang-go
install MailHog Using go: go install github.com/mailhog/MailHog@latest
MAILHOG : ~/go/bin/MailHog
```

4. Navigate to the backend folder and open three separate terminals. Execute the following commands in each:
   
- To run flask app(run virtual environment and pip install all dependencies)
  
```
BACKEND : python main.py
```

-To run celery

```
WORKERS : celery -A main:cel_app worker -l info
```

-To run celery beat

```
BEATS : celery -A main:cel_app beat --max-interval 1 -l info
```

5. Navigate to the frontend folder.

In the terminal, execute the following command:

```
npm run serve
```


### Contributing

Contributions are always welcome !!

If you would like to contribute to the project, please fork the repository and make a pull request.



### Support my work 
Do ⭐ the repository, if it inspired you, gave you ideas for your own portfolio or helped you in any way.


