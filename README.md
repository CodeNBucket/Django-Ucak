Projeyi çalıştırmak için:
- git clone https://github.com/CodeNBucket/Django-Ucak.git
- cd Django-Ucak 
-- Docker kurulmalı
- docker-compose build
- docker-compose up
- docker-compose exec web python manage.py migrate
- docker-compose exec web python manage.py createsuperuser    -- Superuser takımları ve kullanıcıları oluşturmak için gerekli

Bunları yaptıktan sonra:
http://localhost:8000/user/login  -- Ana sayfaya gelebilirsiniz
http://localhost:8000/admin  -- Admin sayfasını açabilirsiniz

Kapatmak istediğinizde:
- docker-compose down
  

Proje Açıklaması:
Hava Aracı Üretim Uygulaması'nda iki farklı takım türü var, Üretim Takımları ve Montaj Takımı

Üretim Takımları -->Kanat Takımı, Gövde Takımı, Kuyruk Takımı, Aviyonik Takımı   
Bu takımların amaçları farklı uçaklar için (TB2, TB3, AKINCI, KIZILELMA) parçalar üretmek

Montaj Takımı --> Montaj Takımı
Montaj Takımının amacı üretilen parçaları birleştirip uçak yaratabilmek

Proje hem daha anlaşılır olsun diye hem de sonradan eklemelerin/güncellemelerin daha rahat olması bakımından bu ana öğeleri 5 farklı modele böldüm
Personel-Takım-Uçak-Parça-Montaj
İçerikleri resimler dosyasına eklediğim 'er_diyagramı'ndan görülebilir, kodu da ordaki ilişkileri baz alarak yazdım

İstenilen bütün fonksyonaliteler çalışıyor ve yine bunlar resimler dosyasından görülebilir

Personel ve takım eklemek için Superuser oluşturulması ve admin panelinden atamaların yapılması gerekiyor 
