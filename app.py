from flask import Flask, request, url_for, render_template
from zeep import Client
import base64

app = Flask(__name__)

def toBraille(url):
    client = Client('http://www.webservicex.net/whois.asmx?WSDL')
    result = client.service.GetWhoIS(url)
    client = Client('http://www.webservicex.net/braille.asmx?WSDL')
    result = client.service.BrailleText(result, 12)
    return result

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        braille = base64.b64encode(toBraille(url))
        return render_template('index.html', braille=braille.decode('utf-8'))
    else:
        return render_template('index.html', braille='')

if __name__ == '__main__':
    app.run(debug=True)
