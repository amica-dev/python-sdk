# ModelloContabile

Modello contabile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**codice** | **str** | Codice del modello. | 
**nome** | **str** | Nome. | 
**stato** | **bool** | Indica se il modello è attivo o meno. | [optional] 
**registro_iva_id** | **int** | Identificativo univoco di &#x60;RegistroIva&#x60;. | [optional] 
**segno_iva** | **str** | Positività o negatività dell&#39;IVA. | [optional] 
**tipo_operazione_contabile** | **str** | Tipo di operazione contabile. | [optional] 
**tipo_registrazione_contabile** | **str** | Tipo di registrazione contabile. | [optional] 
**azione_partita** | **str** | Effetto sulla partita aperta. | [optional] 
**righe** | [**List[ModelloContabileRiga]**](ModelloContabileRiga.md) | Righe del modello contabile. | [optional] 

## Example

```python
from amica_sdk.models.modello_contabile import ModelloContabile

# TODO update the JSON string below
json = "{}"
# create an instance of ModelloContabile from a JSON string
modello_contabile_instance = ModelloContabile.from_json(json)
# print the JSON string representation of the object
print(ModelloContabile.to_json())

# convert the object into a dict
modello_contabile_dict = modello_contabile_instance.to_dict()
# create an instance of ModelloContabile from a dict
modello_contabile_from_dict = ModelloContabile.from_dict(modello_contabile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


