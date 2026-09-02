# ContoContabile

Conto contabile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**banca_id** | **int** | Identificativo univoco di &#x60;Banca&#x60;. | [optional] 
**sezione** | **str** | Sezione di bilancio. | [optional] 
**tipo** | **str** | Tipo di conto. | [optional] 
**raw** | **str** | Numero di conto, in formato grezzo. Sono supportati fino a cinque livelli, ciascuno espresso da un massimo di cinque caratteri allineati a destra e riempiti con spazi, ad es. \&quot;  100   20\&quot; (dieci caratteri in totale) esprime \&quot;100.20\&quot;. | [optional] 
**sottoconto** | **str** | Ultimo quintetto del numero di conto (sottoconto). Per \&quot;100.20\&quot;, il valore sarebbe \&quot;20\&quot;. | [optional] 
**descrizione** | **str** | Descrizione. | [optional] 
**conto** | **str** | Numero di conto (ad es. \&quot;100.20\&quot;). Sono supportati fino a 5 livelli. Il valore è ricavato da &#x60;Raw&#x60;. | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.conto_contabile import ContoContabile

# TODO update the JSON string below
json = "{}"
# create an instance of ContoContabile from a JSON string
conto_contabile_instance = ContoContabile.from_json(json)
# print the JSON string representation of the object
print(ContoContabile.to_json())

# convert the object into a dict
conto_contabile_dict = conto_contabile_instance.to_dict()
# create an instance of ContoContabile from a dict
conto_contabile_from_dict = ContoContabile.from_dict(conto_contabile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


