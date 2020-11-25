#!/usr/bin/env python
# coding: utf-8

# In[1]:


listf = "abcdefghijklmnopqrstuvwxyz"
codes = [ord(letter) - 97 for letter in listf]
print(listf,'\n'+str(codes))


# In[4]:


inp = input("Enter the word to encode: ").lower()

encode_chars = []
for i in inp:
    a_code = int(ord(i)-97)
    enc = (2 + 2*a_code)%26
    encode_chars.append(enc)

print(encode_chars)


# In[5]:


encoded_letters = []
for i in encode_chars:
    enc = chr(i+97)
    encoded_letters.append(enc)
    
print(encoded_letters)
    


# In[3]:


inp1 = input("Enter the word to decode: ").lower()
decoded_chars = []
for i in inp1:
    codec = int(ord(i)-97)
    decoded_chars.append(codec)
    
print(decoded_chars)


# In[14]:


decoded_letters = []
alt_decoded_letters = []
for i in decoded_chars:
    c = int((i -2)/2)
    c_a = int((i+24)/2)
    a_decode = chr(c + 97)
    alt_decode = chr(c_a + 97)
    decoded_letters.append(a_decode)
    alt_decoded_letters.append(alt_decode)

print(decoded_letters,'\n',alt_decoded_letters)


# In[ ]:




