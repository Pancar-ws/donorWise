from flask import Flask, render_template, request
from pakarLogic import evaluasi_pakar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pakar', methods=['GET', 'POST'])
def pakar():
    hasil = None
    if request.method == 'POST':
        usia = int(request.form.get('usia', 0))
        bb = int(request.form.get('bb', 0))
        jeda = request.form.get('jeda', "")
        
        demam = 'demam' in request.form
        penyakit_berat = 'penyakit_berat' in request.form
        obat = 'obat' in request.form
        hamil = 'hamil' in request.form
        haid = 'haid' in request.form
        tato_tindik = 'tato_tindik' in request.form
        vaksin = 'vaksin' in request.form
        
        hasil = evaluasi_pakar(usia, bb, jeda, demam, penyakit_berat, obat, hamil, haid, tato_tindik, vaksin)
        
    return render_template('pakar.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True, port=8080)