from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["localSmartHomeServer"]

device_collections = db["devices"]
device_detail_collections = db["devices_detail"]
device_details_log_collections = db["devices_details_logs"]
device_board_log_collections = db["devices_board_logs"]
fan_board_log_collections = db["fans_board_logs"]

fan_collections = db["fan"]
led_collections = db["led"]
mechanics_collections = db['Mechanics']

fan_details_collections = db["fan_details"]
led_details_collections = db["led_details"]
mechanics_details_collections = db['Mechanics_details']

fan_details_log_collections = db["fan_details_log"]
led_details_log_collections = db["led_details_log"]
mechanics_details_log_collections = db['Mechanics_details_log']

eb_sensor_collections = db["eb_sensor"]
eb_status_collections = db["eb_status"]

eb_ups_voltage_collections = db["eb_ups_voltage"]
eb_ups_ampere_collections = db["eb_ups_ampere"]

eb3phasae_sensor_collections = db["eb_sensor"]
eb3phasae_voltage_collections = db["eb3_voltage"]
eb3phasae_ampere_collections = db["eb3_ampere"]

wta_collections = db["wta"]

board_log_collections = db["board_log"]
room_collections = db["room"]
temp_collections = db["temperature"]
