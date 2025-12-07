import network
from microdot import Microdot, Response
from machine import Pin, PWM
from time import sleep

Response.default_content_type = "text/html"

# ======================
# WiFi Setup
# ======================
SSID = "Ooredoo-1896D3"
PASSWORD = "25005634"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)
while not wifi.isconnected():
    print("Connecting to WiFi...")
    sleep(1)
print("Connected! IP:", wifi.ifconfig()[0])

# ======================
# Motor Pins Setup
# ======================
IN1 = Pin(25, Pin.OUT)
IN2 = Pin(26, Pin.OUT)
IN3 = Pin(27, Pin.OUT)
IN4 = Pin(14, Pin.OUT)

ENA = PWM(Pin(32))
ENB = PWM(Pin(33))
ENA.freq(1000)
ENB.freq(1000)

# ======================
# Motor Functions
# ======================
def motorA_forward(speed):
    IN1.on()
    IN2.off()
    ENA.duty_u16(speed)

def motorA_backward(speed):
    IN1.off()
    IN2.on()
    ENA.duty_u16(speed)

def motorB_forward(speed):
    IN3.on()
    IN4.off()
    ENB.duty_u16(speed)

def motorB_backward(speed):
    IN3.off()
    IN4.on()
    ENB.duty_u16(speed)

def turn_left(speed, direction="forward"):
    if direction == "forward":
        motorA_forward(speed)
        motorB_forward(int(speed/2))
    else:
        motorA_backward(speed)
        motorB_backward(int(speed/2))

def turn_right(speed, direction="forward"):
    if direction == "forward":
        motorA_forward(int(speed/2))
        motorB_forward(speed)
    else:
        motorA_backward(int(speed/2))
        motorB_backward(speed)

def stop_motors():
    IN1.off(); IN2.off(); IN3.off(); IN4.off()
    ENA.duty_u16(0)
    ENB.duty_u16(0)

# ======================
# Microdot App
# ======================
app = Microdot()

# serve index.html
@app.route("/")
def index(request):
    try:
        with open("ui.html") as f:
            return f.read()
    except:
        return "<h1>index.html not found</h1>"

# handle move commands
@app.route("/move")
def move(request):
    cmd = request.args.get("dir")
    speed = int(request.args.get("speed", 40000))

    print("Command:", cmd, "Speed:", speed)

    # Forward + Left example
    if cmd == "forward-left":
        motorA_forward(speed)
        motorB_forward(int(speed/2))
    elif cmd == "forward-right":
        motorA_forward(int(speed/2))
        motorB_forward(speed)
    elif cmd == "backward-left":
        motorA_backward(speed)
        motorB_backward(int(speed/2))
    elif cmd == "backward-right":
        motorA_backward(int(speed/2))
        motorB_backward(speed)
    elif cmd == "forward":
        motorA_forward(speed)
        motorB_forward(speed)
    elif cmd == "backward":
        motorA_backward(speed)
        motorB_backward(speed)
    elif cmd == "left":
        turn_left(speed)
    elif cmd == "right":
        turn_right(speed)
    else:
        stop_motors()

    return "OK"

# ======================
# Run the Server
# ======================
app.run(host="0.0.0.0", port=80)
