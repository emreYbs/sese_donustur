# sese_donustur
**Verdiğiniz Türkçe metni, Türkçe olarak seslendirir ve mp3 olarak kaydeder.**

Bu basit uygulama ile kısa cümleleri seslendirip, mp3 olarak kaydedebilirsiniz. Türkçe için _Text to Speech_ kütüphaneleri eskisi kadar robotik değil. Günlük işler için iş görür. Ancak ben İngilizce için kullanıyorum ve dil öğrenenler, öğrenciler için o daha işlevsel olur. 
- **Tek yapmanız gereken**, benim yazdığım koddaki language='tr' kısmını *'en'* diye değiştirmek.Kendi repoma İngilizce için yazdığım versiyonu da yüklerim, ama zaten kod olarak da bu kısım hariç herşey aynı olur.

![image](https://user-images.githubusercontent.com/59505246/141120859-e6d67559-82a8-425f-b35b-41a7c1910620.png)


 **Uyarı:**
 - Uzun bir metin verirseniz bu kod hata verecektir. Yine Windows harici kullanınca, otomatik olarak kaydedilen mp3 çıktısı seslendirilmeyecektir; ki çok da önemli değil:)
 
 - Verdiğiniz metni, TTS kütüphanesi ile sese dönüştürüp mp3 dosyası olarak kaydettikten sonra, eğer sizin için önemli ise, o mp3 çıktısını saklayın başka bir klasöre kopyalayıp. Yoksa bu kodu her çalıştırdığınızda, mp3 dosyası üzerine tekrar yazar, ve önceki verdiğiniz metin silinir.
