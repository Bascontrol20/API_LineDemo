#https://pypi.org/project/threaded/
import json
import requests
import pymcprotocol #for PLC

import threading

# Set frame type
slmp = pymcprotocol.Type3E()
# Set PLC type
slmp = pymcprotocol.Type3E(plctype="iQ-R")
# Connect PLC
slmp.connect("192.168.137.188", 3000)


def api_get():
    threading.Timer(10.0,api_get).start()
    print("Get API Data")

    get_url = "http://127.0.0.1:8000/api/?format=json"
    resp = requests.get(get_url)
    get_dat = resp.json()
    print(get_dat)
    #print(resp)
    '''Get PLC Tag'''
    
    #get_plc0 = get_dat[0]['plctag']
    #print(get_plc0)
    # get_plc1 = get_dat[1]['plctag']
    # print(get_plc1)

    # '''Get Line Message'''
    # get_msg0 = get_dat[0]['linemsg']
    # print(get_msg0)
    # get_msg1 = get_dat[1]['linemsg']
    # print(get_msg1)

    # '''Get Line Token'''
    # get_tkn0 = get_dat[0]['linetoken']
    # print(get_tkn0)
    # get_tkn1 = get_dat[1]['linetoken']
    # print(get_tkn1)
    
    # for i in range(0,2):
    #     get_plc = get_dat[i]['plctag']
    #     get_msg = get_dat[i]['linemsg']
    #     get_tkn = get_dat[i]['linetoken']
    #     print(get_plc)
    #     print(get_msg)
    #     print(get_tkn)
    #     i+=1


