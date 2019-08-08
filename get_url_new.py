import requests
import json
import yaml
yfile=open('test.yaml','r')
canshudata=yaml.load(yfile)



headars = {"Content-Type": "application/json;charset=UTF-8"}
body={'start': '2019-06-29','end': '2019-07-30','page':'2','size':'2'}
def get_url():

    responses=requests.post(url,headers=headars,data=body)
    res=responses.text
    res_code=responses.status_code
    in_json=json.loads(res)
    print(type(in_json))
    print(type(res))
    return res_code

def testdict():
    # data=canshudata['canshu']
    print(canshudata['canshu']['start'])

if __name__ == '__main__':
    testdict()
