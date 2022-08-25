d = 256
 
# pat  -> pattern
# txt  -> text
# q    -> A prime number
 
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    
    h = 1
    num=0
 
    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q
 
    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
 
    for i in range(N-M+1):
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else: j+=1
 
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                num+=1
    
 
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
 
            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t+q
    print(num)
# Driver Code

 
# A prime number
q = 101
#txt=input()
#pat=input()
txt="abababababba"
pat="ab"

search(pat,txt,q)