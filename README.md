<h1 align="center">Welcome to Todo_with_FastAPI 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://documenter.getpostman.com/view/22926184/2s93RUtBH8" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://twitter.com/mihirh21" target="_blank">
    <img alt="Twitter: mihirh21" src="https://img.shields.io/twitter/follow/mihirh21.svg?style=social" />
  </a>
</p>

`Todoist` is a full stack todo application built with FARM stack. FastAPI and MongoDB on the backend and ReactJS on the frontend.

### 🏠 [Homepage](https://github.com/mihirh19/todo_web_app/)

### How to run Locally?

## Backend

To run the backend, you need to have local mongodb instance running on you can setup a deployed instance using [MongoDB Atlas](https://www.mongodb.com/atlas/database).

### Setting up python environment

Run the following to create a virtual environment for the project. (Assuming you have python installed on local machine)

```bash
python -m virtualenv env
# OR
python -m venv env
#OR
python -m venv --system-site-packages env
#OR
python3 -m venv env
# if still doesn't work, google is your best friend!
```

If you're running the deployed instance, make sure to change the database connection string in `.env` file on the backend.

### Setting up `.env` file

To setup `.env` file on the backend, create a file named `.env` in `/backend/app`.
Add the following in the `.env` file.

```txt
JWT_SECRET_KEY=<RAMDOM_STRING>
JWT_REFRESH_SECRET_KEY=<RANDOM_SECTURE_LONG_STRING>
MONGO_CONNECTION_STRING=<MONGO_DB_CONNECTION_STRING>
# mongodb://localhost:27017/ <-- for local running instances
```

### Installing dependencies

Assuming you are in the base directory.

```bash
cd backend
pip install -r requirements.txt
```

### Activating virtual environment

```bash
# Windows
env/Scripts/activate
# MacOs + Linux
source env/bin/activate
```

### Running the backend

Assuming you are in the backend directory.

```bash
python main.py
```

<hr>

## Author

👤 **Mihir Hadavani**

* Twitter: [@mihirh21](https://twitter.com/mihirh21)
* Github: [@mihirh19](https://github.com/mihirh19)
* LinkedIn: [@mihir-hadavani-996263232](https://linkedin.com/in/mihir-hadavani-996263232)

## Show your support

Give a ⭐️ if this project helped you!
