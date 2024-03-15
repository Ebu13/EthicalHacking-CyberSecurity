# Performans Kıyaslaması

## Algoritma 1

- lrt() fonksiyonu for döngüsü ile 1 den 100 milyona kadarki tüm pozitif tam sayıları sırası ile dönüp -1+2-3+4-5+6...-99999999+100000000 şeklindeki örüntünün cevabını yazdırıyor.
- ortolcum() fonksiyonundaki ``tekrar`` parametresi kadar lrt() fonksiyonunu çalıştırılıp lrt() fonksiyonunun ortalama çalışma süresini hesaplıyor. Ben tekrar sayısını 50 olmasını istedim. Siz daha fazla tekrar ile daha doğru bir sonuca ulaşabilirsiniz. Tabi ki de daha farklı sistemlerde daha yüksek ya da daha düşük değerler çıkabilir.
- İlk olarak PyCharm da, sonra windows cmd terminalinde ve en son olarak Kali linux da denedim. (Kali Linux da GUI kullanıyorum ve UI olmadan kullansaydım daha düşük değerler çıkardı.)

Sırası ile her python denemesindeki değerler:

- PyCharm on Microsoft Windows : 14.056747241020203
- Windows Version 10.0.19045.4170 Administrator Command Processor : 11.314760885238648
- Kali Linux with GNU : 7.2922810411453245
