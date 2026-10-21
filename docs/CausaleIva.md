# CausaleIva

Causale IVA.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**codice** | **str** | Codice. | 
**nome** | **str** | Nome, o descrizione. | 
**aliquota** | **float** | Aliquota applicabile. Il valore è una frazione: &#x60;0.22&#x60; corrisponde al 22%. | [optional] 
**indeducibilit** | **float** | Quota di indeducibilità. | [optional] 
**intracomunitaria** | **bool** | Indica se l&#39;IVA è intracomunitaria. | [optional] 
**non_imponibile** | **bool** | Indica se l&#39;IVA non deve essere considerata nella determinazione dell&#39;imponibile. | [optional] 
**natura** | **str** | Natura dell&#39;esenzione (codice), se applicabile (ad es. \&quot;N1\&quot;). | [optional] 
**split_payment** | **bool** | Indica se si applica lo split payment o meno. | [optional] 
**fattura_elettronica** | **bool** | Indica se l&#39;IVA è stata creata automaticamente durante l&#39;importazione di una fattura elettronica. | [optional] 

## Example

```python
from amica_python_sdk.models.causale_iva import CausaleIva

# TODO update the JSON string below
json = "{}"
# create an instance of CausaleIva from a JSON string
causale_iva_instance = CausaleIva.from_json(json)
# print the JSON string representation of the object
print(CausaleIva.to_json())

# convert the object into a dict
causale_iva_dict = causale_iva_instance.to_dict()
# create an instance of CausaleIva from a dict
causale_iva_from_dict = CausaleIva.from_dict(causale_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


