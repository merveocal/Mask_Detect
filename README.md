#  Gerçek Zamanlı Maske Tespiti (Ağız Tabanlı)

Bu proje, **Python** ve **OpenCV** kullanılarak geliştirilen basit ve etkili bir **maske tespit sistemi**dir. Uygulama, kamera görüntüsünde insan yüzlerini tespit eder ve bu yüzlerde ağız tespitine göre kişinin maske takıp takmadığını belirler.

---

##  Özellikler

- 📷 Gerçek zamanlı kamera görüntüsü üzerinden:
  - Yüz tespiti
  - Ağız tespiti
  - Maske takılıysa: "Thank you" yeşil yazı ile
  - Maske takılı değilse: "Please wearing a mask" kırmızı yazı ile
- Tespit edilen yüz ve ağız bölgeleri kutucukla işaretlenir

---

##  Kullanılan Teknolojiler

- Python 
- OpenCV (cv2)
- Haar Cascade sınıflandırıcıları:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_mcs_mouth.xml`

---
