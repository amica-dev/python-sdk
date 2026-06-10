# BancaDocumento

La banca di un documento (fattura).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome** | **str** | Nome. | [optional] 
**iban** | **str** | Codice IBAN. | [optional] 
**abi** | **str** | Codice ABI. | [optional] 
**cab** | **str** | Codice CAB. | [optional] 
**conto_corrente** | **str** | Numero di conto corrente. | [optional] 
**bic** | **str** | Codice BIC. | [optional] 

## Example

```python
from amica_sdk.models.banca_documento import BancaDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of BancaDocumento from a JSON string
banca_documento_instance = BancaDocumento.from_json(json)
# print the JSON string representation of the object
print(BancaDocumento.to_json())

# convert the object into a dict
banca_documento_dict = banca_documento_instance.to_dict()
# create an instance of BancaDocumento from a dict
banca_documento_from_dict = BancaDocumento.from_dict(banca_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


