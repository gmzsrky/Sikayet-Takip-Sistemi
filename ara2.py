
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup as bs
import mysql.connector
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import os



str5=''
baslik='Dalin'

headers_param = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
r = requests.get("https://www.sikayetvar.com/"+baslik, headers=headers_param)
if r.status_code !=200:
    print('bulunamadi.')
else:
    soup =bs(r.content,'html.parser')
    print(soup.title)
    entryler=soup.find_all('div',attrs={"class":"brandsearch-cards clearfix"})
    x=soup.find_all('article')
    print('Entryler' , sep='\n')

baglanti=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sikayet')
isaretci=baglanti.cursor()
isaretci.execute("SELECT calisan.mail FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad='Dalin'")
veri=isaretci.fetchall()
str1=''.join(map(str,veri))
str1=str1.lstrip("('")
str1=str1.rstrip("',)")
print(str1)
isaretci.execute("SELECT calisan.ad FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad='Dalin'")
adi1=isaretci.fetchall()
ad1=''.join(map(str,adi1))
ad1=ad1.lstrip("('")
ad1=ad1.rstrip("',)")
print(ad1)
isaretci.close()
baglanti.close()
#-------------------------------------------------------------------
# Gmail email sunucusuna baðlanma
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("gamzes.kaya@gmail.com", "yarikeciyariinsan")

    mesaj = MIMEMultipart()
    mesaj["From"] = "gamzes.kaya@gmail.com"           # GÃ¶nderen
    mesaj["To"] = str1          # alici
    mesaj["Subject"] = "Dalin Hakkýndaki Þikayetler"    # Konusu

    for num, entry in enumerate(x, ) :
        yazar = entry.find('span','profile-name')
        tarih = entry.find('span','time-history')
        icerik = entry.find('p','card-text')
       
     
        sikayet_icerik ='{}. {} \n\nyazar: {}, tarih{}'.format(
          num,icerik,yazar,tarih)
 
        body = sikayet_icerik

        body_text = MIMEText(body, "plain")  #
        mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail baþarýlý bir þekilde gönderildi.")
    mail.close()

#hata alýrsak yazdýrmak için
except:
    print("Hata:", sys.exc_info()[0])
   
#-----------------------------------------------------------------  
baslik='Flormar'

headers_param = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
r = requests.get("https://www.sikayetvar.com/"+baslik, headers=headers_param)
if r.status_code !=200:
    print('bulunamadi.')
else:
    soup =bs(r.content,'html.parser')
    print(soup.title)
    entryler=soup.find_all('div',attrs={"class":"brandsearch-cards clearfix"})
    x=soup.find_all('article')
    print('Entryler' , sep='\n')

baglanti=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sikayet')
isaretci2=baglanti.cursor()
isaretci2.execute("SELECT calisan.mail FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad='Flormar'")
veri2=isaretci2.fetchall()
str2=''.join(map(str,veri2))
str2=str2.lstrip("('")
str2=str2.rstrip("',)")
isaretci2.execute("SELECT calisan.ad FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad='Flormar'")
adi2=isaretci2.fetchall()
ad2=''.join(map(str,adi2))
ad2=ad2.lstrip("('")
ad2=ad2.rstrip("',)")
print(ad2)

isaretci.close()
baglanti.close()
#-------------------------------------------------------------------
# Gmail email sunucusuna baðlanma
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("gamzes.kaya@gmail.com", "yarikeciyariinsan")

    mesaj = MIMEMultipart()
    mesaj["From"] = "gamzes.kaya@gmail.com"           # GÃ¶nderen
    mesaj["To"] = str2          # alici
    mesaj["Subject"] = "Flormar Hakkýndaki Þikayetler"    # Konusu

    for num1, entry in enumerate(x, ) :
        yazar = entry.find('span','profile-name')
        tarih = entry.find('span','time-history')
        icerik = entry.find('p','card-text')
       
     
        sikayet_icerik ='{}. {} \n\nyazar: {}, tarih{}'.format(
          num1,icerik,yazar,tarih)
 
        body = sikayet_icerik

        body_text = MIMEText(body, "plain")  #
        mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail baþarýlý bir þekilde gönderildi.")
    mail.close()

