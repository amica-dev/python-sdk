# BeneServizio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**documento_id** | **int** |  | [optional] 
**documento** | [**Documento**](Documento.md) |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**prestazione_id** | **int** |  | [optional] 
**prestazione** | [**Articolo**](Articolo.md) |  | [optional] 
**magazzino_id** | **int** |  | [optional] 
**magazzino** | [**Magazzino**](Magazzino.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**listino_id** | **int** |  | [optional] 
**listino** | [**Listino**](Listino.md) |  | [optional] 
**ordine_id** | **int** |  | [optional] 
**bene_servizio_ordine_id** | **int** |  | [optional] 
**taglia_id** | **int** |  | [optional] 
**taglia** | [**Taglia**](Taglia.md) |  | [optional] 
**ritenuta_fiscale** | **bool** |  | [optional] 
**posizione** | **int** |  | [optional] 
**codice** | **str** |  | [optional] 
**descrizione** | **str** |  | 
**unit_misura** | **str** |  | [optional] 
**quantit** | **float** |  | [optional] 
**quantit_evasa** | **float** |  | [optional] 
**quantit_da_evadere** | **float** |  | [optional] [readonly] 
**sconto1** | **float** |  | [optional] 
**sconto2** | **float** |  | [optional] 
**sconto3** | **float** |  | [optional] 
**sconto4** | **float** |  | [optional] 
**sconto_incondizionato** | **float** |  | [optional] 
**provvigione_agente** | **float** |  | [optional] 
**provvigione_capo_area** | **float** |  | [optional] 
**prezzo_id** | **int** |  | [optional] 
**prezzo** | **float** |  | [optional] 
**prezzo_scontato** | **float** |  | [optional] 
**prezzo_ivato** | **float** |  | [optional] 
**importo** | **float** |  | [optional] 
**dati_aggiuntivi** | [**DatiAggiuntivi**](DatiAggiuntivi.md) |  | [optional] 
**sconto** | **str** |  | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.bene_servizio import BeneServizio

# TODO update the JSON string below
json = "{}"
# create an instance of BeneServizio from a JSON string
bene_servizio_instance = BeneServizio.from_json(json)
# print the JSON string representation of the object
print(BeneServizio.to_json())

# convert the object into a dict
bene_servizio_dict = bene_servizio_instance.to_dict()
# create an instance of BeneServizio from a dict
bene_servizio_from_dict = BeneServizio.from_dict(bene_servizio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


