import time

start = time.time()
n = int(input())
while n > 5:
    print('okay')
    n = int(input())
end = time.time() - start
print(end)
name = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime())

with open(name + '.txt', 'w') as file:
    file.write(str(end))
