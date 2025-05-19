# This is a mappign of the channel jumps of Bluetooth packets

usedChannels = set()
offset = 5

def CheckChannel( channel:int):
    #Looks to see if the selected channel is alread used
    if channel in usedChannels:
        return False
    else:
        return True


def RemapChannel(channel:int):
    if (len(usedChannels) == 37):
        for i in range( 0, 37):
            usedChannels.remove(i)
            index = 0
    
    else:
        index = channel % len(usedChannels)

    return index


if __name__=="__main__":
    unmappedChannel = 0 #This is the channel that will be used for the connection event
    lastUnmappedChannel = 0 #This is the channel that was just being used

    i = 0
    num = input("How many connetion events would you like to predict?:   ")
    try:
         num = int(num)
    except:
        exit(1)
    while( i <  num):
        unmappedChannel = (lastUnmappedChannel + offset) % 37
        if CheckChannel(unmappedChannel) == False:
            print("calling remap channel")
            unmmppedChannel = RemapChannel(unmappedChannel)

        else:
            pass

        
        print("jumping to channel: ", unmappedChannel)
        usedChannels.add(unmappedChannel)
        lastUnmappedChannel = unmappedChannel
        i+=1






