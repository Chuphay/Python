alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
craze = "LDCTFJUEBGQRWZAYKVNPOMHXSI"

def encrypt(s,key):
    s = s.replace("\n", "")
    s = s.lower()
    output = ""
    for i in s:
        try:
            j = (alpha.index(i)+key)%len(alpha)
            output += ALPHA[j]
        except ValueError:
            output += i 
    if key<0:
        output = output.lower()
        return output
    else:           
        return output
jedi = open("/home/chuphay/python/projects/codes/text/jedi.txt").read()
e = encrypt("""The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down what seemed to be a very deep well. Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her, and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything: then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves: here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed: it was labeled "ORANGE MARMALADE," but to her great disappointment it was empty: she did not like to drop the jar, for fear of killing somebody underneath, so managed to put it into one of the cupboards as she fell past it.""",3)
print e
import random        
message = list(ALPHA) 
random.shuffle(message)
message = ''.join(message)
#print message        
       
