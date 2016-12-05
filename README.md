# ExtractionMetadata
Extraction metadata online news with text detection framework

Step sesuai di Paper:

PREPROCESING

-List.py buat ngelist raw html nya

-list htmlnya aku panggil ke Cleantag.py buat ngilangin tag scrip,style,comment pke bs4 terus aku simpen di folder PreProcessing dengan nama file extracts001.html, extracts002.html dst

TEXT DETECTION

-List lagi html yang sudah bersih di ListCleanTag.py

-List html yang udah bersih aku panggil di TextDetection.py buat ngitung 

    #words_count(TC): jumlah kata didalam tag di tiap baris halaman html kecuali didalam tag <a>
    #link_words (LTC) : jumlah kata didalam tag <a> ditiap baris halamn html
    #number_tag_break(P) : jumlah tag P dan Br tiap baris
    #number_tag(TG) : jumlah semua tag tiap baris tagnya buka dan tutup diitung kepisah misal <p> </p> itu berarti ada 2
    #CTTD(CTTD) : words_count + (0.5 * link_words) + number_tag - number_tag_break

-Simpen file nya dalam bentuk csv di folder textdetection dengan nama file textdetection001.csv dst

SMOOTHING

-aku list textdetection001.csv nya di ListTD.py

-panggil listnya ke Smoothing.py buat menyemoothing nilai cttdnya terus filenya aku simpen di folder Smoothing dengan nama file Smoothing001.csv. nilai cttd yang udah di smoothing aku simpen dengan nama kolom CTTDs

FIND CANDIDATES

-nyari niai threshold cttd dari tiap halamn html

-aku list smoothing001.csv di ListSmoothing.py

-terus panggil ke Threshold.py *sebenernya aku mau nyimpen nilai thresholdnya langsung ke csv tiap htmlnya tapi aku ga bisa-bisa wkwkw makanya aku simpen satu-satu deh*

didalam threshold.py ngitung:

    #minval(Minimun CTTDs) : nilai cttd minimum (bukan 0) tiap html
    #maxval(MAximum CTTDs) : nilai cttd maximal tiap html
    #th_gap(Threshold_Gap) : nilai maximum TG di tiap html
    #th_cttd(Threshold_CTTD): minval + (k * (maxval - minval))



