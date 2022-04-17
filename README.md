# Example for the autoscaling web app

## Simple flask web app as a base to demostrate horisontal scaling
## horisontal scaling abilities

* Requirements:
    python3 (tested with Python 3.8, 3.9)

* Local tests:
```bash
cd ./factorial
pip3 install -r factorial/requirements.txt
./local_dev.sh
```

* Docker test:
```bash
docker build -t factorial:latest .
docker run -p 8000:8000 factorial
```
