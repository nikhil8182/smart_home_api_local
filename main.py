import time
from fastapi import FastAPI, Request
from models import *
from mongo import *

app = FastAPI(title="Onwords Local Smart Home Server", docs_url="/admin", redoc_url="/document")


@app.get("/device", tags=["Devices"])
async def All_Device():
    try:
        device_list = []
        documents = device_collections.find()
        for document in documents:
            device_list.append(document)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/device/details", tags=["Devices"])
async def All_Device_Details():
    # device_details_collections.delete_many("_id")
    try:
        device_list = []
        documents = device_detail_collections.find()
        for document in documents:
            device_list.append(document)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/device/log", tags=["Devices"])
async def All_Device_Log():
    try:
        device_list = []
        documents = device_details_log_collections.find()
        for x in documents:
            device_list.append(x)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/device/boardlog", tags=["Devices"])
async def All_Device_Boardlog():
    try:
        device_list = []
        documents = device_board_log_collections.find()
        for x in documents:
            device_list.append(x)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/device/{item_id}", tags=["Devices"])
async def Get_Device_Data_By_ID(item_id: int):
    try:
        return device_collections.find_one({"_id": item_id})
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/device/details/{item_id}", tags=["Devices"])
async def Get_Device_Data_with_ID(item_id: int):
    try:
        return device_detail_collections.find_one({"_id": item_id})
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"

@app.put("/device/details/{item_id}", tags=["Devices"])
def Update_device_details(device: Devices_details_Put, item_id: int):
    device_detail_collections.update_one(
        {"_id": item_id},
        {
            "$set":{
                "name": device.name,
                "room": device.room,
                "device_id": device.device_id,
                "type": device.type
            }
        })

    return {"msg": f"updated device id {item_id} to {device}"}

@app.delete("/device/details/{item_id}", tags=["Devices"])
async def Delete_Devices_Details_by_id(item_id: int):
    device_detail_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.delete("/device/{item_id}", tags=["Devices"])
async def Delete_Devices_by_id(item_id: int):
    device_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


# update device data using put
@app.put("/device/{item_id}", tags=["Devices"])
def Update_device_status(device: Devices_put, item_id: int):
    device_collections.update_one({"_id": item_id}, {"$set": {"status": device.status}})

    return {"msg": f"updated device id {item_id} to {device.status}"}


@app.post("/device", tags=["Devices"])
async def create_New_devices(devices: Devices, request: Request):
    try:
        device_collections.insert_one({"_id": devices.id, "status": devices.status})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = device_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/device/details", tags=["Devices"])
async def create_New_devices(devices: Devices_details, request: Request):
    try:
        device_detail_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = device_detail_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/device/log", tags=["Devices"])
async def create_New_devices_Log(devices: Log, request: Request):
    try:
        device_details_log_collections.insert_one(
            {"_id": time.time(), "device_id": devices.device_id, "status": devices.status,
             "timestamp": devices.timestamp, "updated_by": devices.updated_by})
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.post("/device/boardlog", tags=["Devices"])
async def create_New_devices_Log(devices: Log, request: Request):
    try:
        device_board_log_collections.insert_one(
            {"_id": time.time(), "device_id": devices.device_id, "status": devices.status,
             "timestamp": devices.timestamp, "updated_by": devices.updated_by})
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.get("/fan", tags=["Fan"])
async def All_Fan_Data():
    fan_list = []
    documents = fan_collections.find()
    for document in documents:
        fan_list.append(document)
    return fan_list


@app.get("/fan/{item_id}", tags=["Fan"])
async def Get_Fan_Data_with_ID(item_id: int):
    return fan_collections.find_one({"_id": item_id})


@app.delete("/fan/{item_id}", tags=["Fan"])
async def Delete_fan_by_id(item_id: int):
    fan_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/fan/{item_id}", tags=["Fan"])
def Update_fan_status(device: Fan_put, item_id: int):
    fan_collections.update_one({"_id": item_id}, {"$set": {"status": device.status, "speed": device.speed}})
    return {"msg": f"updated device id {item_id} to {device.status} and speed to{device.speed}"}


@app.post("/fan", description="Create a new item", tags=["Fan"])
async def create_New_fan(fan: Fan, request: Request):
    try:
        fan_collections.insert_one({"_id": fan.id, "status": fan.status, "speed": fan.speed})
        return {"msg": "created successfully", "created_data": fan, "client": request.client}
    except:
        documents = fan_collections.find()
        for document in documents:
            id = document["_id"]
            if id == fan.id:
                return {"msg": {f"id {fan.id} already exist in fan, try using other id"}}


