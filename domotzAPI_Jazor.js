var baseURL = 'https://api-eu-west-1-cell-1.domotz.com/public-api/v1/';
var API_Key = 'RfSnVPIyF8zEegeh4Ph3HUr8FyRX6aEDvkJD6Txw1yA';

var getHeader  = { 'Accept': 'application/json', 'X-Api-Key': API_Key };
var putHeader  = { 'Content-Type':'application/json', 'X-Api-Key': API_Key };
var postHeader = { 'X-Api-Key': API_Key };
var headHeader = { 'X-Api-Key': API_Key };


var domotzAPI_Jazor = {

    listAgent: function() {
        $.ajax({
            url: baseURL + 'agent',
            method: 'get',

            headers: getHeader,
            success: function(data) {
                console.log(JSON.stringify(data,null,2));
                }
        })
    },

    listDevices: function( agentID ) {
      $.ajax({
        url: baseURL + 'agent/' + agentID + '/device',
        method: 'get',

        headers: getHeader,
        success: function(data) {
          console.log(JSON.stringify(data,null,2));
        }
      })
    },

    getDevicePowerActions: function( agentID, deviceID ) {
      $.ajax({
        url: baseURL + 'agent/' + agentID + '/device/' + deviceID + '/action/power',
        method: 'get',

        headers: getHeader,
        success: function(data) {
          console.log(JSON.stringify(data,null,2));
        }
      })
    },

    powerActionOnDevice: function( agentID, deviceID, field ) {
      $.ajax({
        url: baseURL + 'agent/' + agentID + '/device/' + deviceID + '/action/power/' + field,
        method: 'post',

        headers: postHeader,
        success: function(data) {
          console.log(JSON.stringify(data,null,2));
        }
      })
    }

};


// domotzAPI_Jazor.listAgent();
// domotzAPI_Jazor.listDevices('250758');
domotzAPI_Jazor.getDevicePowerActions('250758', '3485967');
// domotzAPI_Jazor.powerActionOnDevice('250758', '3482271', 'software_reboot');
