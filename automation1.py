# Task to classify Private and Public IP address from IOC
def get_octet(ip):
    perbyte = []
    start = 0
    for i,c in enumerate(ip):
        if c == '.':
            perbyte.append(int(ip[start:i]))
            start = i+1
    perbyte.append(int(ip[start:len(ip)]))
    return(perbyte)


def compare_octet(ip):
    if ip[0] == 10:
        if ip[1] >= 0 and ip[1] <= 255:
            if ip[2] >= 0 and ip[2] <= 255:
                if ip[3] >= 0 and ip[3] <= 255:
                    return(True)

    if ip[0] == 172:
        if ip[1] >= 16 and ip[1] <= 31:
            if ip[2] >= 0 and ip[2] <= 255:
                if ip[3] >= 0 and ip[3] <= 255:
                    return(True)
        else:
            return(False)

    if ip[0] == 192:
        if ip[1] == 168:
            if ip[2] >= 0 and ip[2] <= 255:
                if ip[3] >= 0 and ip[3] <= 255:
                    return(True)
        else:
            return(False)

    else:
        return(False)

if __name__ in ('__main__', '__builtin__', 'builtins'):
    list = demisto.args().get('list')
    private_ip = []
    public_ip = []
    print(len(list))
    i = 1
    for i in range(0,len(list)):
        print(compare_octet(get_octet(list[i])))
        if compare_octet(get_octet(list[i])) == True:
            private_ip.append(list[i])
        else:
            public_ip.append(list[i])
    context = {'PrivateIP': private_ip, 'PublicIP': public_ip}
    demisto.results({
        'Type': entryTypes['note'],
        'ContentsFormat': formats['json'],
        'Contents': context,
        'HumanReadable': context,
        'EntryContext': context
        })
