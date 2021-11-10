#! /usr/bin/python
#EmreYbs

#Eksik kütüphanelerinizi bu şekilde yükleyebilirsiniz: pip install cprint

from gtts import gTTS
import os
from halo import Halo
import time
from cprint import *

cprint.ok("\n\tSese Dönüştür uygulamasına hoş geldiniz")

banner = """
    


 ____                    ____                        _              
/ ___|  ___  ___  ___   |  _ \  ___  _ __  _   _ ___| |_ _   _ _ __ 
\___ \ / _ \/ __|/ _ \  | | | |/ _ \| '_ \| | | / __| __| | | | '__|
 ___) |  __/\__ \  __/  | |_| | (_) | | | | |_| \__ \ |_| |_| | |   
|____/ \___||___/\___|  |____/ \___/|_| |_|\__,_|___/\__|\__,_|_|   by EmreYbs

    
    """
cprint (banner)
cprint.info("'Sese Dönüştür' uygulaması hakkında: ")
cprint.warn(" Sizin vereceğiniz cümle ya da metni, sesli okuma teknolojisi ile mp3 olarak kaydeder")



spinner = Halo(text="Verdiginiz metni, seslendirip mp3 olarak kaydedecegim.\n",spinner="dots",color="cyan", text_color="red")
spinner.info("Dil öntanımlı olarak: Türkçe'dir.")
spinner.start()
time.sleep(4)
spinner.stop()


myText= input("\nSeslendirmem için bir cümle ya da metin giriniz :\n\n")
language = 'tr' # Eğer İngilizce olarak seslendirmesini isterseniz de "en" yapın. İngilizce de TTS kütüphaneleri daha iyi sonuç veriyor. 
#Ancak ben, kendi ülkemin insanlarının da işine yarasın diye bu basit kodu yazdım. İngilizcesi, öğrencilerin, dil öğrenenlerin daha çok işine yarar.
output = gTTS(text = myText, lang = language, slow = False) #Eğer slow=True yaparsanız da kaplumbağa gibi yavaş okur ki önermem:)
output.save("sese_donustu.mp3") #Bu mp3 çıktısını saklayın. Yoksa yeni bir denemede, üzerine yazar.
os.system("start sese_donustu.mp3") #Windows OS için


spinner.start()
spinner.info("Metinden sese dönüştürme işlemi başladı")
spinner.info("mp3 ses dosyası olarak kaydediyorum... ")
spinner.succeed("İşlem tamamdır.")
spinner.succeed("Başarılı şekilde dönüştürüldü ve kaydedildi.")
spinner.info("Verdiğiniz metin mp3 olarak otomatikman seslendirilecek.")
time.sleep(2)
spinner.warn("Eğer otomatik seslendirme başarısız olmuşsa, aynı klasör altında mp3 dosyası olarak, kendiniz de bulabilirsiniz.")
#os.system("start sese_donustu.mp3") #Bazı işletim sistemlerinde hata verebilir ve otomatik başlatmayabilir.
# Windows kullanıyorsanız, sorun yaşamamanız gerekir. Linux'ta ise otomatik başlamayacak ve basit bir hata verecektir.
spinner.fail("Otomatik başlamama Nedeni: Farklı işletim sistemi kaynaklı ya da tanımlı uygulama olmayabilir...")
spinner.stop()


cprint.ok("\nVerdiğiniz cümle/metin dönüştürüldü : \n\n",myText)
cprint.info("\nBeni kullandığınız için teşekkürler. Umarım faydalı olmuşumdur\n ")
