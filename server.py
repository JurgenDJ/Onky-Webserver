from fastapi import FastAPI
import eiscp
import time

app = FastAPI()


def getPowerState(receiver):
    result = receiver.raw('PWRQSTN') 
    print(result)
    return result == 'PWR01'

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/radio/mnm")
def set_mnm():
    with eiscp.eISCP('192.168.1.32') as receiver:
        _, powerstatus = receiver.command('main power query')
        if powerstatus != 'on':
            receiver.command('main power on')
            time.sleep(2)
        result = receiver.raw('SLI2B')  # source NET
        result = receiver.raw('NSV0e0')
        result = receiver.raw('NLSI00001')  # select eerste element in de lijst => my Presets
        result = receiver.raw('NLSI00001')  # select tweede element in de lijst => MNM
    return {}


@app.post("/radio/radio1")
def set_radio1():
    with eiscp.eISCP('192.168.1.32') as receiver:
        _, powerstatus = receiver.command('main power query')
        if powerstatus != 'on':
            receiver.command('main power on')
            time.sleep(2)
        result = receiver.raw('SLI2B')  # source NET
        result = receiver.raw('NSV0e0')
        result = receiver.raw('NLSI00001')  # select eerste element in de lijst => my Presets
        result = receiver.raw('NLSI00002')  # select tweede element in de lijst => Radio 1
    return {}


@app.post("/volume/up")
def set_volumeUp():
    with eiscp.eISCP('192.168.1.32') as receiver:
        result = receiver.command('volume level-up')
        return result


@app.post("/volume/down")
def set_volumeDown():
    with eiscp.eISCP('192.168.1.32') as receiver:
        result = receiver.command('volume level-down')
        return result

@app.post("/power/off")
def powerOff():
    with eiscp.eISCP('192.168.1.32') as receiver:
        result = receiver.command('main power off')
        return result

@app.post("/power/on")
def powerOn():
    with eiscp.eISCP('192.168.1.32') as receiver:
        result = receiver.command('main power on')
        return result
