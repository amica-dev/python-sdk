# SpesaDocumento

Spesa di documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**documento_id** | **int** | Identificativo univoco di Amica.Documento. | [optional] 
**spesa_id** | **int** | Identificativo univoco di Amica.SpesaDocumento.Spesa. | [optional] 
**spesa** | [**Spesa**](Spesa.md) |  | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di Amica.SpesaDocumento.CausaleIva. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**importo** | **float** | Importo. | [optional] 
**pagamento** | **bool** | Indica se è un pagamento o meno. | [optional] 

## Example

```python
from amica_python_sdk.models.spesa_documento import SpesaDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of SpesaDocumento from a JSON string
spesa_documento_instance = SpesaDocumento.from_json(json)
# print the JSON string representation of the object
print(SpesaDocumento.to_json())

# convert the object into a dict
spesa_documento_dict = spesa_documento_instance.to_dict()
# create an instance of SpesaDocumento from a dict
spesa_documento_from_dict = SpesaDocumento.from_dict(spesa_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


