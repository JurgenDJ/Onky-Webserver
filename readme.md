# Onkyo control api server
Simple webservice, as a wrapper for controlling my Onkyo receiver.
Basically I'm running small scripts on top of the eiscp library that I found on github (but which is no longer maintained / completed)
these scripts can be triggered through a fastapi based web interface.

The service can be queried (swagger style) using http://localhost:8000/docs

## install 
1) create and activate the virtual environment:
```bash
py -m venv venv
./venv/scripts/activate
```
2) install the packages
```bash
pip install -r requirements.txt
```
## Run server
The easiest way is to use the vsCode Task explorer -> vscode -> **Run Fastapi webserver**
of manueel met het commando:
```bash
py -m venv venv
uvicorn server:app --reload
```
de reload parameter zorgt dat de server herstart wanneer server.py wordt aangepast.