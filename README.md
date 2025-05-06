# Otomata Week 11 Assignment 

### Nama Kelompok :
_____

| Nama                             | NRP        | Kelas     |
| -------------------------------- | ---------- | --------- |
| Alvin Zanua Putra                | 5025231064 | Otomata E |
| Pramudtya Faiz Ardiansyah        | 5025231108 | Otomata E |
| Christoforus Indra Bagus Pratama | 5025231124 | Otomata E |
| Muhammad Azhar Aziz              | 5025231131 | Otomata E |

# 🧠 CYK Algorithm Implementation in Python


Implementasi algoritma **Cocke–Younger–Kasami (CYK)** untuk memeriksa apakah sebuah string diterima oleh grammar berbentuk **Chomsky Normal Form (CNF)**. Program ini menerima file `.json` yang berisi grammar dan input string.

---

## 📚 Apa itu CYK Algorithm?

**CYK (Cocke–Younger–Kasami)** adalah algoritma parsing berbasis tabel (bottom-up parser) yang digunakan untuk grammar dalam bentuk **CNF (Chomsky Normal Form)**.

### 🔁 Cara Kerja:
1. Inisialisasi tabel segitiga berdasarkan input string.
2. Isi baris pertama tabel dengan non-terminal yang menghasilkan terminal input.
3. Bangun kombinasi non-terminal dari bawah ke atas berdasarkan produksi CNF.
4. String diterima jika simbol awal (`S`) muncul di sel kiri atas tabel akhir.

---

## 📦 Struktur File

```
cyk-project/
├── main.py                # Program utama CYK
├── CNF-ACCEPTED.json      # Grammar CNF, string diterima
├── CNF-REJECTED.json      # Grammar CNF, string ditolak
└── README.md              # Dokumentasi ini
```

---

## ▶️ Cara Menjalankan

### 💻 Clone repository :

```bash
git clone https://github.com/alvinzanuaputra/cyk-algorithm.git
cd cyk-algorithm
```

### 💻 Jalankan via terminal:
```bash
python cyk_algorithm.py <nama_file.json>
```

### 🔁 Contoh:
```bash
python cyk_algorithm.py CNF-ACCEPTED.json
```

---

## 📄 Format File JSON

```json
{
  "grammar": {
    "S": ["AB", "BC"],
    "A": ["BA", "a"],
    "B": ["CC", "b"],
    "C": ["AB", "a"]
  },
  "input": "baaba"
}
```

- `grammar`: dictionary di mana key adalah non-terminal, dan value adalah list produksi (2 simbol non-terminal atau 1 terminal saja untuk CNF).
- `input`: string yang akan dicek.

---

## ✅ Contoh Output

### CNF-ACCEPTED.json
```
String 'baaba' is ACCEPTED by the grammar.
```

### CNF-REJECTED.json
```
String 'bbbbb' is REJECTED by the grammar.
```

### Output :

```bash

ASUS TUF GAMING A15@ASUSTUF-ALVINZP MINGW64 ~/Desktop/KULIAH/Otomata/W11
$ ls
CNF-ACCEPTED.json  CNF-REJECTED.json  cyk_algorithm.py  README.md

ASUS TUF GAMING A15@ASUSTUF-ALVINZP MINGW64 ~/Desktop/KULIAH/Otomata/W11
$ python cyk_algorithm.py CNF-ACCEPTED.json
String 'baaba' is ACCEPTED by the grammar.

ASUS TUF GAMING A15@ASUSTUF-ALVINZP MINGW64 ~/Desktop/KULIAH/Otomata/W11
$ python cyk_algorithm.py CNF-REJECTED.json
String 'bbbbb' is REJECTED by the grammar.

ASUS TUF GAMING A15@ASUSTUF-ALVINZP MINGW64 ~/Desktop/KULIAH/Otomata/W11
$
```

⚠️ Catatan Penting
Algoritma CYK hanya dapat digunakan untuk grammar dalam bentuk CNF (Chomsky Normal Form).

Mengapa?
CYK adalah algoritma bottom-up parsing berbasis tabel yang dibangun dengan asumsi bahwa setiap produksi memiliki bentuk yang tetap dan terbatas, yaitu:
`A → BC (dua non-terminal)`
`A → a (satu terminal)`
Sementara itu, dalam grammar BNF (Backus-Naur Form), produksi bisa memiliki bentuk seperti:
`S → aSb | ε | A | a`
Produksi semacam ini bisa lebih panjang, mengandung campuran terminal dan non-terminal, bahkan epsilon (kosong). Struktur produksi yang tidak konsisten ini membuatnya sulit untuk diproses secara sistematis oleh algoritma CYK.# cyk-algorithm
