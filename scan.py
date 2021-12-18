import socket
import threading
import queue

IP_ADDRESS='0.0.0.1'
q=queue.Queue()

#storing ports
for i in range(0,65536):
    q.put(i)

def scanner(IP_ADDRESS):
    while not q.empty():
        port=q.get()
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            for i,j,k,l in range(0,256):
                IP_ADDRESS=str(i)+'.'+str(j)+'.'+str(k)+'.'+str(l)
                try:
                    s.connect((IP_ADDRESS,port))
                    with open('openport.txt','a') as fo:
                        fo.write(str(port)+'\n')
                except Exception as e:
                    with open('closeport.txt','a') as fo:
                        fo.write(str(port)+'\n')
        q.task_done()

for _ in range(30):
    t=threading.Thread(target=scanner,daemon=True)
    t.start()

q.join()
print('Done')            
    

