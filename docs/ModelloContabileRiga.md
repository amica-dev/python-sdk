# ModelloContabileRiga

Riga di un `ModelloContabile`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**modello_contabile_id** | **int** | Identificativo univoco di &#x60;ModelloContabile&#x60;. | [optional] 
**causale_contabile_id** | **int** | Identificativo univoco di &#x60;CausaleContabile&#x60;. | [optional] 
**conto_raw** | **str** | Numero di conto, in formato grezzo. Sono supportati fino a cinque livelli, ciascuno espresso da un massimo di cinque caratteri allineati a destra e riempiti con spazi, ad es. \&quot;  100   20\&quot; (dieci caratteri in totale) esprime \&quot;100.20\&quot;. | 
**importo** | **float** | Importo. | [optional] 
**tipo_importo** | **str** | Cosa rappresenta &#x60;Importo&#x60;. | [optional] 
**segno_contabile** | **str** | Dare o avere. | [optional] 

## Example

```python
from amica_python_sdk.models.modello_contabile_riga import ModelloContabileRiga

# TODO update the JSON string below
json = "{}"
# create an instance of ModelloContabileRiga from a JSON string
modello_contabile_riga_instance = ModelloContabileRiga.from_json(json)
# print the JSON string representation of the object
print(ModelloContabileRiga.to_json())

# convert the object into a dict
modello_contabile_riga_dict = modello_contabile_riga_instance.to_dict()
# create an instance of ModelloContabileRiga from a dict
modello_contabile_riga_from_dict = ModelloContabileRiga.from_dict(modello_contabile_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


