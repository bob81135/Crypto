msg = "KTIAAQKITQAJWZML"

for i in range(26):
    ans = ""
    for j in msg:
        tag = ord(j)-i
        if(tag<65):
            ans+=chr(tag+26)
        else:
            ans+=chr(tag)
    print("key%d:%s"%(i,ans))
