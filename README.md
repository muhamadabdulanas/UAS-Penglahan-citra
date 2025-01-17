# UAS-Penglahan-citra

### Muhamad Abdul Anas
### 312210269
### TI.22.A2

## Paper
### klilk:[Paper Citra.pdf](https://github.com/user-attachments/files/16117761/Paper.Citra.pdf)


# App K-Means Clutering Segmentasi Gambar

## Imports: Mengimpor library yang diperlukan seperti streamlit, numpy, cv2 (OpenCV), Image (dari PIL), dan matplotlib untuk plotting.
#### Pertama, gambar dibaca menggunakan OpenCV dan kemudian dikonversi dari format BGR (default OpenCV) ke RGB untuk keperluan visualisasi yang lebih tepat di matplotlib.

### import matplotlib.pyplot as plt
### import cv2
### %matplotlib inline

## Mengubah Warna Gambar
![Screenshot (50)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/24a09770-c2fd-44d4-8cb1-67df8b4e89e9)


## Membentuk ulang gambar menjadi susunan piksel 2D dengan 3 nilai warna (RGB)
![Screenshot (51)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/a3def2cf-41a6-44b3-9c72-ba57101c7886)


## Mengonvresi ke tipe Float
![Screenshot (52)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/7da454d3-6e89-4c00-a7d3-c7dde02295dd)


## Melakukan k-means clustering dengan jumlah cluster yang ditetapkan
### retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

## Mengonversi data menjadi nilai 8-bit
![Screenshot (53)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/b2084187-108d-426e-ab17-8854472c4380)

## Scirpt Code APK cluster

![Screenshot (54)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/6aa6945f-d02c-43bc-b170-725d3cddb3d6)

![Screenshot (55)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/fdffb4c4-bc86-4411-979d-8a6f5fb10223)


# Hasil

![Screenshot (57)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/d5d5203f-09e2-4051-a257-aad71b08e586)

![Screenshot (56)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/c64b3164-7018-4e9b-898c-892b321585c5)

![Screenshot (58)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/514d0abc-12a9-4cfe-be84-7ea690af4ee2)

![Screenshot (59)](https://github.com/muhamadabdulanas/UAS-Penglahan-citra/assets/115569493/544a3375-97e6-4ab4-b92d-a3fe1a265633)









