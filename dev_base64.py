#! /user/bin/evn python3
#! --coding=utf-8--

import base64
print("=======start=================")
origin ="this is for base code"
print("origin:",origin)
encode =base64.b64encode(bytes(origin,'utf-8'))
print('encode',encode)
decode  = base64.b64decode(encode)
print('decode',decode)
print("success" if origin==str(decode,'utf-8') else "fail")


print("====================")
target ="YGBgYWJiYmJiYmJiYmNjY2NjY2NjY2NjY2NjYmJiYmFhYWFhYWFhYWBgYGBfX19fX19fX19fX19fX19fX19fX19fX19fX19eXl5eXl5eXl5eXl5eXl5eXl5fX19fX19fX19fX19fX19fX19fX15eXl5eX19fX19fX19fX19fX19fX19fX19fX19fX19fX19gYGBgX19fX19fX19fX19fX19fX19fX19fYGBgYGBgYGBgX19fX19fX19fX19fX19fX19gYGBgYGBgYGBgYGBfX19fX19fX19fX19fX19fYGBgYGBgYGBgYF9fX19fX19fX19fX19fX19fX19gYGBgYGBgYGBgX19fX19fX19fX19fX2BgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYF9fX19fX2BgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYF9fX19fX2BgYGBgYGBgYGBgYWFhYWFgYGBgYGBgYWFhYWFhYWBgYGBgYGBgYGBgYGBgYGBgYF9fX19fX19gYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYF9fX19gYGBgYGBgYGBgYGBgYGBfX19eXl9fX19gYGBgYGBgYGBgYF9fX19gYGBfX19fX19fX19fX19fYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBgYGBfX19fX19fYGBgYGBgYGBgYGBgYGBgYGFhYGBgYGBgYGBfX19fX19fX19fX2BgYGBgYGBgYGBfX19fX19gYGBgYGBgX19fX19fX19fX19fX19fYGBgYGBgYGBgYGBgYGBgX19fX19fX19fX19fX19fX19fX19fX19fX19fX2BgYGBfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19gYGFhYWJhYWFhYWFhYF9fXl5eXVxcW1tbXFxdXl9fYGBgYGBfX19eXl1dXV1dXV1dXV5eXl9fX15eXV1dXV1dXFxcXF1dXV5eX19fX19fXl1dXFxbWlpaW1xdXV5fYGBfX19eXl5dXVxcXFxdXV5eX19fXl5eXV1dXFtaWVlYV1ZWVVVVVlhZW1xdXl5dXV1dXl5eXl5eXl5eXl5eXl5eXV1dXFtaWVhWVlVUU1JRUVFTU1VVVlZYWlxeXl5eXl4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY2NjY2NjY2NjY2NiYmJiYWFhYWFhYWFhYWBgYGBgX15dXV1cXFxcXV5fX2BhYWFhYWFgYGBgX19eXl5eXV1cW1pZWlpbXF1eX2FgYGBgYGBgYGBfX19fXl5dXVxbWllYV1ZWVVVUVFRUVVVWVldZW1xeX19eXV1cW1pZWVlZWFhXVlVVVVVWVldXWVpbXV5gYGBgYGBgYF9fX19fX2BgYGBfX19fX19fX19fX15eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXl5eXV1dXV1dXQ=="
decode_tar = base64.b64decode(target)
print("length:",len(decode_tar),"decode tar",decode_tar)
print("success" if len(decode_tar) % 4==0 else "fail")
print(1834//2)
