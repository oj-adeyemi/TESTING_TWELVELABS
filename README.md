## Playing around with Twelve Labs API and SDK

### First create a virtual envrionment

```bash
python3 -m venv .venv
or
python -m venv .venv

```
### Activate the virtual environment

```bash
source .venv/bin/activate #on Mac book
source .venv\Scripts\activate #on WIndows
```

### Create a .env file with the following values
``` bash
 API_KEY="TWELVE_LABS_API_KEY"
 API_URL="TWELVE_LABS_API_URL" #only needed for rest api
```

### Install dependencies from requirements.txt file

```bash
pip install -r requirements.txt
```

---
### [TWELVE LABS REST API DOCS](https://docs.twelvelabs.io/reference/api-reference)

### [TWELVE LABS PYTHON SDK REPO](https://github.com/twelvelabs-io/twelvelabs-python/tree/main)