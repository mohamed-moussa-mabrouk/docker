fil = open(r"Pride and Prejudice.txt","r",encoding="utf-8")
x = fil.read()
y = x.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
inp_string = y
no_puncuation = ""
for char in inp_string:
   if char not in punctuations:
       no_puncuation = no_puncuation + char       
       
filee2 = open(r"Beyond the Wall of Sleep.txt","r",encoding="utf-8")
z = filee2.read()
w= z.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
inp_str = w
 
nopuncua = ""
for char in inp_str:
   if char not in punctuations:
       nopuncua = nopuncua + char   
document_text1 = no_puncuation
document_text2 = nopuncua

document_words1 = document_text1.split()
document_words2 = document_text2.split()

intersect = set(document_words1).intersection( set(document_words2 ) )

print(intersect)
