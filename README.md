# Mesaj-Botu
CustomTkinter arayüzü ile desteklenmiş, güvenli ve thread-tabanlı bir otomatik mesaj gönderme aracıdır. Özellikle tekrarlayan metin girişleri ve otomasyon testleri için optimize edilmiştir.

## ✨ Özellikler

* **Güvenli Başlatma:** "Başlat" komutundan sonra kullanıcıya hazırlık süresi tanıyan 3 saniyelik geri sayım.
* **Threaded Mimari:** Gönderim işlemi sırasında GUI (arayüz) donmaz, kullanıcı etkileşimi kesilmez.
* **Dinamik Gecikme:** Mesajlar arası bekleme süresi kullanıcı tarafından belirlenebilir (Örn: 0.5s).
* **Modern Tasarım:** `CustomTkinter` ile Dark Mode uyumlu, minimalist buton ve form yapısı.
* **Anlık Durum Takibi:** Renk kodlu (Yeşil: Çalışıyor, Turuncu: Geri sayım, Kırmızı: Durduruldu) durum etiketi.

## 🛠️ Kurulum

Gerekli kütüphaneleri hızlıca kurun:

```
pip install customtkinter pyautogui keyboard
```

## 🚀 Kullanım

1. **Mesaj:** Gönderilmesini istediğiniz metni girin.
2. **Gecikme:** Saniye cinsinden hızı belirleyin.
3. **Başlat:** Butona basın ve 3 saniye içinde hedef pencereyi (WhatsApp Web, Discord, Not Defteri vb.) seçin.
4. **Durdur:** İstediğiniz an işlemi güvenli bir şekilde sonlandırın.
