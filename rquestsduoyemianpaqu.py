import requests
headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#r=requests.get("http://zyk.bjhd.gov.cn/zwdt/hdyw/index.shtml",headers=headers)
for i in range(0,50) :   
    if i==0:
       r=requests.get("http://zyk.bjhd.gov.cn/zwdt/hdyw/index.shtml",headers=headers) 
    else:
        r=requests.get("http://zyk.bjhd.gov.cn/zwdt/hdyw/index_{}.shtml".format(i),headers=headers) 
    r.encoding="utf8"
    print(r.url)
    with open("/home/chy/Desktop/chy/text5.txt",'w') as f:
        f.write(r.text)


