
#Given starting IP and subnet mask, as well as ranges for addresses and names, I should be able to organize them and subnet them. started on tues i think (8/29/18)

print("When asked for information, write in the order given and separate each one with a space.")
print("")
startingInfo = input("Input the starting IP address and the starting subnet mask for your network. ")  # Asking for IP and subnet as string
startingInfo = startingInfo.split()     # Splitting them into IP and subnet variables
startingIP = (startingInfo[0].split("."))    # Splitting IP into octets
startingMask = (startingInfo[1].split("."))    # Splitting subnet into octets
subnet = 1  # Used for tracking total subnets and active subnets during loop
networkInfo = []
networkName =  []    #establishing lists with empty values
networkHosts = []
networkNumber = []  # largest to smallest subnets
subNetworkName = []
subNetworkHosts = []
subNetworkRange = []

print(".".join(startingIP) + " is the starting IP. The subnet mask is " + ".".join(startingMask) + ".")
print("In the event of multiple networks with the same amount of hosts, the first network entered will take precedence.")
while 1 > 0:    
    #networkInfo.append(input("Input the name (with no spaces) and the amount of hosts in the network. "))
    #networkName.append(networkInfo[subnet - 1].split()[0])
    #networkHosts.append(int(networkInfo[subnet - 1].split()[1]))
    networkName.append(0)
    networkHosts.append(0)
    networkName[subnet - 1], networkHosts[subnet - 1] = input("Input the name (with no spaces) and the amount of hosts in the network. ").split()   # splits the name/hosts into their own lists
    if input("Do you have another range; [y] or [n] ") == "n":
        break   # ends loop if no networks left
        print("Calculating subnets...")
    else:
        subnet = subnet + 1

x = 0
while x < subnet:
    networkNumber.append(0)     # creates an empty list for organizing largest to smallest networks
    x += 1
    #networkHostsFodder.append(int(networkHosts[x]))
z = 0       # turn hosts into ints

while z < subnet:
    x = 0   # checks and organizes each network from largest to smallest
    while x < subnet:
        if int(networkHosts[x]) > int(networkHosts[networkNumber[z]]):  # have to make it reloop and pick 2nd, 3rd, 4th, etc.
            networkNumber[z] = x    # stores the network's numbers (which network it was entered as Ex. second network entered) based on their size
        x += 1
    networkHosts[networkNumber[z]] = -1*int(networkHosts[networkNumber[z]]) # take the highest of that loop and denote it as negative
    z += 1

print(networkHosts)
print(networkNumber)                 # troubleshooting!!!!

# now time to take the biggest network, assign it a subnet mask/range, and work down
z = 0
x = 0

while z < len(networkNumber):
    subNetworkName.append(0)
    subNetworkName[z] = networkName[networkNumber[z]]  # assigns the zth network's name
    if z > 0:
        subNetworkRange.append(0)
        subNetworkRange[z] = subNetworkRange[z - 1] + 2**x   # finds the end of the previous network if not the first 
    else:
        subNetworkRange.append(0)
        subNetworkRange[0] = (int(startingIP[0]) * 16777216) + (int(startingIP[1]) * 65536) + (int(startingIP[2]) * 256) + int(startingIP[3]) # starts at the starting IP if first network
    x = 0
    while 2**x - 2 <= -1 * int(networkHosts[networkNumber[z]]):
        x += 1                                      # calculates the overall hosts offered by the network
    #subNetworkHosts = 2**x
    print()
    print("Network " + subNetworkName[z] + ":")
    y = [0, 0, 0, 0]
    y[0] = subNetworkRange[z] % 256
    y[1] = subNetworkRange[z] % 65536 - y[0]
    y[2] = subNetworkRange[z] % 16777216 - y[0] - y[1]      # finds each individual octet
    y[3] = subNetworkRange[z] - y[0] - y[1] - y[2]
    print("Name: " + str(int(y[3] // 16777216)) + "." + str(int(y[2] // 65536)) + "." + str(int(y[1] // 256)) + "." + str(y[0]))    # prints seperated address
    i = 0
    while i < 4:
        if x < 8 * (3 - i):     # if there are less host bits than the bits up to that octet then the address must match
            y[i] = 255
        elif x > 8 * (4 - i):         # if there are more host bits than bits up to the octet, it must be zero     (keep in mind that y for IPs is tracked from left to right, while the mask is calculated from right to left)
            y[i] = 0
        else:
             y[i] = 256-2**(x - 8 * (3-i))  # if there is no bit overkill, the mask must be calculated
        i += 1

    print("Subnet Mask/CITR Number: " + str(y[0])  + "." + str(y[1]) + "." + str(y[2]) + "." + str(y[3]) + " or /" + str(32-x))
    y[0] = subNetworkRange[z] % 256
    y[1] = subNetworkRange[z] % 65536 - y[0]
    y[2] = subNetworkRange[z] % 16777216 - y[0] - y[1]      # finds each individual octet again
    y[3] = subNetworkRange[z] - y[0] - y[1] - y[2]
    print("First Usable IP: " +  str(int(y[3] // 16777216)) + "." + str(int(y[2] // 65536)) + "." + str(int(y[1] // 256)) + "." + str(y[0] + 1))    # y's must be reset
    y[0] = (subNetworkRange[z] + 2**x - 1) % 256                     # recalculates the octets after hosts factored in
    y[1] = (subNetworkRange[z] + 2**x)% 65536 - y[0]
    y[2] = (subNetworkRange[z] + 2**x)% 16777216 - y[0] - y[1]
    y[3] = (subNetworkRange[z] + 2**x) - y[0] - y[1] - y[2]
    print("Last Usable IP: " + str(int(y[3] // 16777216)) + "." + str(int(y[2] // 65536)) + "." + str(int(y[1] // 256)) + "." + str((y[0] - 1)))    # prints final addresses
    print("Broadcast IP: " + str(int(y[3] // 16777216)) + "." + str(int(y[2] // 65536)) + "." + str(int(y[1] // 256)) + "." + str((y[0])))
    z += 1          # adds 1 to loop counter
        # subNetwork____: mask, range, hosts, name

print()
print("Thank you for using this Subnet Calculator, made by Jacob Gray!")
input("Press enter when you are done.")




















