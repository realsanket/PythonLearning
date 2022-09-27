def encode(plain_text,shift_num):
    encoded_text=""
    for i in plain_text:
        ascii=ord(i)
        encoded_text+=chr(ascii+shift_num)
    print("The encode text is "+encoded_text)

def decode(text,shift_num):
    decode_text=""
    for i in text:
        ascii=ord(i)
        decode_text+=chr(ascii-shift_num)
    print("The decoded text is "+decode_text)
