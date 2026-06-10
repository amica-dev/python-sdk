# Componente

Componente (distinta base). Può essere incluso in Amica.Articolo.DistintaBase.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**articolo_id** | **int** | Identificativo univoco dell&#39;Amica.Componente.Articolo da comporre. | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**articolo_componente_id** | **int** | Identificativo univoco del componente (distinta base). | [optional] 
**articolo_componente** | [**Articolo**](Articolo.md) |  | [optional] 
**quantita_necessaria** | **float** | Quantità necessaria per l&#39;assemblaggio. | [optional] 

## Example

```python
from amica_sdk.models.componente import Componente

# TODO update the JSON string below
json = "{}"
# create an instance of Componente from a JSON string
componente_instance = Componente.from_json(json)
# print the JSON string representation of the object
print(Componente.to_json())

# convert the object into a dict
componente_dict = componente_instance.to_dict()
# create an instance of Componente from a dict
componente_from_dict = Componente.from_dict(componente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


