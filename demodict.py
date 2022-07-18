#DemoDict.py
device = {"아이폰":5, "윈도우":10}
print(device)
print(len(device))
print(device["아이폰"])
#입력
device["맥북"] = 15

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)


for v in device.values():
    print(v)

for k in device.keys():
    print(v)    

device2 = device 
print(id(device))    
print(id(device2))