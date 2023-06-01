import requests

url = "https://api.q1q1.cn/api/idcard"

info = input("Please enter your name and ID card number:")
split_info = info.split()

if len(split_info) == 2:
    name,cardno = split_info
    data = {
    "name":name,
    "cardno":cardno
    }
    if len(cardno) == 18:
       response = requests.post(url,data=data).json()
       status_code = response["ret"]
       if status_code == 200:
         message =response["msg"]
         real_name = response["data"]["real_name"]
         idcard = response["data"]["idcard"]
         print(f"name:{real_name} ID card:{idcard} msg:{message}")
       else:
        print(f"{info} msg:{response['msg']}")
    else:
        print("The format of the ID card is incorrect.")
        exit()
else: 
    print("Please enter your name and ID card number correctly!")
    exit()