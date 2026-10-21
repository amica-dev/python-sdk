# Prezzo

Prezzo di listino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**listino_id** | **int** | Identificativo univoco di &#x60;Listino&#x60;. | [optional] 
**articolo_id** | **int** | Identificativo univoco di &#x60;Articolo&#x60;. In alternativa, usare &#x60;PrestazioneId&#x60;. | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**prestazione_id** | **int** | Identificativo univoco di &#x60;Prestazione&#x60;. In alternativa, usare &#x60;ArticoloId&#x60;. | [optional] 
**prestazione** | [**Prestazione**](Prestazione.md) |  | [optional] 
**importo** | **float** | Importo (prezzo). | [optional] 
**sconto1** | **float** | Primo sconto percentuale, applicato sul prezzo del bene o della prestazione. Il valore è una frazione: &#x60;0.10&#x60; corrisponde al 10%. | [optional] 
**sconto2** | **float** | Secondo sconto percentuale, applicato a seguito dell&#39;applicazione di &#x60;Sconto1&#x60; Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto3** | **float** | Terzo sconto percentuale, applicato a seguito dell&#39;applicazione di &#x60;Sconto2&#x60; Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**sconto4** | **float** | Quarto sconto percentuale, applicato a seguito dell&#39;applicazione di &#x60;Sconto3&#x60; Il valore è una frazione: &#x60;0.05&#x60; corrisponde al 5%. | [optional] 
**ricarico** | **float** | Ricarico (percentuale) da applicare sul costo del prodotto (o della prestazione). Se utilizzato, &#x60;Importo&#x60; viene ignorato. | [optional] 
**provvigione_agente** | **float** | Provvigione corrisposta all&#39;agente, in percentuale. | [optional] 
**provvigione_capo_area** | **float** | Provvigione corrisposta al capo area, in percentuale. | [optional] 

## Example

```python
from amica_python_sdk.models.prezzo import Prezzo

# TODO update the JSON string below
json = "{}"
# create an instance of Prezzo from a JSON string
prezzo_instance = Prezzo.from_json(json)
# print the JSON string representation of the object
print(Prezzo.to_json())

# convert the object into a dict
prezzo_dict = prezzo_instance.to_dict()
# create an instance of Prezzo from a dict
prezzo_from_dict = Prezzo.from_dict(prezzo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