def schedule_api():
    threading.Timer(10.0,schedule_api).start()
    print("Line Notify Running...")
    get_url = "http://127.0.0.1:8000/api/?format=json"
    resp = requests.get(get_url)
    get_dat = resp.json()

    
    head_device = get_dat[0]['plctag']
    device_batch_read = slmp.batchread_bitunits(headdevice=head_device, readsize=50)

    


    '''MC01 M1000-M1009'''
    #MessageNo.1
    if device_batch_read[0] == 1:
        id= get_dat[0]['linetoken']
        msg1 = get_dat[0]['linemsg']
        line_notify(msg1,id)
    #MessageNo.2
    if device_batch_read[1] == 1:
        id= get_dat[1]['linetoken']
        msg1 = get_dat[1]['linemsg']
        line_notify(msg1,id)
    #MessageNo.3
    if device_batch_read[2] == 1:
        id= get_dat[2]['linetoken']
        msg1 = get_dat[2]['linemsg']
        line_notify(msg1,id)
    #MessageNo.4
    if device_batch_read[3] == 1:
        id= get_dat[3]['linetoken']
        msg1 = get_dat[3]['linemsg']
        line_notify(msg1,id)
    #MessageNo.5
    if device_batch_read[4] == 1:
        id= get_dat[4]['linetoken']
        msg1 = get_dat[4]['linemsg']
        line_notify(msg1,id)
    #MessageNo.6
    if device_batch_read[5] == 1:
        id= get_dat[5]['linetoken']
        msg1 = get_dat[5]['linemsg']
        line_notify(msg1,id)
    #MessageNo.7
    if device_batch_read[6] == 1:
        id= get_dat[6]['linetoken']
        msg1 = get_dat[6]['linemsg']
        line_notify(msg1,id)
    #MessageNo.8
    if device_batch_read[7] == 1:
        id= get_dat[7]['linetoken']
        msg1 = get_dat[7]['linemsg']
        line_notify(msg1,id)
    #MessageNo.9
    if device_batch_read[8] == 1:
        id= get_dat[8]['linetoken']
        msg1 = get_dat[8]['linemsg']
        line_notify(msg1,id)
    #MessageNo.10
    if device_batch_read[9] == 1:
        id= get_dat[9]['linetoken']
        msg1 = get_dat[9]['linemsg']
        line_notify(msg1,id)

    '''MC01 M1011-M1020'''
    #MessageNo.11
    if device_batch_read[10] == 1:
        id= get_dat[10]['linetoken']
        msg1 = get_dat[10]['linemsg']
        line_notify(msg1,id)
    #MessageNo.12
    if device_batch_read[11] == 1:
        id= get_dat[11]['linetoken']
        msg1 = get_dat[11]['linemsg']
        line_notify(msg1,id)
    #MessageNo.13
    if device_batch_read[12] == 1:
        id= get_dat[12]['linetoken']
        msg1 = get_dat[12]['linemsg']
        line_notify(msg1,id)
    #MessageNo.14
    if device_batch_read[13] == 1:
        id= get_dat[13]['linetoken']
        msg1 = get_dat[13]['linemsg']
        line_notify(msg1,id)
    #MessageNo.15
    if device_batch_read[14] == 1:
        id= get_dat[14]['linetoken']
        msg1 = get_dat[14]['linemsg']
        line_notify(msg1,id)
    #MessageNo.16
    if device_batch_read[15] == 1:
        id= get_dat[15]['linetoken']
        msg1 = get_dat[15]['linemsg']
        line_notify(msg1,id)
    #MessageNo.17
    if device_batch_read[16] == 1:
        id= get_dat[16]['linetoken']
        msg1 = get_dat[16]['linemsg']
        line_notify(msg1,id)
    #MessageNo.18
    if device_batch_read[17] == 1:
        id= get_dat[17]['linetoken']
        msg1 = get_dat[17]['linemsg']
        line_notify(msg1,id)
    #MessageNo.19
    if device_batch_read[18] == 1:
        id= get_dat[18]['linetoken']
        msg1 = get_dat[18]['linemsg']
        line_notify(msg1,id)
    #MessageNo.20
    if device_batch_read[19] == 1:
        id= get_dat[19]['linetoken']
        msg1 = get_dat[19]['linemsg']
        line_notify(msg1,id)

    '''MC01 M1021-M1030'''
    #MessageNo.21
    if device_batch_read[20] == 1:
        id= get_dat[20]['linetoken']
        msg1 = get_dat[20]['linemsg']
        line_notify(msg1,id)
    #MessageNo.22
    if device_batch_read[21] == 1:
        id= get_dat[21]['linetoken']
        msg1 = get_dat[21]['linemsg']
        line_notify(msg1,id)
    #MessageNo.23
    if device_batch_read[22] == 1:
        id= get_dat[22]['linetoken']
        msg1 = get_dat[22]['linemsg']
        line_notify(msg1,id)
    #MessageNo.24
    if device_batch_read[23] == 1:
        id= get_dat[23]['linetoken']
        msg1 = get_dat[23]['linemsg']
        line_notify(msg1,id)
    #MessageNo.25
    if device_batch_read[24] == 1:
        id= get_dat[24]['linetoken']
        msg1 = get_dat[24]['linemsg']
        line_notify(msg1,id)
    #MessageNo.26
    if device_batch_read[25] == 1:
        id= get_dat[25]['linetoken']
        msg1 = get_dat[25]['linemsg']
        line_notify(msg1,id)
    #MessageNo.27
    if device_batch_read[26] == 1:
        id= get_dat[26]['linetoken']
        msg1 = get_dat[26]['linemsg']
        line_notify(msg1,id)
    #MessageNo.28
    if device_batch_read[27] == 1:
        id= get_dat[27]['linetoken']
        msg1 = get_dat[27]['linemsg']
        line_notify(msg1,id)
    #MessageNo.29
    if device_batch_read[28] == 1:
        id= get_dat[28]['linetoken']
        msg1 = get_dat[28]['linemsg']
        line_notify(msg1,id)
    #MessageNo.30
    if device_batch_read[29] == 1:
        id= get_dat[29]['linetoken']
        msg1 = get_dat[29]['linemsg']
        line_notify(msg1,id)

    '''MC01 M1031-M1040'''
    #MessageNo.31
    if device_batch_read[30] == 1:
        id= get_dat[30]['linetoken']
        msg1 = get_dat[30]['linemsg']
        line_notify(msg1,id)
    #MessageNo.32
    if device_batch_read[31] == 1:
        id= get_dat[31]['linetoken']
        msg1 = get_dat[31]['linemsg']
        line_notify(msg1,id)
    #MessageNo.33
    if device_batch_read[32] == 1:
        id= get_dat[32]['linetoken']
        msg1 = get_dat[32]['linemsg']
        line_notify(msg1,id)
    #MessageNo.34
    if device_batch_read[33] == 1:
        id= get_dat[33]['linetoken']
        msg1 = get_dat[33]['linemsg']
        line_notify(msg1,id)
    #MessageNo.35
    if device_batch_read[34] == 1:
        id= get_dat[34]['linetoken']
        msg1 = get_dat[34]['linemsg']
        line_notify(msg1,id)
    #MessageNo.36
    if device_batch_read[35] == 1:
        id= get_dat[35]['linetoken']
        msg1 = get_dat[35]['linemsg']
        line_notify(msg1,id)
    #MessageNo.37
    if device_batch_read[36] == 1:
        id= get_dat[36]['linetoken']
        msg1 = get_dat[36]['linemsg']
        line_notify(msg1,id)
    #MessageNo.38
    if device_batch_read[37] == 1:
        id= get_dat[37]['linetoken']
        msg1 = get_dat[37]['linemsg']
        line_notify(msg1,id)
    #MessageNo.39
    if device_batch_read[38] == 1:
        id= get_dat[38]['linetoken']
        msg1 = get_dat[38]['linemsg']
        line_notify(msg1,id)
    #MessageNo.40
    if device_batch_read[39] == 1:
        id= get_dat[39]['linetoken']
        msg1 = get_dat[39]['linemsg']
        line_notify(msg1,id)

    '''MC01 M1041-M1050'''
    #MessageNo.41
    if device_batch_read[40] == 1:
        id= get_dat[40]['linetoken']
        msg1 = get_dat[40]['linemsg']
        line_notify(msg1,id)
    #MessageNo.42
    if device_batch_read[41] == 1:
        id= get_dat[41]['linetoken']
        msg1 = get_dat[41]['linemsg']
        line_notify(msg1,id)
    #MessageNo.43
    if device_batch_read[42] == 1:
        id= get_dat[42]['linetoken']
        msg1 = get_dat[42]['linemsg']
        line_notify(msg1,id)
    #MessageNo.44
    if device_batch_read[43] == 1:
        id= get_dat[43]['linetoken']
        msg1 = get_dat[43]['linemsg']
        line_notify(msg1,id)
    #MessageNo.45
    if device_batch_read[44] == 1:
        id= get_dat[44]['linetoken']
        msg1 = get_dat[44]['linemsg']
        line_notify(msg1,id)
    #MessageNo.46
    if device_batch_read[45] == 1:
        id= get_dat[45]['linetoken']
        msg1 = get_dat[45]['linemsg']
        line_notify(msg1,id)
    #MessageNo.47
    if device_batch_read[46] == 1:
        id= get_dat[46]['linetoken']
        msg1 = get_dat[46]['linemsg']
        line_notify(msg1,id)
    #MessageNo.48
    if device_batch_read[47] == 1:
        id= get_dat[47]['linetoken']
        msg1 = get_dat[47]['linemsg']
        line_notify(msg1,id)
    #MessageNo.49
    if device_batch_read[48] == 1:
        id= get_dat[48]['linetoken']
        msg1 = get_dat[48]['linemsg']
        line_notify(msg1,id)
    #MessageNo.50
    if device_batch_read[49] == 1:
        id= get_dat[49]['linetoken']
        msg1 = get_dat[49]['linemsg']
        line_notify(msg1,id)


def line_notify(message,id):

    # tokendb = Linemessage.objects.get(id=id).linetoken
    tokendb = id
    #print(tokendb)
    url = 'https://notify-api.line.me/api/notify'
    token1 = tokendb
    headers1 = {'content-type':'application/x-www-form-urlencoded',
                'Authorization':'Bearer '+token1}
    msg1 = message
    r = requests.post(url, headers=headers1 , data = {'message':msg1}) 
    print(r.text)
    

if __name__ == '__main__':
    schedule_api()
    #api_get()