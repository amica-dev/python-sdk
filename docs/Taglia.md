# Taglia

Taglia.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome. | 
**taglia1** | **str** | Identificativo taglia #1 (es. &#39;XL&#39;). | [optional] 
**taglia2** | **str** | Identificativo taglia #2. | [optional] 
**taglia3** | **str** | Identificativo taglia #3. | [optional] 
**taglia4** | **str** | Identificativo taglia #4. | [optional] 
**taglia5** | **str** | Identificativo taglia #5. | [optional] 
**taglia6** | **str** | Identificativo taglia #6. | [optional] 
**taglia7** | **str** | Identificativo taglia #7. | [optional] 
**taglia8** | **str** | Identificativo taglia #8. | [optional] 
**taglia9** | **str** | Identificativo taglia #9. | [optional] 
**taglia10** | **str** | Identificativo taglia #10. | [optional] 
**taglia11** | **str** | Identificativo taglia #11. | [optional] 
**taglia12** | **str** | Identificativo taglia #12. | [optional] 
**taglia13** | **str** | Identificativo taglia #13. | [optional] 
**taglia14** | **str** | Identificativo taglia #14. | [optional] 
**taglia15** | **str** | Identificativo taglia #15. | [optional] 
**taglia16** | **str** | Identificativo taglia #16. | [optional] 

## Example

```python
from amica_python_sdk.models.taglia import Taglia

# TODO update the JSON string below
json = "{}"
# create an instance of Taglia from a JSON string
taglia_instance = Taglia.from_json(json)
# print the JSON string representation of the object
print(Taglia.to_json())

# convert the object into a dict
taglia_dict = taglia_instance.to_dict()
# create an instance of Taglia from a dict
taglia_from_dict = Taglia.from_dict(taglia_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


