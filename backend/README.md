# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

### Auth0 Setup

this app uses auth0 for authntication with RBAC as follows:

- Public:
  - `get:drinks`
- Barista:
  - `get:drinks-detail`
- Manger:
  - `get:drinks-detail`
  - `post:drinks`
  - `patch:drinks`
  - `delete:drinks`

#### Testing

to test the api endpoints with [Postman](https://www.postman.com/):


1. Setup 2 jwt tokens for `barista` and `manger` with the permissions for each one as stated above.

    sample jwt token for `Manger`:
     ```bash
     {
     "aud": "coffee-shop-api",
     "iat": 1604235877,
     "exp": 1604243077,
     "scope": "",
     "permissions": [
         "delete:drinks",
         "get:drinks-detail",
         "patch:drinks",
         "post:drinks"
        ]
     }
     ```

2. Import the collection `./backend/udacity-fsnd-udaspicelatte.postman_collection.json` into postman.
3. in postman right-click the collection folder for barista and manager, navigate to the authorization tab, and include the JWT in the token field.
4. run the different requests to test the api endpoints.
