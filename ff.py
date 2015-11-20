# help  
# python json_format.py json_text  
import os  
import sys  
import json  
  
length = len(sys.argv)  
  
print ("==================================")
if length > 1:  
    try:  
        jsonstr = sys.argv[1]  
        jsonObj = json.loads(jsonstr)  
        formatJsonStr = json.dumps(jsonObj,indent=4,ensure_ascii=False,sort_keys=True)  
  
        print (formatJsonStr) 
    except Exception:  
        # print e  
        print ("json parse error.")  
else :  
    print ("argv's length is 1, no json text input.")  
print("==================================")