import execnet

def square(channel):
    while not channel.isclosed():
        number = channel.receive()
        no_2 = number ** 2
        channel.send(no_2)

gateway = execnet.makegateway()
channel = gateway.remote_exec(square)

for i in range(10):
    channel.send(i)
    i_2 = channel.receive()
    print(f"{i} squared is {i_2}")

gateway.exit()