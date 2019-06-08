#!/usr/bin/python
file_name=input("enter the name or address of file")
f=open(file)
data=f.read()
words=len(data.split())
lines=len(data.splitlines())
print("no of words=",words)
print(lines)