@app.get("/fan/details", tags=["Fan"])
async def All_Fan_Details():
    try:
        device_list = []
        documents = fan_details_collections.find()
        for document in documents:
            device_list.append(document)
        return {"details": device_list}
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/fan/log", tags=["Fan"])
async def All_fan_Logs():
    device_list = []
    documents = fan_details_log_collections.find()
    for x in documents:
        device_list.append(x)

    return device_list


@app.post("/fan/details", tags=["Fan"])
async def create_New_Fan_Details(devices: Fan_details, request: Request):
    try:
        fan_details_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = fan_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/fan/log", tags=["Fan"])
async def create_New_Fan_Log(devices: Log, request: Request):
    try:
        fan_details_log_collections.insert_one(
            {
            "_id": time.time(),
            "device_id": devices.device_id,
            "status": devices.status,
            "timestamp": devices.timestamp,
            "updated_by": devices.updated_by
            }
        )
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}


@app.get("/fan/boardlog", tags=["Fans"])
async def All_Fan_Boardlog():
    try:
        device_list = []
        documents = fan_board_log_collections.find()
        for x in documents:
            device_list.append(x)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"

@app.post("/fan/boardlog", tags=["Fans"])
async def create_New_Fan_Board_Log(devices: Log, request: Request):
    try:
        fan_board_log_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": devices.device_id,
                "status": devices.status,
                "timestamp": devices.timestamp,
                "updated_by": devices.updated_by
            }
        )
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id {devices.device_id} already exist in devices log, try using other id"}}



@app.get("/led", tags=["LED"])
async def All_LED_Data():
    list = []
    documents = led_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/led/{item_id}", tags=["LED"])
async def Get_LED_Data_with_ID(item_id: int):
    return led_collections.find_one({"_id": item_id})


@app.delete("/led/{item_id}", tags=["LED"])
async def Delete_led_by_id(item_id: int):
    led_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/led/{item_id}", tags=["LED"])
def Update_led_status(led: Led_put, item_id: int):
    led_collections.update_one({"_id": item_id}, {"$set": {"status": led.status, "R": led.R, "G": led.G, "B": led.B}})
    return {"msg": f"updated to {led}"}


@app.post("/led", description="Create a new LED", tags=["LED"])
async def create_New_led(led: Led, request: Request):
    try:
        led_collections.insert_one({"_id": led.id, "status": led.status, "R": led.R, "G": led.G, "B": led.B})
        return {"msg": "created successfully", "created_data": led, "client": request.client}
    except:
        documents = led_collections.find()
        for document in documents:
            id = document["_id"]
            if id == led.id:
                return {"msg": {f"id {led.id} already exist in fan, try using other id"}}


@app.get("/led/details", tags=["LED"])
async def All_LED_Details():
    try:
        device_list = []
        documents = led_details_collections.find()
        for document in documents:
            device_list.append(document)
        return {"details": device_list}
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/led/log", tags=["LED"])
async def All_LED_Logs():
    device_list = []
    documents = led_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list


@app.post("/led/details", tags=["LED"])
async def create_New_LED_Details(devices: Led_details, request: Request):
    try:
        led_details_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = led_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/led/log", tags=["LED"])
async def create_New_LED_Log(devices: Log, request: Request):
    try:
        led_details_log_collections.insert_one(
            {"_id": time.time(), "device_id": devices.device_id, "status": devices.status,
             "timestamp": devices.timestamp, "updated_by": devices.updated_by})
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.get("/mechanics", tags=["Mechanics"])
async def All_mechanics_Data():
    list = []
    documents = mechanics_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/mechanics/{item_id}", tags=["Mechanics"])
async def Get_mechanics_Data_with_ID(item_id: int):
    return mechanics_collections.find_one({"_id": item_id})


@app.delete("/mechanics/{item_id}", tags=["Mechanics"])
async def Delete_mechanics_by_id(item_id: int):
    mechanics_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/mechanics/{item_id}", tags=["Mechanics"])
def Update_mechanics_status(mechanics: Mechanics_put, item_id: int):
    mechanics_collections.update_one({"_id": item_id}, {"$set": {"values": mechanics.values}})
    return {"msg": f"updated to {mechanics}"}


@app.post("/mechanics", description="Create a new Mechanics", tags=["Mechanics"])
async def create_mechanics_led(mechanics: Mechanics, request: Request):
    try:
        mechanics_collections.insert_one({"_id": mechanics.id, "values": mechanics.values})
        return {"msg": "created successfully", "created_data": mechanics, "client": request.client}
    except:
        documents = mechanics_collections.find()
        for document in documents:
            id = document["_id"]
            if id == mechanics.id:
                return {"msg": {f"id {mechanics.id} already exist in fan, try using other id"}}


