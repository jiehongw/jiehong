import urllib.request
pic_paidaxin="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1578047322273&di=5e9d9c462845b335cfabd4cb3b7af3c3&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2Ff319da6f0ace1d8d3fd2aa31051f977526978eb918657-N0EIPb_fw658"
pic_resp=urllib.request.urlopen(pic_paidaxin)
pic=pic_resp.read()
with open("bd_logo.png","wb")as f:
    f.write(pic)
