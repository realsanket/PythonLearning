from encodedecodemodule import encode,decode 
text=input("Type Message \n")
shift_num=int(input("Type Shift Number \n"))
operation=input("type encode or decode \n")



if operation=="encode":
    encode(text,shift_num)
else:
    decode(text,shift_num)   


