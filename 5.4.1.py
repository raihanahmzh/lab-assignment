from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.54.4',  #Your Server IP
    'username': 'rai', #your Server Username
    'password': 'abc123', #your server password
    'port' : 22,
    'secret': 'abc123',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
