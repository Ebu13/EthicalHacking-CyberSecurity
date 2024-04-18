# Kurulumdan Öncekiler

Benim 480 GB SDD olduğu için aynı laptop üzerine windows 10 ve Kali linux u kullanma kararı verdim.
VirtualBox da iyi bir seçimdi ama kaynakları daha iyi kullanmak ve performanslı olmak adına bu yolu 
tercih ettim.

İlk olarak W10 yükleyidim kurulumları tamamladım. Normal bir windows kullanıcısı olan bir yazılımcının
yapacağı herşeyi yaptım.

## Adım 1: Disk Bölme

1. Windows+R tuşlarına basarak "Çalıştır" penceresini açtım.
2. "compmgmt.msc" komutunu kullanarak Disk Yöneticisi'ne girdim.
3. Ayırmak istediğim sürücü parçasını seçerek birimi küçült dedim. 120 GB'lık bir alanı ayırdıktan sonra ayrılmamış alan olarak bıraktım.

# Kurulum Esnası

https://www.youtube.com/watch?v=AIZvEYkT_ts adresindeki kurulum videosunda denilen adımları takip ettim.

Rufus ile Kali Linux u Flash Belleğe kurduktan sonra videodaki gibi yaptım. Ama farklı olarak 

Guided - use the largest continuous free space

seçimini seçtim.

# Yaşadığım sıkıntılar

Secure boot enabled olduğu için flash ımı çalıştırmıyordu. Ben de disabled yaptım. Eğer EFI dosyasını bulamazsa
disabled yapıp denemenizi öneririm.

BIOS a erişememe sorunum oldu.Hızlıca başlatıp BIOS girmek için gereken tuşa basmanızda engel oluşuyorsa Güç ve uyku ayarlarına gidin. Ek güç ayarlarına gidin.Güç düğmelerinin yapacaklarını seçin e gidin. Kapatma ayarlarından şu anda kullanılmayan ayarları değiştir e tıkla ve hızlı başlatmayı kapatın.

