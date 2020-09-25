from flask import Flask
from zeep import Client, helpers
from zeep.transports import Transport
from soap_retry import CalculatorRetry

app = Flask(__name__)

class ConnectWSDL():
    def __init__(self):
        self.service        = CalculatorRetry()
        self.session        = self.service.requests_retry_session(method_whitelist=False)
        self.transport      = Transport(session=self.session, timeout=30, operation_timeout=30)
        self.client         = Client(wsdl=self.service.soap_sv, transport=self.transport)
    
    def suma(self, data):
        status              = True
        res                 = self.client.service.Add(data['valor1'], data['valor2'])
        
        # casting zeep objecto to python dictionary
        pyd                 = helpers.serialize_object(res)
        return pyd

@app.route('/')
def index():
    sv                      = ConnectWSDL()
    resultado               = sv.suma(data={'valor1': 50, 'valor2': 100})
    return str(resultado)

if __name__ == '__main__':
    app.run()