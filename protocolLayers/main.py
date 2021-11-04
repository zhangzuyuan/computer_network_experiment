



from OSI.OSI import OSI


if __name__ == '__main__':
    ans = input('Please input the message:\n')

    #创建了两个OSI模型，模拟数据的传输
    net1 = OSI()
    net2 = OSI()

    print("The message that started the transmission is:",ans)

    #这里把要传输的数据发送给第一个模型，返回的是物理层编码完成后的编码
    encode_mes = net1.send(ans)

    #这里模拟另一个OSI接收到
    mes = net2.receive(encode_mes)
    
    print("The message that completes the transmission is:",mes)