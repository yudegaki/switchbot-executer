import pexpect, sys
from argparse import ArgumentParser

# ref: https://github.com/OpenWonderLabs/python-host/blob/master/switchbot.py#L200-L210
cmd_dict = {
    'TurnOn': '570101',
    'TurnOff': '570102',
    'Press': '570100',
    'Down': '570103',
    'Up': '570104'
}

def exec(mac_addr, action):
    conn = pexpect.spawn('gatttool -b ' + mac_addr + ' -t random -I')
    conn.expect('\[LE]')

    retry = 3
    while retry > 0:
        conn.sendline('connect')
        resp = conn.expect(['Error', 'Connection successful.*'])
        retry -= 1
        if resp != 0:
            break
        elif retry == 0:
            print('Connection Error')
            sys.exit(1)

    conn.sendline(f'char-write-cmd 0x0013 {cmd_dict[action]}')
    conn.expect('\[LE\]>')
    conn.sendline("quit")
    print("Complete!!")

def get_args():
    argparser = ArgumentParser()
    argparser.add_argument('-m', '--mac', help='Switch Bot Mac Address', required=True)
    argparser.add_argument('-c', '--cmd', help='Switch Bot Command', required=True, choices=['TurnOn', 'TurnOff', 'Press', 'Down', 'Up'])
    
    return argparser.parse_args()


def main():
    args = get_args()
    exec(args.mac, args.cmd) 

if __name__ == "__main__":
    main()