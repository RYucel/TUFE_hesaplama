# KKTC TÜFE Değişim Hesaplayıcısı

Bu web uygulaması, Kuzey Kıbrıs Türk Cumhuriyeti (KKTC) için Tüketici Fiyat Endeksi (TÜFE) değişimini hesaplamak ve belirli bir tarihteki Türk Lirası (TL) değerinin zaman içindeki değişimini göstermek için geliştirilmiştir.

## Nasıl Kullanılır?

Uygulamayı kullanmak için aşağıdaki adımları izleyin:

1.  **Başlangıç Tarihi Seçin:**
    *   "Başlangıç Tarihi" bölümünden, hesaplamaya başlamak istediğiniz ay ve yılı seçin. Ay için açılır menüden ayı, yıl için ise yıl açılır menüsünden yılı seçebilirsiniz.
2.  **Bitiş Tarihi Seçin:**
    *   "Bitiş Tarihi" bölümünden, hesaplamanın sona ermesini istediğiniz ay ve yılı seçin. Ay ve yıl seçimleri "Başlangıç Tarihi" seçimi ile aynı şekilde yapılır.
3.  **Lira Miktarını Girin (İsteğe Bağlı):**
    *   "Hesaplanacak Lira Miktarı" alanına, değer kaybını görmek istediğiniz TL miktarını girin. Varsayılan değer 100 TL'dir. İstediğiniz herhangi bir pozitif sayı girebilirsiniz.
4.  **"Hesapla" Düğmesine Tıklayın:**
    *   Tarihleri ve lira miktarını seçtikten sonra, "Hesapla" düğmesine tıklayarak hesaplamayı başlatın.

## Sonuçlar

Hesaplama tamamlandıktan sonra, sonuçlar ekranın altında görüntülenecektir. Sonuçlar aşağıdaki bilgileri içerir:

*   **TÜFE Değişimi:** Seçilen başlangıç ve bitiş tarihleri arasındaki toplam TÜFE değişim yüzdesini gösterir. Bu değer, enflasyonun seçilen dönemdeki artışını veya azalışını ifade eder.
*   **[Girilen Miktar] TL Değer Kaybı:** Başlangıç tarihindeki [Girilen Miktar] TL'nin, bitiş tarihindeki değerini gösterir. Bu, paranın enflasyon nedeniyle zaman içinde nasıl değer kaybettiğini veya kazandığını görselleştirmenize yardımcı olur. Örneğin, 100 TL girdiyseniz, sonuç "100 TL'nin [Başlangıç Tarihi] Tarihindeki Değeri, [Bitiş Tarihi] Tarihinde: [Değer] TL" şeklinde olacaktır.
*   **Açıklayıcı Cümle:** Sonuçların altında, "[Girilen Miktar] TL'nin [Başlangıç Tarihi] tarihindeki değeri, [Bitiş Tarihi] tarihinde [Değer] TL'ye eşdeğerdir." şeklinde bir açıklama cümlesi yer alır. Bu cümle, sonuçları daha kolay anlamanıza yardımcı olur.

## Veri Kaynağı

Bu uygulama, Ocak 1978'den Aralık 2024'e kadar olan aylık TÜFE verilerini kullanmaktadır. Veri kaynağı [Veri Kaynağının Adı veya Kaynağa Bağlantı (Eğer varsa ekleyin, örneğin KKTC Devlet İstatistik Enstitüsü veya benzeri bir kurum)].

## Teknolojiler

Bu web uygulaması aşağıdaki teknolojiler kullanılarak geliştirilmiştir:

*   **Frontend:** HTML, CSS, Bootstrap (Modern ve şık tasarım için)
*   **Backend:** Python, Flask (Web uygulaması çerçevesi)
*   **Veri İşleme:** pandas (Veri analizi ve manipülasyonu için)

## Katkıda Bulunma

Bu proje açık kaynaklıdır ve katkılarınızı memnuniyetle karşılar. Katkıda bulunmak için lütfen [Katkıda Bulunma Talimatları veya Proje Reposuna Bağlantı (Eğer varsa ekleyin)] bölümüne bakın.

## Lisans

[Proje Lisansı (MIT Lisansı)]
