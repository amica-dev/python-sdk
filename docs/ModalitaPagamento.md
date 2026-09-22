# ModalitaPagamento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**codice_pagamento_fe** | **str** |  | [optional] 
**ricevuta_bancaria** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.modalita_pagamento import ModalitaPagamento

# TODO update the JSON string below
json = "{}"
# create an instance of ModalitaPagamento from a JSON string
modalita_pagamento_instance = ModalitaPagamento.from_json(json)
# print the JSON string representation of the object
print(ModalitaPagamento.to_json())

# convert the object into a dict
modalita_pagamento_dict = modalita_pagamento_instance.to_dict()
# create an instance of ModalitaPagamento from a dict
modalita_pagamento_from_dict = ModalitaPagamento.from_dict(modalita_pagamento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


