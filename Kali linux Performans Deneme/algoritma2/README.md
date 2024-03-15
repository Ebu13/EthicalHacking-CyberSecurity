# Performans Kıyaslaması

## Algoritma 2

- matrix_printer() fonksiyonu rastgele 100x100 lük bir matris oluşturur. Sonra da her bir elemanın karesini alır. Sonrasında da her sütunun toplamını alır ve ekrana en büyük değeri yazdırır.
- ortolcum() fonksiyonundaki ``tekrar`` parametresi kadar lrt() fonksiyonunu çalıştırılıp lrt() fonksiyonunun ortalama çalışma süresini hesaplıyor. Ben tekrar sayısını 50 olmasını istedim. Siz daha fazla tekrar ile daha doğru bir sonuca ulaşabilirsiniz. Tabi ki de daha farklı sistemlerde daha yüksek ya da daha düşük değerler çıkabilir.
- İlk olarak PyCharm da, sonra windows cmd terminalinde ve en son olarak Kali linux da denedim. (Kali Linux da GUI kullanıyorum ve UI olmadan kullansaydım daha düşük değerler çıkardı.)

Sırası ile her python denemesindeki değerler:

- PyCharm on Microsoft Windows : 0.18274078369140626
- Windows Version 10.0.19045.4170 Administrator Command Processor with venv : 0.6815551233291626
- Kali Linux with GNU : 0.19978536128997804
