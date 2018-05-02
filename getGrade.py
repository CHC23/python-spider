import requests
import json
import jsonpath

session=requests.session()
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        # 'Cookie':'JSESSIONID=abcnrEh66aY5f_TvRX2lw; selectionBar=0'
    }

def urpLogin():#模拟登陆
    print("请输入学号和密码")
    j_username=input("请输入学号：")
    j_password=input("请输入密码：")
    userData={
        'j_username':j_username,
        'j_password':j_password,
        'j_captcha1': 'error'
    }
    session.post('http://xsjwxt.sxau.edu.cn:7873/j_spring_security_check',data=userData,headers=headers)

def getGrade():
    urpLogin()
    res=session.get('http://xsjwxt.sxau.edu.cn:7873/student/integratedQuery/scoreQuery/allPassingScores/callback')
    htmlData=res.text
    jsonData=json.loads(htmlData)                                           #转换json格式
    CnameList=jsonpath.jsonpath(jsonData,"$..courseName")                   #提取课程名
    CreditList =jsonpath.jsonpath(jsonData, "$..credit")                    #提取学分成绩
    GradeList=jsonpath.jsonpath(jsonData, "$..courseScore")                 #提取卷面成绩
    PointList=jsonpath.jsonpath(jsonData, "$..gradePointScore")             #提取绩点成绩
    for cna,cre,gra,poi in zip(CnameList,CreditList,GradeList,PointList):   #for循环打印列表
        print("课程名：",cna,"||","学分：",cre,"||","分数：",gra,"||","绩点：",poi)
        # reslut={
        #     "课程名":cna,
        #     "学分":cre,
        #     "成绩":gra,
        #     "绩点":poi
        # }
        # print(reslut)

if __name__=='__main__':
    try:
        getGrade()
    except:
        print("网络连接失败，请检查网络")