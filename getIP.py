import  requests
import time
from bs4 import  BeautifulSoup
import  re
import sqlite3

agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'
headers = {
    # "Host": "www.xicidaili.com",
    # "Referer": "https://www.xicidaili.com/",
    'User-Agent': agent
}
url="http://www.xicidaili.com/"

session=requests.Session()

homeresponse=session.get(url=url, headers=headers)
soup=BeautifulSoup(homeresponse.text,'html.parser')
td=soup.findAll('tr', {'class': 'odd'}).__str__()
i=0
td2=[]

now = time.strftime("%Y-%m-%d") + ".db"
try:
    conn = sqlite3.connect(now)
except:
    print("Error to open database")
create_tb = '''
   CREATE TABLE IF NOT EXISTS PROXY
   (
   IP TEXT,
   PORT TEXT
   );
   '''
conn.execute(create_tb)

while i<=100:
    td2.append(re.findall('<td>(.*?)</td>',td)[i])
    td2.append(re.findall('<td>(.*?)</td>',td)[i+1])
    i=i+6
    insert_db_cmd = '''
        INSERT INTO PROXY (IP,PORT) VALUES ('%s','%s');
        ''' % (re.findall('<td>(.*?)</td>',td)[i], re.findall('<td>(.*?)</td>',td)[i+1])
    conn.execute(insert_db_cmd)
    conn.commit()  # 记得commit



print(td2)

conn.close()

