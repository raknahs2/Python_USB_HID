import pywinusb.hid as hid


def sample_handler(data):
    print("Raw data: {0}".format(data))

# VID and PID customization changes here...
filter = hid.HidDeviceFilter(vendor_id = 0x03eb, product_id = 0x2402)
hid_device = filter.get_devices()
device = hid_device[0]
device.open()
print(hid_device)
target_usage = hid.get_full_usage_id(0x00, 0x3f)
device.set_raw_data_handler(sample_handler)
print(target_usage)


report = device.find_output_reports()

print(report)
print(report[0])

buffer = [0x31]*11
buffer[0] = 0

# data to be transmitted from HID to UART
buffer[1] = 9  # data length;   Range->1 to 9
buffer[2] = 0x36 # data 1
buffer[3] = 0x33 # data 2
buffer[4] = 0x34 # data 3
buffer[5] = 0x35 # data 4
buffer[6] = 0x36 # data 5
buffer[7] = 0x37 # data 6
buffer[8] = 0x38 # data 7
buffer[9] = 0x39 # data 8
buffer[10] = 0x20 # data 9


print(buffer)

report[0].set_raw_data(buffer)
report[0].send()
