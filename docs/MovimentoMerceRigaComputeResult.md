# MovimentoMerceRigaComputeResult

Restituito dal metodo `ComputeRiga` di `MovimentoMerceService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**riga** | [**MovimentoMerceRiga**](MovimentoMerceRiga.md) |  | [optional] 
**importo** | **float** | Importo, determinato come prodotto tra &#x60;Quantità&#x60; e &#x60;PrezzoNetto&#x60;. Non è memorizzato. | [optional] 
**importo_ivato** | **float** | Importo IVA inclusa, determinato come prodotto tra &#x60;Quantità&#x60; e &#x60;PrezzoIvato&#x60;. Non è memorizzato. | [optional] 

## Example

```python
from amica_python_sdk.models.movimento_merce_riga_compute_result import MovimentoMerceRigaComputeResult

# TODO update the JSON string below
json = "{}"
# create an instance of MovimentoMerceRigaComputeResult from a JSON string
movimento_merce_riga_compute_result_instance = MovimentoMerceRigaComputeResult.from_json(json)
# print the JSON string representation of the object
print(MovimentoMerceRigaComputeResult.to_json())

# convert the object into a dict
movimento_merce_riga_compute_result_dict = movimento_merce_riga_compute_result_instance.to_dict()
# create an instance of MovimentoMerceRigaComputeResult from a dict
movimento_merce_riga_compute_result_from_dict = MovimentoMerceRigaComputeResult.from_dict(movimento_merce_riga_compute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


