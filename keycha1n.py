import dfu, utils, subprocess
kprint = utils.kprint

if __name__ == '__main__':
    print(">>> keycha1n by gurkentier v0.1")
    kprint("Credits and big thanks to axi0mX (https://github.com/axi0mX/ipwndfu) for the amazing checkm8 exploit and the ipwndfu utility!")
    kprint("Credits and big thanks to the checkra1n team for this great jailbreak utility! (https://checkra.in)")
    kprint("Searching for device in DFU mode...")
    device = dfu.acquire_device()
    identifier = device.serial_number
    kprint("Found iDevice in DFU mode with serial number: ")
    kprint(str(identifier))
    kprint(" ")
    kprint("Launching checkra1n jailbreak...")
    ######################################
    #TODO: launch checkra1n once released
    #args = ("bin/checkra1n", "--this-is-an-arg", "-flag")
    #checkra1n = subprocess.Popen(args, stdout=subprocess.PIPE)
    #checkra1n.wait()
    #output = checkra1n.stdout.read()
    #kprint("checkra1n stdout: ")
    #print(output)
    ######################################
    kprint("There is no linux version of the checkra1n jailbreak available at the moment.")
    kprint("We will update keycha1n as soon as the official Linux version is released.")
    kprint("Thanks for using keycha1n!")
    kprint("(c) by gurkentier 2019")