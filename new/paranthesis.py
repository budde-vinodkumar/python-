s="()"
stack=[]
for ch in s:
    if ch=="(": stack.append(ch)
    else: stack.pop()
print("Balanced" if not stack else "Not")