# hata alýrsak yazdýrmak için
except:
    print("Hata:", sys.exc_info()[0])
   


#-----------------------------------------------------------
baslik='Danone'

headers_param = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"}
r = requests.get("https://www.sikayetvar.com/"+baslik, headers=headers_param)
if r.status_code !=200:
    print('bulunamadi.')
else:
    soup =bs(r.content,'html.parser')
    print(soup.title)
    entryler=soup.find_all('div',attrs={"class":"brandsearch-cards clearfix"})
    x=soup.find_all('article')
    print('Entryler' , sep='\n')

baglanti=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sikayet')
isaretci3=baglanti.cursor()
isaretci3.execute("SELECT calisan.mail FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad='Danone'")
veri3=isaretci3.fetchall()
str3=''.join(map(str,veri3))
str3=str3.lstrip("('")
str3=str3.rstrip("',)")
isaretci3.execute("SELECT calisan.ad FROM calisan,calisan_sirket,sirket WHERE calisan.calisan_id=calisan_sirket.calisan_id AND calisan_sirket.sirket_id=sirket.sirket_id AND sirket.ad='Danone'")
adi3=isaretci3.fetchall()
ad3=''.join(map(str,adi3))
ad3=ad3.lstrip("('")
ad3=ad3.rstrip("',)")
print(ad3)

isaretci.close()
baglanti.close()
#-------------------------------------------------------------------
# Gmail email sunucusuna baðlanma
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("gamzes.kaya@gmail.com", "yarikeciyariinsan")

    mesaj = MIMEMultipart()
    mesaj["From"] = "gamzes.kaya@gmail.com"           # GÃ¶nderen
    mesaj["To"] = str3          # alici
    mesaj["Subject"] = "Danone Hakkýndaki Þikayetler"    # Konusu

    for num2, entry in enumerate(x, ) :
        yazar = entry.find('span','profile-name')
        tarih = entry.find('span','time-history')
        icerik = entry.find('p','card-text')
       
     
        sikayet_icerik ='{}. {} \n\nyazar: {}, tarih{}'.format(
          num2,icerik,yazar,tarih)
 
        body = sikayet_icerik

        body_text = MIMEText(body, "plain")  #
        mesaj.attach(body_text)

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail baþarýlý bir þekilde gönderildi.")
    mail.close()

# hata alýrsak yazdýrmak için
except:
    print("Hata:", sys.exc_info()[0])
   
class Dialog(QDialog):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        grid=QGridLayout()
       
        '''combo=QComboBox(self)
        combo.addItem('Dalin')
        combo.addItem('Flormar')
        combo.addItem('Danone')
        grid.addWidget(combo,0,1)
#birinci satÄ±r
        index = combo.currentIndex()
        sayac=index'''
        grid.addWidget(QLabel("Sirket Adi:"),0,0)
        self.companycode=QLineEdit()
        grid.addWidget(QLabel('Dalin'),0,1)
        grid.addWidget(QLabel("Sirket Adi:"),0,2)
        self.companycode=QLineEdit()
        grid.addWidget(QLabel('Flormar'),0,3)
        grid.addWidget(QLabel("Sirket Adi:"),0,4)
        self.companycode=QLineEdit()
        grid.addWidget(QLabel('Danone'),0,5)

        grid.addWidget(QLabel("Personel Adi:"),1,0)
        self.companycode=QLineEdit()
        grid.addWidget(QLabel(str(ad1)),1,1)
        grid.addWidget(QLabel("Personel Adi:"),1,2)
        self.companycode=QLineEdit() 
        grid.addWidget(QLabel(str(ad2)),1,3)
        grid.addWidget(QLabel("Personel Adi:"),1,4)
        self.companycode=QLineEdit()
        grid.addWidget(QLabel(str(ad3)),1,5)
