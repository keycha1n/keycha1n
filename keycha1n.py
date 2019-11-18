import dfu

if __name__ == '__main__':
    device = dfu.acquire_device()
    identifier = device.serial_number
    print(identifier)