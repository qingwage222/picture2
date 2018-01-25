import requests
from bs4 import BeautifulSoup
import random
import re
def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'dong')
    strb = '\n\r hello dong \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello d'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('ds')
    print 5, stra + strb + strc
    print 6, len(strb)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(" ")
    print 9, strc.find('l')


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5 | 3, 5 & 3, 5 ^ 4
class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __repr__(self):
        return 'im guest:' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group


def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')


def demo_exception():
    try:
        print 2 / 1
        print 2 / 0
        # if type == 'c':
        #raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print 'error:', e
    finally:
        print 'clean up'
def demo_random():
    random.seed(1)
    print 1,random.random()
    print 2,random.randint(0,50)
    print 3,random.choice(range(0,100,20))
    print 4,random.sample(range(0,100),2)
    a=[1,2,3]
    random.shuffle(a)
    print 5,a

def demo_re():
    str='abc123def12gh'
    p1=re.compile('[\d]+')
    p2=re.compile('\d')
    print p1.findall(str)
    print p2.findall(str)
    str='a@163.com;b@gmail.com;c@qq.com;d@qq.com'
    p3=re.compile('[\w]+@[163|qq]+\.com')
    print p3.findall(str)

if __name__ == '__main__':
    '''
    print 'hello world'
    print create_user('USERX')
    demo_exception()
    '''

    demo_re()
    #demo_random()

