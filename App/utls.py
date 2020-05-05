import base64
def make_date_secret(source):
    #base64 encode 后是二进制，在decode成字符串
    encode_content = base64.standard_b64encode(source.encode('utf-8')).decode("utf-8")
    print("encode_content",encode_content)
    add_content_encode = "5a4546703332746776646a6730324146" + encode_content + "6677657232334657464e56"
    print("add_content_encode",add_content_encode)
    encode_twice = base64.standard_b64encode(add_content_encode.encode('utf-8')).decode('utf-8')
    print("encode_twice",encode_twice)
    return encode_twice