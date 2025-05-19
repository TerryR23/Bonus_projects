# This is a mapping of the channel jumps of Bluetooth packets

usedChannels = set()
offset = 5
connectionAddress = 0xE89BED68

def CheckChannel( channel:int):
    #Looks to see if the selected channel is already used
    if channel in usedChannels:
        return False
    else:
        return True


def RemapChannel(channel:int):
    if (len(usedChannels) == 37):
        for i in range(0, 37):
            usedChannels.remove(i)
            return 5
    else:
        match algorithm:
            case 1: 
                index = channel % len(usedChannels)
            case 2:
                index = ((3 * prn_e) // (2 ** 16))
    return index


def MamBlock(a:int, b:int):

    output = ((a * 17) + b) % (2 ** 16)
    return output

def Permutate(a:int):
    #This is a simple permutation function
    a &= 0xFFFF  # Ensure only 16 bits are considered

    low_byte = a & 0x00FF        # Lower 8 bits

    high_byte = (a & 0xFF00) >> 8 # Higher 8 bits

    return (low_byte << 8) | high_byte




if __name__ == "__main__":
    unmappedChannel = 0 #This is the channel that will be used for the connection event
    lastUnmappedChannel = 0 #This is the channel that was just being used

    i = 0

    algorithm = int(input("which algorithm would you like to use? (1 or 2):   "))
    num = input("How many connection events would you like to predict?:   ")
    try:
        num = int(num)
    except:
        exit(1)
    while( i <  num):
        match algorithm:
            case 1:
                unmappedChannel = (lastUnmappedChannel + offset) % 37
                #There is a logically loop error if the channel is zero and all channels have been used
                if CheckChannel(unmappedChannel) == False:
                    print("calling remap channel")
                    lastUnmappedChannel = unmappedChannel
                    unmappedChannel = RemapChannel(unmappedChannel)
                else: pass
                print("jumping to channel: ", unmappedChannel)
                usedChannels.add(unmappedChannel)
                lastUnmappedChannel = unmappedChannel
                i+=1

            case 2:
                # This is algorithm 2
                i = int(hex(i),16) #converts counter to a hex value
                temp = i ^ connectionAddress

                #The below section is the Pseudo random Number generator. 
                for count in range (0,3):
                    temp = Permutate(temp)
                    temp = MamBlock(temp, connectionAddress)
                
                prn_s = temp
                prn_e = temp ^ connectionAddress
                unmappedChannel = prn_e % 37
                if CheckChannel(unmappedChannel) == False:
                    print("calling remap Channel")
                    unmappedChannel = RemapChannel(unmappedChannel)
                else: pass
                print("jumping to channel: ", unmappedChannel)
                usedChannels.add(unmappedChannel)
                lastUnmappedChannel = unmappedChannel
                i+=1






