# CodicePagamento

Tabella \"Codice Pagamento\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice** | **str** | Codice della voce. | [optional] 
**descrizione** | **str** | Descrizione della voce. | [optional] 

## Example

```python
from amica_sdk.models.codice_pagamento import CodicePagamento

# TODO update the JSON string below
json = "{}"
# create an instance of CodicePagamento from a JSON string
codice_pagamento_instance = CodicePagamento.from_json(json)
# print the JSON string representation of the object
print(CodicePagamento.to_json())

# convert the object into a dict
codice_pagamento_dict = codice_pagamento_instance.to_dict()
# create an instance of CodicePagamento from a dict
codice_pagamento_from_dict = CodicePagamento.from_dict(codice_pagamento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