@app.get("/mechanic/details", tags=["Mechanics"])
async def All_Mechanics_Details():
    try:
        device_list = []
        documents = mechanics_details_collections.find()
        for document in documents:
            device_list.append(document)
        return device_list
    except:
        return "invalid url, contact admin at admin@onwords.in or cs@onwords.in"


@app.get("/mechanic/log", tags=["Mechanics"])
async def All_mechanics_Logs():
    device_list = []
    documents = mechanics_details_log_collections.find()
    for x in documents:
        device_list.append(x)
    return device_list


@app.post("/mechanic/details", tags=["Mechanics"])
async def create_New_Fan_Details(devices: Mechanics_details, request: Request):
    try:
        mechanics_details_collections.insert_one(
            {"_id": devices.id, "name": devices.device_name, "room": devices.room, "device_id": devices.device_id,
             "type": devices.type})
        return {"msg": "created successfully", "created_data": devices, "client": request.client}
    except:
        documents = mechanics_details_collections.find()
        for document in documents:
            id = document["_id"]
            if id == devices.id:
                return {"msg": {f"id {devices.id} already exist in devices, try using other id"}}


@app.post("/mechanic/log", tags=["Mechanics"])
async def create_New_Fan_Log(devices: Log, request: Request):
    try:
        mechanics_details_log_collections.insert_one(
            {"_id": time.time(), "device_id": devices.device_id, "status": devices.status,
             "timestamp": devices.timestamp, "updated_by": devices.updated_by})
        return {"msg": "log created", "created_data": devices, "client": request.client}
    except:
        return {"msg": {f"id already exist in devices log, try using other id"}}


@app.get("/eb", tags=["EB"])
async def All_eb_Data():
    list = []
    documents = eb_sensor_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb/{item_id}", tags=["EB"])
async def Get_Eb_Data_with_ID(item_id: int):
    return eb_sensor_collections.find_one({"_id": item_id})


@app.delete("/eb/{item_id}", tags=["EB"])
async def Delete_Eb_by_id(item_id: int):
    eb_sensor_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/eb/{item_id}", tags=["EB"])
def Update_Eb(eb: Eb_put, item_id: int):
    eb_sensor_collections.update_one(
        {"_id": item_id}, {
            "$set": {
                "voltage": eb.voltage,
                "amp": eb.amp,
                "ups_voltage": eb.ups_voltage,
                "ups_amp": eb.ups_AMP,
                "status": eb.status,
                "ups_battery_percentages": eb.ups_battery_percentage
            }
        }
    )
    return {"msg": f"updated to {eb}"}


@app.post("/eb", description="Create a new Mechanics", tags=["EB"])
async def create_New_Eb(eb: Eb, request: Request):
    try:
        eb_sensor_collections.insert_one(
            {
                "_id": eb.id,
                "voltage": eb.voltage,
                "amp": eb.amp,
                "ups_voltage": eb.ups_voltage,
                "ups_amp": eb.ups_AMP,
                "status": eb.status,
                "ups_battery_percentages": eb.ups_battery_percentage
            }
        )
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_sensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/eb/status", tags=["EB"])
async def All_eb_Data():
    list = []
    documents = eb_status_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb/status/{item_id}", tags=["EB"])
async def Get_Eb_Data_with_ID(item_id: int):
    return eb_status_collections.find_one({"_id": item_id})


@app.post("/eb/status", description="Create a new Mechanics", tags=["EB"])
async def create_New_Eb(eb: EbStatus, request: Request):
    try:
        eb_status_collections.insert_one({"_id": eb.id, "status": eb.status, "time_stamp": eb.time_stamp})
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_status_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/ups/voltage", tags=["EB"])
async def All_eb_Data():
    list = []
    documents = eb_ups_voltage_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/ups/voltage/{item_id}", tags=["EB"])
async def Get_Eb_Data_with_ID(item_id: int):
    return eb_ups_voltage_collections.find_one({"_id": item_id})


@app.post("/ups/voltage", description="Create a new Mechanics", tags=["EB"])
async def create_New_Eb(eb: UpsVoltage, request: Request):
    try:
        eb_ups_voltage_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": eb.device_id,
                "voltage": eb.voltage,
                "time_stamp": eb.time_stamp
            }
        )
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_ups_voltage_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/ups/ampere", tags=["EB"])
async def All_eb_Data():
    list = []
    documents = eb_ups_ampere_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/ups/ampere/{item_id}", tags=["EB"])
