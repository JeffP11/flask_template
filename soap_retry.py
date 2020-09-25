from requests.adapters import HTTPAdapter, Retry
import requests

class CalculatorRetry():
    def __init__(self):
        self.soap_sv    = "http://www.dneonline.com/calculator.asmx?WSDL"

    def requests_retry_session(
        self,
        retries             = 5,
        backoff_factor      = 0.3,
        status_forcelist    = (500, 502, 503, 504),
        session             = None, **kwargs) -> requests.Session:
        
        session             = session or requests.Session()
        retry               = Retry(
        total               = retries,
        read                = retries,
        connect             = retries,
        backoff_factor      = backoff_factor,
        status_forcelist    = status_forcelist,
        **kwargs
        )

        adapter             = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session