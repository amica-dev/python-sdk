# InventarioComputeResult

Restituito dai metodi `Compute` e `Process` di `InventarioService`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**righe** | [**List[InventarioRiga]**](InventarioRiga.md) | Righe dell&#39;inventario elaborato. | [optional] 
**avvisi** | **List[str]** | Avvisi dell&#39;elaborazione, da mostrare all&#39;utente. | [optional] 
**concurrency_token** | **int** | Impronta delle righe elaborate. Passata a &#x60;Process&#x60;, impedisce il salvataggio se nel frattempo i dati sono cambiati e l&#39;elaborazione darebbe righe diverse. | [optional] 
**giacenze_allineabili** | **bool** | Indica se &#x60;Process&#x60; con &#x60;alignStock&#x60; allineerebbe davvero le giacenze: non le allinea se nel magazzino ci sono movimenti successivi alla data dell&#39;inventario. | [optional] 
**inventario** | [**Inventario**](Inventario.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.inventario_compute_result import InventarioComputeResult

# TODO update the JSON string below
json = "{}"
# create an instance of InventarioComputeResult from a JSON string
inventario_compute_result_instance = InventarioComputeResult.from_json(json)
# print the JSON string representation of the object
print(InventarioComputeResult.to_json())

# convert the object into a dict
inventario_compute_result_dict = inventario_compute_result_instance.to_dict()
# create an instance of InventarioComputeResult from a dict
inventario_compute_result_from_dict = InventarioComputeResult.from_dict(inventario_compute_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


