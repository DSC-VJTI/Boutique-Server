# Boutique Server

## Quick Setup

1. Clone the repo

```bash
$ git clone https://github.com/DSC-VJTI/Boutique-Server
```

2. Create a `virtual environment` and install the requirements

```bash
$ pip install -r requirements.txt
```

3. You need to set the following environment variables

```
  DATABASE_URL                  // Database URL
```

4. Run the project

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
