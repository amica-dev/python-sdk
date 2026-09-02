# ProblemDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**overridable** | **bool** | Indica se l&#39;errore è *forzabile*: ripetendo la stessa richiesta con &#x60;validationOverride&#x3D;true&#x60; il servizio la accetta nonostante la validazione fallita (tipico delle anomalie formali su dati reali, come la partita IVA di un fornitore estero). È presente su tutte le risposte di errore e vale &#x60;false&#x60; per gli errori che non ammettono deroga. | [optional] 

## Example

```python
from amica_python_sdk.models.problem_details import ProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails from a JSON string
problem_details_instance = ProblemDetails.from_json(json)
# print the JSON string representation of the object
print(ProblemDetails.to_json())

# convert the object into a dict
problem_details_dict = problem_details_instance.to_dict()
# create an instance of ProblemDetails from a dict
problem_details_from_dict = ProblemDetails.from_dict(problem_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


