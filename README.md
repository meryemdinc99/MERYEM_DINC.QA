# optional python3 -m venv ./venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 -m pytest -v


İçindekiler
1.Proje Özeti
2.Amaç
3.Önkoşullar (Nereye kurduk?)
4.Kurulum — Aşama Aşama
5.Dizin Yapısı (Nereye koydum?)
6.Test Süreçleri ve Aşamalar(Gerçekleşti/Gerçekleşmedi)
7.Testleri Çalıştırma (Komutlar ve Örnek Çıktılar)
8.Sonuçlar ve Raporlama
9.İletişim 

1.Proje Özeti
MERYEM_DINC.QA, Insider web sitesinin kariyer sayfası test otomasyonu için geliştirilmiş bir Selenium–Pytest tabanlı QA projesidir.
Proje, manuel test sürecinde yapılan kontrolleri otomatikleştirerek regresyon testlerini hızlandırmak ve hata yakalama oranını artırmayı amaçlar.

2.Amaç
-Insider kariyer akışını uçtan uca test etmek,
-“Careers” → “QA Jobs” yolunu doğrulamak,
-Pozisyon filtreleme adımlarını kontrol etmek

3.Önkoşullar (Nereye kurduk?)
Proje, macOS ortamında aşağıdaki sürümlerle çalıştırıldı.
-Python	3.9.6
-Selenium	4.x
-Pytest	8.x
-pytest-html	Raporlama için
-Tarayıcı	Google Chrome (güncel)
-IDE	VS Code

4.Kurulum — Aşama Aşama
4.a. Proje bağımlılıklarını izole etmek için venv adlı sanal ortam oluşturuldu.
python3 -m venv venv

4.b.Python komutlarının proje ortamındaki kütüphaneleri kullanması için Terminal (venv) etiketiyle başlar.
source venv/bin/activate

4.c.Projedeki tüm bağımlılıkları tek komutla yüklemek için Selenium, Pytest ve raporlama eklentileri kuruldu.
pip install -r requirements.txt

4.d.Pytest’in doğru şekilde kurulduğunu teyit edildi.
pytest --version

5.Dizin Yapısı (Nereye koydum?)

Automation_Test/
-pages/                 # (POM) yapısı  
--base_page.py         
--home_page.py          # Ana sayfa elementleri
--careers_page.py       # Kariyer sayfası işlemleri (navigasyon)
--qa_jobs_page.py       # QA sayfasındaki iş ilanı filtreleri

-tests/
--test_career_page.py   # Test senaryosu (Insider Career Flow)

-utils/
--driver_factory.py     # Testlerde kullanılacak olan WebDriver Chrome başlatmak, ayarlamak ve yönetmek
--screenshot_helper.py  # Test başarısız olduğunda ekran görüntüsü almak ve kaydetmek

-conftest.py            # Pytest’in test başlatma, bitirme işlemlerini yönetmesi için fixture’ları tanımlayan özel dosya
-pytest.ini             # Testlerin nasıl çalışacağını, hangi dosyaların test olarak tanımlanacağını, raporlama detaylarını belirler
-requirements.txt       # Proje için gerekli tüm kütüphanelerin sürümleriyle birlikte listelendiği dosya

6.Test Süreçleri ve Aşamalar(Gerçekleşti/Gerçekleşmedi)

    Aşama	                            Açıklama                                          Durum	
6.a. Ana sayfa yüklenmesi	          Sayfa başarıyla açıldı, başlık doğrulandı.         Gerçekleştirildi
6.b. Careers yönlendirmesi     	    “careers” içeren URL başarıyla tespit edildi.      Gerçekleştirildi
6.c. QA sayfası geçişi	            Element zamanında bulunamadı (TimeoutException).   Gerçekleştirilemedi
6.d. Rapor oluşturma	              HTML raporu başarıyla üretildi.                    Gerçekleştirildi
6.e. Screenshot alma	        	    Hata anında screenshot alındı.                     Gerçekleştirildi

Hata Detayı:Yani Selenium, CareersPage.go_to_qa_page() fonksiyonunda tanımlı olan QA_PAGE elementini belirtilen süre içinde bulamadı veya tıklayamadı.

Exception: Failed to click QA page link: Message:
selenium.common.exceptions.TimeoutException

Bu hatanın muhtemel nedenleri:
-Sayfa yüklenmeden tıklama denendi — WebDriverWait süresi yeterli olmayabilir.
-Element görünür durumda değil — tıklanabilir hale gelmeden bekleme bitti.

Proje bu durumda otomatik olarak ekran görüntüsü alıp screenshots/ klasörüne kaydeder böylece görsel olarak incelenebilir:
screenshots/qa_page_error_YYYYMMDD_HHMMSS.png

7.Testleri Çalıştırma (Komutlar ve Örnek Çıktılar)
-Tüm testleri çalıştırmak için
pytest -v

-HTML raporu üretmek için
pytest -v --html=report.html --self-contained-html

8.Sonuçlar ve Raporlama
Test sonucu:
FAILED tests/test_career_page.py::test_insider_career_flow
E   Exception: Failed to click QA page link: Message: TimeoutException

-Bu hata, CareersPage üzerinde bulunan QA linkinin tıklanabilir hale gelmemesi nedeniyle oluşmuştur.
Yani test senaryosu, “Careers sayfasından QA Jobs sayfasına yönlendirme” adımında element bulunamadığı için başarısız olmuştur.

9.İletişim 
Meryem DİNÇ
mry317dnc@gmail.com






