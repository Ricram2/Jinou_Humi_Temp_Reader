
import sys
import pexpect
DEVICE = "C7:DA:EB:01:F7:38"   #MAC address of your device
if len(sys.argv) == 2:
  DEVICE = str(sys.argv[1])


# Run gatttool interactively.
child = pexpect.spawn("gatttool -I")

# Connect to the device.
print("Connecting to:"),
print(DEVICE)
NOF_REMAINING_RETRY = 3
while True:
  try:
    child.sendline("connect {0}".format(DEVICE))
    child.expect("Connection successful", timeout=5)
  except pexpect.TIMEOUT:
    NOF_REMAINING_RETRY = NOF_REMAINING_RETRY-1
    if (NOF_REMAINING_RETRY>0):
      print ("timeout, retry...")
      continue
    else:
      print ("timeout, giving up.")
      break
  else:
    print("Connected!")
    child.sendline("char-read-hnd 0x0023")
    child.expect("Characteristic value/descriptor: ", timeout=10)
    child.expect("\r\n", timeout=10)
    print(child.before)

    hex_full = child.before;
    hex_temp_s = int(hex_full[0:2], 16);
    hex_temp = int(hex_full[3:5], 16);
    hex_temp_dec = int(hex_full[6:8], 16);
    hex_hum = int(hex_full[12:14], 16);
    hex_hum_dec = int(hex_full[15:18], 16);

    sign = "+";

    def hex_to_sign(hex): 

        if hex_temp_s == 0:
            sign = "+"
        elif hex_temp_s == 1:
            sign = "-"
        return sign

    hex_to_sign(hex_temp_s)
    print(sign,hex_temp,".",hex_temp_dec," | ",hex_hum,".",hex_hum_dec,"%")

    break