import requests
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
from .util import format_string


class Cardapio:

    BASE_URL = "https://www.prefeitura.unicamp.br/apps/site/cardapio.php?d="

    def __init__(self, days_delta=0, hours_delta=0, date=None):
        date = date or (datetime.today() + timedelta(days=days_delta, hours=hours_delta)).strftime('%Y-%m-%d')
        try:
            response = requests.get(self.BASE_URL + date, timeout=3)
            response.raise_for_status()
            if response.text.find("Não existe cardápio") >= 0:
                raise LookupError("Não existe cardápio")
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.Timeout:
            self.soup = "_O servidor da Unicamp demorou demais para responder._\n_Tente novamente mais tarde._"
            raise requests.exceptions.Timeout("O servidor da Unicamp demorou demais para responder. Tente novamente mais tarde.")
        except requests.HTTPError:
            self.soup = "_O servidor da Unicamp está sendo malcriado._"
            raise requests.HTTPError("O servidor da Unicamp está sendo malcriado.")
        except LookupError:
            self.soup = "*Esse cardápio não existe.*\n_Será que não tem bandeco?_"
            raise LookupError("Esse cardápio não existe. Será que não tem bandeco?")
        except requests.exceptions.ConnectionError:
            self.soup = "_Não foi possível estabelecer uma conexão com o servidor da Unicamp._"
            raise requests.exceptions.ConnectionError("Não foi possível estabelecer uma conexão com o servidor da Unicamp.")
        except Exception as e:
            self.soup = "_Algo bem errado aconteceu:_\n\n" + str(type(e).__name__)
            raise e("Algo bem errado aconteceu")

    @property
    def breakfast(self):
        if type(self.soup) is str:
            return self.soup
        raw = self.soup.find_all("div", {"class": "fundo_cardapio"})
        return '\n'.join(format_string(raw)).strip()

    @property
    def lunch(self):
        if type(self.soup) is str:
            return self.soup
        raw = self.soup.find_all("table", {"class": "fundo_cardapio"})[0].find_all("td")
        return '\n'.join(format_string(raw)).strip()

    @property
    def veglunch(self):
        if type(self.soup) is str:
            return self.soup
        raw = self.soup.find_all("table", {"class": "fundo_cardapio"})[1].find_all("td")
        return '\n'.join(format_string(raw)).strip()

    @property
    def dinner(self):
        if type(self.soup) is str:
            return self.soup
        raw = self.soup.find_all("table", {"class": "fundo_cardapio"})[2].find_all("td")
        return '\n'.join(format_string(raw)).strip()

    @property
    def vegdinner(self):
        if type(self.soup) is str:
            return self.soup
        raw = self.soup.find_all("table", {"class": "fundo_cardapio"})[3].find_all("td")
        return '\n'.join(format_string(raw)).strip()
