# Articolo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**categoria_merceologica_id** | **int** |  | [optional] 
**categoria_merceologica** | [**CategoriaMerceologica**](CategoriaMerceologica.md) |  | [optional] 
**gruppo_merceologico_id** | **int** |  | [optional] 
**gruppo_merceologico** | [**GruppoMerceologico**](GruppoMerceologico.md) |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**taglia_id** | **int** |  | [optional] 
**taglia** | [**Taglia**](Taglia.md) |  | [optional] 
**marca_id** | **int** |  | [optional] 
**marca** | [**Marca**](Marca.md) |  | [optional] 
**produttore_id** | **int** |  | [optional] 
**produttore** | [**Produttore**](Produttore.md) |  | [optional] 
**nome** | **str** |  | 
**codice** | **str** |  | 
**nome_breve** | **str** |  | [optional] 
**codice_fornitore** | **str** |  | [optional] 
**codice_produttore** | **str** |  | [optional] 
**gestione_articolo** | **str** |  | [optional] 
**contesto_articolo** | **str** |  | [optional] 
**bar_code** | **str** |  | [optional] 
**costo_ultimo** | **float** |  | [optional] 
**costo_medio** | **float** |  | [optional] 
**unit_misura_intera** | **bool** |  | [optional] 
**articolo_composto** | **bool** |  | [optional] 
**stato** | **bool** |  | [optional] 
**data_inserimento** | **datetime** |  | [optional] 
**unit_misura_movimenti** | **str** |  | [optional] 
**unit_misura_inventario** | **str** |  | [optional] 
**fattore_conversione_unit_misura** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**media_file** | [**ArticoloMediaFile**](ArticoloMediaFile.md) |  | [optional] 
**conto_raw_vendita** | **str** |  | [optional] 
**conto_raw_acquisto** | **str** |  | [optional] 
**distinta_base** | [**List[Componente]**](Componente.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.articolo import Articolo

# TODO update the JSON string below
json = "{}"
# create an instance of Articolo from a JSON string
articolo_instance = Articolo.from_json(json)
# print the JSON string representation of the object
print(Articolo.to_json())

# convert the object into a dict
articolo_dict = articolo_instance.to_dict()
# create an instance of Articolo from a dict
articolo_from_dict = Articolo.from_dict(articolo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


