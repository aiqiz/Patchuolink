
import serial
import time

ser = serial.Serial(
        port='/dev/cu.usbmodem2101',
        baudrate=9600,
        timeout=1
    )
time.sleep(1)

def read():
    RGB = []
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            data = ser.readline()
            data = data.decode().strip()  # Strip newline characters
            if data[0] == 'R' or data[0] == 'G'or data[0] == 'B':
                RGB.append(int(data[1:]))
            if len(RGB) == 3:
                print(RGB)
                return RGB
    
def colour(data):
    values = data[1:]

    error = [0,0,0]
    sum = 0
    sum_prev = 1000
    colour = None

    RGBlist = {"healthy1": [151,176,125], "healthy2": [173,197,135], 
               "healthy3": [123,140,86], "healthy4": [91,110,68], 
               "healthy5": [117,166,99],"healthy6": [97,141,68], 
               "healthy7": [91,117,66], "healthy8": [136,152,103],
               "healthy9": [118,121,114], "healthy10": [119,121,106],"unhealthy1": [158,162,136],
               "unhealthy2": [176,186,139], "unhealthy3": [153,172,131],
               "unhealthy4": [151,172,127],}
    
    for key, value in RGBlist.items():
        sum = 0

        for i in range (len(value)):
            error[i] = abs(data[i]-value[i])
            sum += error[i]

        if sum < sum_prev:
            colour = key
            sum_prev = sum

    print(colour)
    return colour

def distance(dummylist):
    # Process dummylist to calculate distances
    distance_list = []
    for i in range(len(dummylist) - 1):
        distance_list.append(dummylist[i + 1] - dummylist[i])
    return distance_list

dummy = []
timeout_counter = 0


while True:
    data = read()

    if data:
        if data[0] == "Distance":
            dummy.append(data)
        elif data[0] == "RGB":
            colour(data)
        timeout_counter = 0
    else:
        timeout_counter += 1
        if timeout_counter >= 10:  # Exit loop if no data received for 10 seconds
            break

dist = distance(dummy)
print(dist)
