# i2cdetect -y 1


from time import sleep
import smbus

MOISTURE_SENSOR_BUS = 1 # indicates /dev/i2c-1
ADDR = 0x8

moistureSensor = smbus.SMBus(MOISTURE_SENSOR_BUS)

sleep(0.5)

# resp = moistureSensor.read_byte(ADDR) # :)
# resp = moistureSensor.write_byte_data(ADDR, 0, 1) :)
resp = moistureSensor.read_i2c_block_data(ADDR, 0x62, 16)
# resp = moistureSensor.read_byte_data(ADDR, 10)
print(resp)

out = ''

for c in resp:
	if 0x20 <= c <= 0x7e:
		out += chr(c)
print(out)

# '<delimiter>'.join(list_of_char)


'''
resp = moistureSensor.read_byte(ADDR)
print(resp)
resp = moistureSensor.read_byte(ADDR)
print(resp)
resp = moistureSensor.read_byte(ADDR)
print(resp)
resp = moistureSensor.read_byte(ADDR)
print(resp)

block = moistureSensor.read_i2c_block_data(ADDR, 0)

'''
