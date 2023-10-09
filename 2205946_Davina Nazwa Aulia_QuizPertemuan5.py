<!DOCTYPE html>
<html>
<head>
    <title>Davina Nazwa Aulia (2205946)</title>
    <style>
    body {
        font-family: Arial, Helvetica, sans-serif;
    }

    * {
        box-sizing: border-box;
    }

    input[type=text], select, textarea {
        width: 100%;
        padding: 12px;
        border: 1px solid #ccc;
        border-radius: 4px;
        resize: vertical;
    }

    label {
        padding: 12px 12px 12px 0;
        display: inline-block;
    }

    input[type=submit] {
        background-color: #aa7804;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        float: right;
    }

    input[type=submit]:hover {
        background-color: #aa7804;
    }

    .container {
        border-radius: 5px;
        background-color: #f2f2f2;
        padding: 20px;
    }

    .col-25 {
        float: left;
        width: 25%;
        margin-top: 6px;
    }

    .col-75 {
        float: left;
        width: 75%;
        margin-top: 6px;
    }

    /* Clear floats after the columns */
    .row::after {
        content: "";
        display: table;
        clear: both;
    }

    /* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
    @media screen and (max-width: 600px) {
    .col-25, .col-75, input[type=submit] {
        width: 100%;
        margin-top: 0;
    }
    }
    </style>
    <script>
    function tampilHasil()
    {
        // Mendapatkan nilai dari input dan pilihan
        var nama = document.getElementById("nama").value;
        var alamatPemesan = document.getElementById("alamatPemesan").value;
        var jenisKopi = document.getElementById("jenisKopi").value;
        var ukuran = document.querySelector('input[name="ukuran"]:checked').value;
        var makananPelengkap = [];
        var checkboxes = document.querySelectorAll('input[name="makananPelengkap"]:checked');
        for (var i = 0; i < checkboxes.length; i++) {
            makananPelengkap.push(checkboxes[i].value);
        }

        // Harga Kopi
        var hargaKopi = 0;
        if (jenisKopi === "kopiarabika") {
            hargaKopi = 10000;
        } else if (jenisKopi === "kopirobusta") {
            hargaKopi = 15000;
        } else if (jenisKopi === "kopiliberika") {
            hargaKopi = 20000;
        } else if (jenisKopi === "kopiekselsa") {
            hargaKopi = 25000;
        }

        // Harga Makanan Pelengkap
        var hargaMakananPelengkap = 0;
        for (var j = 0; j < makananPelengkap.length; j++) {
            if (makananPelengkap[j] === "Cake") {
                hargaMakananPelengkap += 5000;
            } else if (makananPelengkap[j] === "Brownies") {
                hargaMakananPelengkap += 10000;
            } else if (makananPelengkap[j] === "Dalgona Candy") {
                hargaMakananPelengkap += 15000;
            }
        }

        // Menghitung total harga
        var totalHarga = hargaKopi + hargaMakananPelengkap;

        // Menampilkan hasil
        var hasilText = "Nama : " + nama + "<br>";
        hasilText += "Alamat : " + alamatPemesan + "<br>";
        hasilText += "Pesanan Jenis Kopi : " + jenisKopi + "<br>";
        hasilText += "Ukuran : " + ukuran + "<br>";
        hasilText += "Total : " + totalHarga + makananPelengkap;

        document.getElementById("hasil").innerHTML = hasilText;
    }
    </script>
</head>
<body>

<h2>Form Pemesanan Coffee</h2>

<div class="container">
  <form>
  <div class="row">
    <div class="col-25">
      <label for="nama">Nama Lengkap Pemesan</label>
    </div>
    <div class="col-75">
      <input type="text" id="nama" name="nama" placeholder="Masukan Nama Anda ...">
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="jenisKopi">Pilih Jenis Kopi</label>
    </div>
    <div class="col-75">
      <select id="jenisKopi" name="jenisKopi">
        <option value="kopiarabika">Kopi Arabika</option>
        <option value="kopirobusta">Kopi Robusta</option>
        <option value="kopiliberika">Kopi Liberika</option>
        <option value="kopiekselsa">Kopi Ekselsa</option>
      </select>
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="alamatPemesan">Alamat Pemesan</label>
    </div>
    <div class="col-75">
      <textarea id="alamatPemesan" name="alamatPemesan" placeholder="Alamat Pemesan.." style="height:200px"></textarea>
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="ukuran">Ukuran</label>
    </div>
    <div class="col-75">
        <input type="radio" id="ukuranS" name="ukuran" value="Small">
        <label for="ukuranS"> Small</label><br>
        <input type="radio" id="ukuranM" name="ukuran" value="Medium">
        <label for="ukuranM"> Medium</label><br>
        <input type="radio" id="ukuranL" name="ukuran" value="Large">
        <label for="ukuranL"> Large</label>
    </div>
  </div>
  <div class="row">
    <div class="col-25">
      <label for="makananPelengkap">Makanan Pelengkap</label>
    </div>
    <div class="col-25">
        <input type="checkbox" id="makananPelengkap1" name="makananPelengkap" value="Cake">
        <label for="makananPelengkap1"> Cake</label><br>
        <input type="checkbox" id="makananPelengkap2" name="makananPelengkap" value="Brownies">
        <label for="makananPelengkap2"> Brownies</label><br>
        <input type="checkbox" id="makananPelengkap3" name="makananPelengkap" value="Dalgona Candy">
        <label for="makananPelengkap3"> Dalgona Candy</label>
    </div>
  </div>
  <br>
  <div class="row">
    <input type="button" onClick="tampilHasil()" value="Simpan">
  </div>
  </form>
</div>

<div class="row">
    <div class="col-100">
      <p id="hasil" name="hasil"></p>
    </div>
  </div>

</body>
</html>
