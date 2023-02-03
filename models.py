from pydantic import BaseModel


class Devices(BaseModel):
    id: int
    status: bool


class Log(BaseModel):
    status: str
    timestamp: int


class Devices_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str


class Fan_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str


class Mechanics_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str


class Led_details(BaseModel):
    id: int
    device_id: int
    device_name: str
    room: str
    type: str
    # log:og


class Log(BaseModel):
    device_id: int
    status: str
    timestamp: int
    updated_by: str


class Devices_put(BaseModel):
    status: bool


class Led(BaseModel):
    id: int

    status: bool
    R: str
    G: str
    B: str


class Led_put(BaseModel):
    status: bool
    R: str
    G: str
    B: str


class Fan(BaseModel):
    id: int
    status: bool
    speed: int


class Fan_put(BaseModel):
    status: bool
    speed: int


class Mechanics(BaseModel):
    id: int
    value: str


class Mechanics_put(BaseModel):
    id: int
    value: str


class Wta(BaseModel):
    id: int
    level: int


class Eb(BaseModel):
    id: int
    voltage: int
    amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int


class Eb_put(BaseModel):
    voltage: int
    amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int


class Eb3(BaseModel):
    id: int
    R_voltage: int
    Y_voltage: int
    B_voltage: int
    R_amp: float
    Y_amp: float
    B_amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int


class Eb3_put(BaseModel):
    R_voltage: int
    Y_voltage: int
    B_voltage: int
    R_amp: float
    Y_amp: float
    B_amp: float
    status: bool
    ups_voltage: int
    ups_AMP: int
    ups_battery_percentage: int


class Rooms(BaseModel):
    id: int
    name: str
    devices: list[int]
    fan: list[int]
    led: list[int]
    mechanics: list[int]
