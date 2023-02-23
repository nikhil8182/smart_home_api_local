from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["localSmartHomeServer"]

device_collections = db["devices"]
fan_collections = db["fan"]
led_collections = db["led"]
mechanics_collections = db['Mechanics']

device_detail_collections = db["devices_detail"]
fan_details_collections = db["fan_details"]
led_details_collections = db["led_details"]
mechanics_details_collections = db['Mechanics_details']

device_details_log_collections = db["devices_details_logs"]
fan_details_log_collections = db["fan_details_log"]
led_details_log_collections = db["led_details_log"]
mechanics_details_log_collections = db['Mechanics_details_log']

device_board_log_collections = db["devices_board_logs"]

eb_sensor_collections = db["eb_sensor"]
eb3phasae_sensor_collections = db["eb_sensor"]
wta_collections = db["wta"]

board_log_collections = db["board_log"]
room_collections = db["room"]
temp_collections = db["temperature"]