#ikinci satÄ±r
        grid.addWidget(QLabel("Personel Mail:"),2,0)
        self.postingdate=QDateEdit()
        grid.addWidget(QLabel(str1),2,1)
        grid.addWidget(QLabel("Personel Mail:"),2,2)
        self.postingdate=QDateEdit()
        grid.addWidget(QLabel(str2),2,3)
        grid.addWidget(QLabel("Personel Mail:"),2,4)
        self.postingdate=QDateEdit()
        grid.addWidget(QLabel(str3),2,5)
#Ã¼Ã§Ã¼ncÃ¼ satÄ±r
        grid.addWidget(QLabel("Sikayet Sayisi"),3,0)
        self.journalentry=QDateEdit()
        grid.addWidget(QLabel(str(num)),3,1)
        grid.addWidget(QLabel("Sikayet Sayisi"),3,2)
        self.journalentry=QDateEdit()
        grid.addWidget(QLabel(str(num1)),3,3)
        grid.addWidget(QLabel("Sikayet Sayisi"),3,4)
        self.journalentry=QDateEdit()
        grid.addWidget(QLabel(str(num2)),3,5)
        
        grid.addWidget(QLabel("Personel Ekle"),6,0)
        self.yeni=QLineEdit()
        grid.addWidget(self.yeni,6,1)
        grid.addWidget(QLabel("Sirekt Ekle"),8,0)
        self.yeni=QLineEdit()
        grid.addWidget(self.yeni,8,1)
        grid.addWidget(QLabel("Personel Mail Ekle"),7,0)
        self.yeni=QLineEdit()
        grid.addWidget(self.yeni,7,1)
       
               
            
     
    
        #print(str5)
#dÃ¶rdÃ¼ncÃ¼ satÄ±r


       #submit butonu
        proposeitems=QPushButton("Submit")
       #proposeitems.clicked.connect(self."hesapla kullanmis")
        proposeitems.clicked.connect(self.find)
        grid.addWidget(proposeitems,9,7)
        self.setLayout(grid)
    
        def find(self):
          self.str5 = self.ui.lineEdit.text()
          print(self.str5)


           
           
data = {
    'Ad': pd.Series(['Selin','Pelin','Mehmet']),
    'Soyad': pd.Series(['Yýlmaz','Aslan','Mutlu']),
    'Ýlgilendiði Þirket': pd.Series(['Dalin','Flormar','Danone']),
    'Mail Adresi:':pd.Series(['seliny872@gmail.com','17hilalyldz@gmail.com','gamzes.kaya@gmail.com'])
}
df = pd.DataFrame(data)
print(df)

ufo = pd.read_csv('sikayet_var.csv')
ufo[ufo['marka'].isin(['Dalin'])]
print(ufo[ufo['marka'].isin(['Dalin'])])


ufo1 = pd.read_csv('sikayet_var.csv')
ufo1[ufo1['marka'].isin(['Flormar'])]
print(ufo1[ufo1['marka'].isin(['Flormar'])])

ufo2 = pd.read_csv('sikayet_var.csv')
ufo2[ufo2['marka'].isin(['Danone'])]
print(ufo2[ufo2['marka'].isin(['Danone'])])

'''ufo=pd.read_csv('sikayet_var.csv')
print(ufo.values)'''

'''data=pd.read_csv('a.csv')
x = data.retail_price
y = data.price
plt.bar(x, y)
plt.show()'''

'''data1=pd.read_csv('a.csv')
x=data1.units_sold
y=data1.rating
plt.plot(x,y)
plt.xlabel='satılan birim'
plt.ylablel='değerlendirme puanı'
plt.title='satılan birim/değerlendirme puanı oranları'
plt.show()'''


'''data=pd.read_csv('a.csv')
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes=[data.retail_price,data.price,data.rating]
plt.pie(data.retail_price,data.price,data.rating)
plt.show()'''


   
app=QApplication([])
pencere=Dialog()
pencere.setWindowTitle("Þikayet Takip")
pencere.show()
sys.exit(app.exec_())
