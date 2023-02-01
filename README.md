
# DataPiratesChallenge
Solução do DataPiratesChallenge - Neoway

# Objetivo
Essa aplicação recupera faixas de códigos postais ("faixa de CEP") para até 100 localidades em quaisquer 2 estados do Brasil. Os dados são lidos no [site dos correios](http://www.buscacep.correios.com.br/sistemas/buscacep/ResultadoBuscaFaixaCEP.cfm).

# Como usar?
Clone o repositório e execute `make build run STATES="STATE1 STATE2 STATE3 ..."` no diretório `DataPiratesChallenge`. ESTADOS são variáveis opcionais que mapeiam para estados brasileiros específicos (entradas com 2 letras maiúsculas são válidas). Se nenhum STATE for fornecido, os valores padrão serão `CE` e `DF`. Se um estado inválido for fornecido, o aplicativo não será sexecutado.

De modo alternativo, você pode criar seu próprio virtualenv com `virtualenv venv -p python` (certifique-se de usar python 3.8), instale as dependências necessárias com `pip install -r requirements.txt` e execute o aplicativo com `python ./src/buscaCep.py STATE1 STATE2 ...` (isso exigirá que você passe pelo menos um argumento).

# Saída
Os arquivos são gravados como `jsonlines` na pasta `out`, cada linha correspondendo a um intervalo de códigos postais. Cada elemento possui três atributos: id (`id`), localização (`localidade`) e faixa de código postal (`faixa de CEP`).