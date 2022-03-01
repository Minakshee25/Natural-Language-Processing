# code by Minakshee Narayankar
from nltk import word_tokenize
def preprocess(d):
    d=d.lower()
    d="eos "+ d
    d=d.replace("."," eos")
    return d
def generate_tokens(d):
    tokens = word_tokenize(d)
    return tokens
def generate_tokens_freq(tokens):
    dct={}
    for i in tokens:
        dct[i]=0
    for i in tokens:
        dct[i]+=1
    return dct
def generate_ngrams(tokens,k):
    l=[]
    i=0
    while(i<len(tokens)):
        l.append(tokens[i:i+k])
        i=i+1
    l=l[:-1]
    return l
def generate_ngram_freq(bigram):
    dct1={}
    for i in bigram:
        st=" ".join(i)
        dct1[st]=0
    for i in bigram:
        st=" ".join(i)
        dct1[st]+=1
    return dct1
def find1(s,dct1):
    try:
        return dct1[s]
    except:
        return 0
def print_probability_table(distinct_tokens,dct,dct1):
    n=len(distinct_tokens)
    l=[[]*n for i in range(n)]
    for i in range(n):
        denominator = dct[distinct_tokens[i]]
        for j in range(n):
            numerator = find1(distinct_tokens[i]+" "+distinct_tokens[j],dct1)
            l[i].append(float("{:.3f}".format(numerator/denominator)))
    return l
d=input("Enter corpus = ")
print("\n"+'\033[1m'+"Given Corpus"+'\033[0m')
print(d)

d=preprocess(d)
print("\n"+'\033[1m'+"Preprocessing"+'\033[0m')
print(d)

tokens=generate_tokens(d)
print("\n"+'\033[1m'+"Generate Tokens"+'\033[0m')
print(tokens)

distinct_tokens = list(set(sorted(tokens)))
dct=generate_tokens_freq(tokens)
print("\n"+'\033[1m'+"Generate Frequency of Tokens"+'\033[0m')
print(dct)

bigram = generate_ngrams(tokens,2)
print("\n"+'\033[1m'+"Generate bigrams"+'\033[0m')
for i in bigram:
    print("'{}'".format(' '.join(i)), end=", ")

dct1=generate_ngram_freq(bigram)
print("\n\n"+'\033[1m'+"Generate Frequency of bigrams"+'\033[0m')
print(dct1)

probability_table=print_probability_table(distinct_tokens,dct,dct1)
print("\n"+'\033[1m'+"Probability table"+'\033[0m'+"\n")

n=len(distinct_tokens)
print("\t"+'\033[1m', end="")
for i in range(n):
    print(distinct_tokens[i],end="\t")
print('\033[0m'+"\n")

for i in range(n):
    print('\033[1m',distinct_tokens[i],'\033[0m',end="\t")
    for j in range(n):
        print(probability_table[i][j],end="\t")
    print("")

print("\n","-"*100)
text = input("\nEnter text to check its probability = ")
print("\n"+'\033[1m'+"Given Text"+'\033[0m')
print(text)

p = preprocess(text)
print("\n"+'\033[1m'+"Preprocessing"+'\033[0m')
print(p)

t=generate_tokens(p)
print("\n"+'\033[1m'+"Generate Tokens"+'\033[0m')
print(t)

n = generate_ngrams(t,2)
print("\n"+'\033[1m'+"Generate bigrams"+'\033[0m')
for i in n:
    print("'{}'".format(' '.join(i)), end=", ")
print("\n\n"+'\033[1m'+"Calculate bigram probability"+'\033[0m')
s=1
dct2={}
for i in n:
    dct2[" ".join(i)]=0
    
for i in n:
    k=distinct_tokens.index(i[0])
    m=distinct_tokens.index(i[1])
    dct2[" ".join(i)]=probability_table[k][m]
    print("P('{}')\t=  ".format(' '.join(i)),probability_table[k][m])
    s*=probability_table[k][m]

print("\n"+'\033[1m'+ "Calculate Probability of the sentence"+'\033[0m')
print(f"P('{text}') \n= ",end="")
x=dct2.popitem()
for i in dct2:
    print(f"P('{i}')", end=" * ")
print(f"P('{x[0]}')\n= ", end='')

for i in dct2:
    print(dct2[i], end=" * ")
print(x[1],"\n=",s)

print("\n"+'\033[1m'+f"Probability('{text}') = "+"{:.5f}".format(s))



'''
output format:
Enter corpus = I am a girl. I like Quant. Nisha like Eng. I know it.

Given Corpus
I am a girl. I like Quant. Nisha like Eng. I know it.

Preprocessing
eos i am a girl eos i like quant eos nisha like eng eos i know it eos

Generate Tokens
['eos', 'i', 'am', 'a', 'girl', 'eos', 'i', 'like', 'quant', 'eos', 'nisha', 'like', 'eng', 'eos', 'i', 'know', 'it', 'eos']

Generate Frequency of Tokens
{'eos': 5, 'i': 3, 'am': 1, 'a': 1, 'girl': 1, 'like': 2, 'quant': 1, 'nisha': 1, 'eng': 1, 'know': 1, 'it': 1}

Generate bigrams
'eos i', 'i am', 'am a', 'a girl', 'girl eos', 'eos i', 'i like', 'like quant', 'quant eos', 'eos nisha', 'nisha like', 'like eng', 'eng eos', 'eos i', 'i know', 'know it', 'it eos', 

Generate Frequency of bigrams
{'eos i': 3, 'i am': 1, 'am a': 1, 'a girl': 1, 'girl eos': 1, 'i like': 1, 'like quant': 1, 'quant eos': 1, 'eos nisha': 1, 'nisha like': 1, 'like eng': 1, 'eng eos': 1, 'i know': 1, 'know it': 1, 'it eos': 1}

Probability table

	like	it	i	know	girl	eos	a	quant	eng	nisha	am	

 like 	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.5	0.5	0.0	0.0	
 it 	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	
 i 	0.333	0.0	0.0	0.333	0.0	0.0	0.0	0.0	0.0	0.0	0.333	
 know 	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	
 girl 	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	
 eos 	0.0	0.0	0.6	0.0	0.0	0.0	0.0	0.0	0.0	0.2	0.0	
 a 	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	
 quant 	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	
 eng 	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	
 nisha 	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	
 am 	0.0	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	

 ----------------------------------------------------------------------------------------------------

Enter text to check its probability = Nisha like quant.

Given Text
Nisha like quant.

Preprocessing
eos nisha like quant eos

Generate Tokens
['eos', 'nisha', 'like', 'quant', 'eos']

Generate bigrams
'eos nisha', 'nisha like', 'like quant', 'quant eos', 

Calculate bigram probability
P('eos nisha')	=   0.2
P('nisha like')	=   1.0
P('like quant')	=   0.5
P('quant eos')	=   1.0

Calculate Probability of the sentence
P('Nisha like quant.') 
= P('eos nisha') * P('nisha like') * P('like quant') * P('quant eos')
= 0.2 * 1.0 * 0.5 * 1.0 
= 0.1

Probability('Nisha like quant.') = 0.10000
'''