async def Get_Eb_Data_with_ID(item_id: int):
    return eb_ups_ampere_collections.find_one({"_id": item_id})


@app.post("/ups/ampere", description="Create a new Mechanics", tags=["EB"])
async def create_New_Eb(eb: UpsAmpere, request: Request):
    try:
        eb_ups_ampere_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": eb.device_id,
                "ampere": eb.ampere,
                "time_stamp": eb.time_stamp
            }
        )
        return {"msg": "created successfully", "created_data": eb, "client": request.client}
    except:
        documents = eb_ups_ampere_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb.id:
                return {"msg": {f"id {eb.id} already exist in fan, try using other id"}}


@app.get("/eb3", tags=["EB 3 Phase"])
async def All_Eb3phase_Data():
    list = []
    documents = eb3phasae_sensor_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb3/{item_id}", tags=["EB 3 Phase"])
async def Get_Eb3phase_Data_with_ID(item_id: int):
    return eb3phasae_sensor_collections.find_one({"_id": item_id})


@app.delete("/eb3/{item_id}", tags=["EB 3 Phase"])
async def Delete_Eb3phase_by_id(item_id: int):
    eb3phasae_sensor_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.put("/eb3/{item_id}", tags=["EB 3 Phase"])
def Update_Eb3phase_status(eb3: Eb3_put, item_id: int):
    eb3phasae_sensor_collections.update_one(
        {"_id": item_id}, {
            "$set": {
                "R_voltage": eb3.R_voltage,
                "Y_voltage": eb3.Y_voltage,
                "B_voltage": eb3.B_voltage,
                "R_amp": eb3.R_amp,
                "Y_amp": eb3.Y_amp,
                "B_amp": eb3.B_amp,
                "ups_voltage": eb3.ups_voltage,
                "ups_AMP": eb3.ups_AMP,
                "ups_battery_percentage": eb3.ups_battery_percentage,
                "status": eb3.status

            }
        }
    )
    return {"msg": f"updated to {eb3}"}


@app.post("/eb3", description="Create a new Mechanics", tags=["EB 3 Phase"])
async def create_New_Eb3phase(eb3: Eb3, request: Request):
    try:
        eb3phasae_sensor_collections.insert_one(
            {
                "_id": eb3.id,
                "R_voltage": eb3.R_voltage,
                "Y_voltage": eb3.Y_voltage,
                "B_voltage": eb3.B_voltage,
                "R_amp": eb3.R_amp,
                "Y_amp": eb3.Y_amp,
                "B_amp": eb3.B_amp,
                "ups_voltage": eb3.ups_voltage,
                "ups_AMP": eb3.ups_AMP,
                "ups_battery_percentage": eb3.ups_battery_percentage,
                "status": eb3.status
            }
        )
        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_sensor_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb3.id:
                return {"msg": {f"id {eb3.id} already exist in fan, try using other id"}}


@app.get("/eb3/voltage/", tags=["EB 3 Phase"])
async def All_Eb3phase_Voltage_Data():
    list = []
    documents = eb3phasae_voltage_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb3/voltage/{item_id}", tags=["EB 3 Phase"])
async def Get_Eb3phase_Data_with_ID(item_id: int):
    return eb3phasae_voltage_collections.find_one({"device_id": item_id})


@app.post("/eb3/voltage", description="Create a new Mechanics", tags=["EB 3 Phase"])
async def create_New_Eb3phase(eb3: Eb3Voltage, request: Request):
    try:
        eb3phasae_voltage_collections.insert_one(
            {
                "_id": time.time(), 
                "device_id": eb3.device_id,
                "r_voltage": eb3.r_voltage,
                "y_voltage": eb3.y_voltage,
                "b_voltage": eb3.b_voltage,
                "time_stamp": eb3.time_stamp
            }
        )

        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_voltage_collections.find()
        for document in documents:
            id = document["device_id"]
            if id == eb3.device_id:
                return {"msg": {f"id {eb3.device_id} already exist in fan, try using other id"}}


@app.put("/eb3/voltage/{item_id}", tags=["EB 3 Phase"])
def Update_Eb3phase_Voltage_status(eb3: Eb3Voltage, item_id: int):
    eb3phasae_voltage_collections.update_one(
        {"device_id": item_id}, {
            "$set": {
                "r_voltage": eb3.r_voltage,
                "y_voltage": eb3.y_voltage,
                "b_voltage": eb3.b_voltage,
                "time_stamp": eb3.time_stamp
            }
        }
    )
    return {"msg": f"updated to {eb3}"}

