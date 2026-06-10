# DatiTrasporto

Dati di trasporto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colli** | **int** | Numero di colli che compongono la spedizione. | [optional] 
**peso** | **float** | Peso totale della spedizione. | [optional] 
**peso_unit_misura** | **str** | Unità di misura applicata al &#x60;Peso&#x60; (es. \&quot;KG\&quot;). | [optional] 
**data_trasporto** | **datetime** | Data di inizio del trasporto. | [optional] 
**porto** | **str** | Porto: assegnato, franco, ecc. | [optional] 
**mezzo_di_trasporto** | **str** | Mezzo di trasporto. | [optional] 
**aspetto_beni** | **str** | Aspetto esteriore dei beni trasportati. | [optional] 
**autista_nome** | **str** | Nome dell&#39;autista. | [optional] 
**autista_targa** | **str** | Targa del veicolo che effettua il trasporto. | [optional] 
**autista_patente** | **str** | Numero della patente dell&#39;autista. | [optional] 

## Example

```python
from amica_sdk.models.dati_trasporto import DatiTrasporto

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasporto from a JSON string
dati_trasporto_instance = DatiTrasporto.from_json(json)
# print the JSON string representation of the object
print(DatiTrasporto.to_json())

# convert the object into a dict
dati_trasporto_dict = dati_trasporto_instance.to_dict()
# create an instance of DatiTrasporto from a dict
dati_trasporto_from_dict = DatiTrasporto.from_dict(dati_trasporto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


