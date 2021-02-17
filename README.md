# Boutique Server

## Quick Setup

1. Clone the repo

```bash
$ git clone https://github.com/DSC-VJTI/Boutique-Server
```

2. Create a `virtual environment` and install the requirements

```bash
$ pip install -r requirements_dev.txt
```

3. Install `pre-commit` hooks

```bash
$ pre-commit install
```

4. You need to set the following environment variables

```
  SECRET_KEY                    // JWT secret
  ALGORITHM                     // Algorithm for encoding JWT
  ACCESS_TOKEN_EXPIRE_MINUTES   // JWT token expiration in minutes
  DATABASE_URL                  // Database URL
```

5. Run the project

  - Using `main.py`

  ```bash
  // using main.py

  $ cd src/app

  $ python main.py

  ```

  - Using `uvicorn` command

  ```bash
  $ uvicorn --app-dir="./src/app" --reload main:app
  ```