@app.get("/eb3/ampere/", tags=["EB 3 Phase"])
async def All_Eb3phase_ampere_Data():
    list = []
    documents = eb3phasae_ampere_collections.find()
    for document in documents:
        list.append(document)
    return list


@app.get("/eb3/ampere/{item_id}", tags=["EB 3 Phase"])
async def Get_Eb3phase_Data_with_ID(item_id: int):
    return eb3phasae_ampere_collections.find_one({"device_id": item_id})


@app.post("/eb3/ampere", description="Create a new Mechanics", tags=["EB 3 Phase"])
async def create_New_Eb3phase(eb3: Eb3Ampere, request: Request):
    try:
        eb3phasae_ampere_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": eb3.device_id,
                "r_ampere": eb3.r_ampere,
                "y_ampere": eb3.y_ampere,
                "b_ampere": eb3.b_ampere,
                "time_stamp": eb3.time_stamp
            }
        )

        return {"msg": "created successfully", "created_data": eb3, "client": request.client}
    except:
        documents = eb3phasae_ampere_collections.find()
        for document in documents:
            id = document["_id"]
            if id == eb3.id:
                return {"msg": {f"id {eb3.id} already exist in fan, try using other id"}}

@app.put("/eb3/ampere/{item_id}", tags=["EB 3 Phase"])
def Update_Eb3phase_Ampere_status(eb3: Eb3Ampere, item_id: int):
    eb3phasae_ampere_collections.update_one(
        {"device_id": item_id}, {
            "$set": {
                "r_ampere": eb3.r_ampere,
                "y_ampere": eb3.y_ampere,
                "b_ampere": eb3.b_ampere,
                "time_stamp": eb3.time_stamp
            }
        }
    )
    return {"msg": f"updated to {eb3}"}


@app.get("/room", tags=["Rooms"])
async def All_Room_Data():
    room_list = []
    documents = room_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list

@app.post("/room", description="Create a new room", tags=["Rooms"])
async def create_New_room(room: Rooms, request: Request):
    try:
        room_collections.insert_one(
            {
                "_id": room.id,
                "name": room.name,
                "device_id": room.devices,
                "fan_id": room.fan,
                "led_id": room.led,
                "mechanics_id": room.mechanics
            }
        )
        return {"msg": "created successfully", "created_data": room, "client": request.client}
    except:
        documents = device_collections.find()
        for document in documents:
            id = document["_id"]
            if id == room.id:
                return {"msg": {f"id {room.id} already exist in rooms, try using other id"}}

@app.get("/room/{item_id}", tags=["Rooms"])
async def Get_room_Data_with_ID(item_id: int):
    return room_collections.find_one({"_id": item_id})

@app.put("/room/{item_id}", tags=["Rooms"])
async def Put_room_Data_with_ID(rooms: Rooms, item_id: int):
    eb3phasae_ampere_collections.update_one(
        {"_id": item_id}, {
            "$set": {
                "name": rooms.name,
                "device_id": rooms.devices,
                "fan_id": rooms.fan,
                "led_id": rooms.led,
                "mechanics_id": rooms.mechanics
            }
        }
    )
    return {"msg": f"updated to {rooms}"}

@app.delete("/room/{item_id}", tags=["Rooms"])
async def Delete_room_by_id(item_id: int):
    room_collections.delete_one({"_id": item_id})
    return {"msg": f"Successfully deleted item in {item_id}"}


@app.get("/temp", tags=["Temperature"])
async def All_Room_Data():
    room_list = []
    documents = temp_collections.find()
    for document in documents:
        room_list.append(document)
    return room_list


@app.post("/temp", description="Create a new item", tags=["Temperature"])
async def create_New_fan(temp: Temperature, request: Request):
    try:
        temp_collections.insert_one(
            {
                "_id": time.time(),
                "device_id": temp.device_id,
                "room": temp.room,
                "temperature": temp.temperature,
                "humidity": temp.humidity,
                "timestamp": temp.timestamp
            }
        )
        return {"msg": "created successfully", "created_data": temp, "client": request.client}
    except:
        documents = temp_collections.find()
        for document in documents:
            id = document["_id"]
            if id == temp.device_id:
                return {"msg": {f"id {temp.device_id} already exist in temp, try using other id"}}

# to run use this command uvicorn main:app --reload --host 0.0.0.0 --port 8182
