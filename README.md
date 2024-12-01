# Spinning donut in python

Program Python sederhana untuk membuat animasi donat berputar di terminal menggunakan karakter ASCII. Proyek ini mendemonstrasikan penggunaan matematika dan rendering terminal untuk mensimulasikan objek 3D yang berputar.

---

## Cara Kerja

### 1. Persamaan Torus
Donat (torus) didefinisikan oleh dua radius:
- **Radius Dalam (R1)**: Radius lingkaran penampang.
- **Radius Luar (R2)**: Radius lintasan lingkaran besar.

### 2. Rotasi 3D
Donat diputar pada dua sumbu menggunakan transformasi trigonometri:
- **Sudut A**: Rotasi pada sumbu Y.
- **Sudut B**: Rotasi pada sumbu Z.

### 3. Proyeksi
Koordinat 3D dari donat diproyeksikan ke bidang 2D (layar terminal) menggunakan formula proyeksi perspektif.

### 4. Rendering ASCII
Intensitas cahaya dari setiap titik direpresentasikan menggunakan karakter dari set berikut:

