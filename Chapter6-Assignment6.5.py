6.5 Write code using find() and string slicing (see section 6.10) to extract the
number at the end of the line below. Convert the extracted value to a floating point
number and print it out.

Desired Output
0.8475

Code:
text = "X-DSPAM-Confidence:    0.8475"

str = "X-DSPAM-Confidence: 0.8475"
pos = str.find(":")
spos = str[pos+2 : ]
fspos = float(spos)
print(fspos)

Your Output
0.8475