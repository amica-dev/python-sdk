# FatturaElettronicaXml

Contenuto della fattura elettronica (XML).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**file_name** | **str** | Nome del file. | [optional] 
**xml** | **str** | Contenuto del file. | [optional] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaXml from a JSON string
fattura_elettronica_xml_instance = FatturaElettronicaXml.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaXml.to_json())

# convert the object into a dict
fattura_elettronica_xml_dict = fattura_elettronica_xml_instance.to_dict()
# create an instance of FatturaElettronicaXml from a dict
fattura_elettronica_xml_from_dict = FatturaElettronicaXml.from_dict(fattura_elettronica_xml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


