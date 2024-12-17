import qwiic_i2c

#results = qwiic.list_devices()
#print(results)

#mydevice = qwiic.create_device(results[1][0])
#print(mydevice)

my_bus = qwiic_i2c.get_i2c_driver()
scan_list = my_bus.scan()
print("Bus Scan:", scan_list)

ping_result = my_bus.ping(93)
print("Device is connected:", ping_result)

read_data = my_bus.read_byte(93, register_address)
print("Read byte:", read_data)
