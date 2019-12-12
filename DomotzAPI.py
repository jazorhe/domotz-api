import json
import requests

from site_notes import magri
from site_notes import bobby3Avalon
from site_notes import bambra
from site_notes import APICredentials

# curl -X GET https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent
# -H 'Accept: application/json' -H 'X-Api-Key: RfSnVPIyF8zEegeh4Ph3HUr8FyRX6aEDvkJD6Txw1yA' | json_pp

#  No modem found on Magri's

def printJSON(r):
    json_response = r.json()
    if r.status_code != 200:
        print('API Error:', r.status_code)
        print(json.dumps(json_response, indent=4),'\n')

    else:
        print('Response status_code: ', r.status_code, '\n')
        print(json.dumps(json_response, indent=4),'\n')



def listAgents( params = {} ):
    return requests.get('https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent',
        params=params, headers = APICredentials.getheaders)


def listDevices( agentID, params = {} ):
    return requests.get('https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent/' + agentID + '/device',
        params=params, headers = APICredentials.getheaders)

def getDevicePowerActions( agentID, device, params = {} ):
    print('Getting Power Actions on device', device['DeviceName'])
    return requests.get('https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent/' + agentID + '/device/' + device['DeviceID'] + '/action/power',
        params=params, headers = APICredentials.getheaders)

def powerActionOnDevice( agentID, device, field, params = {} ):
    print('Attempting', field, 'on device', device['DeviceName'])
    return requests.post('https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent/' + agentID + '/device/' + device['DeviceID'] + '/action/power/' + field,
        params=params, headers = APICredentials.postheaders)

def connectToDevice( agentID, device ):
    print("Connecting to device: ", device)
    return requests.post('https://api-eu-west-1-cell-1.domotz.com/public-api/v1/agent/' + agentID + '/device/' + device['DeviceID'] + '/connection',
        headers = APICredentials.postheaders)


if __name__ == "__main__":

    # r = listAgents()
    # r = listDevices(magri.AgentID)

    # r = getDevicePowerActions(magri.AgentID, magri.quickTest)
    # r = powerActionOnDevice(magri.AgentID, magri.quickTest, 'software_reboot')
    # r = connectToDevice(magri.AgentID, magri.usgGateway)

    # printJSON(r)

    devicelist = listDevices(magri.AgentID)
    for item in devicelist.json():
        body = { 'DeviceName': item['display_name'], 'DeviceID': str(item['id']) }
        r = getDevicePowerActions(magri.AgentID, body)
        if r.json()['software_reboot']:
            print('ip_address: ', item['ip_addresses'], 'id: ', item['id'])
            printJSON(r)
