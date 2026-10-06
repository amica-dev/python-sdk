# Articolo

Articolo di magazzino o prodotto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**categoria_merceologica_id** | **int** | Identificativo univoco della &#x60;CategoriaMerceologica&#x60; (categoria merceologica). | [optional] 
**categoria_merceologica** | [**CategoriaMerceologica**](CategoriaMerceologica.md) |  | [optional] 
**gruppo_merceologico_id** | **int** | Identificativo univoco del &#x60;GruppoMerceologico&#x60; (gruppo merceologico). | [optional] 
**gruppo_merceologico** | [**GruppoMerceologico**](GruppoMerceologico.md) |  | [optional] 
**causale_iva_id** | **int** | Identificativo univoco della &#x60;CausaleIva&#x60; (causale IVA). Id univoco della &lt;a href&#x3D;\&quot;#tag/CausaleIva\&quot;&gt;causale IVA&lt;/a&gt; predefinita per l&#39;articolo. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**taglia_id** | **int** | Identificativo univoco della &#x60;Taglia&#x60; (taglia). | [optional] 
**taglia** | [**Taglia**](Taglia.md) |  | [optional] 
**marca_id** | **int** | Identificativo univoco della &#x60;Marca&#x60;. | [optional] 
**marca** | [**Marca**](Marca.md) |  | [optional] 
**produttore_id** | **int** | Identificativo univoco del &#x60;Produttore&#x60; (produttore). | [optional] 
**produttore** | [**Produttore**](Produttore.md) |  | [optional] 
**nome** | **str** | Nome. | 
**codice** | **str** | Identificativo, o codice. | 
**nome_breve** | **str** | Nome breve. | [optional] 
**codice_fornitore** | **str** | Codice dell&#39;articolo o prodotto presso il fornitore. | [optional] 
**codice_produttore** | **str** | Codice dell&#39;articolo o prodotto presso il produttore. | [optional] 
**gestione_articolo** | **str** | Modalità di gestione. | [optional] 
**contesto_articolo** | **str** | Contesto in cui viene utilizzato. | [optional] 
**bar_code** | **str** | Codice a barre. | [optional] 
**costo_ultimo** | **float** | Ultimo prezzo di costo. | [optional] 
**costo_medio** | **float** | Prezzo di costo medio. | [optional] 
**unit_misura_intera** | **bool** | Indica se l&#39;unità di misura deve essere arrotondata all&#39;intero più vicino. | [optional] 
**articolo_composto** | **bool** | Indica se è composto assemblando altri articoli. | [optional] 
**stato** | **bool** | Stato. &#x60;true&#x60; se attivo, &#x60;false&#x60; altrimenti. | [optional] 
**data_inserimento** | **datetime** | Data di primo inserimento. | [optional] 
**unit_misura_movimenti** | **str** | Unità di misura da utilizzare nei movimenti di magazzino. | [optional] 
**unit_misura_inventario** | **str** | Unità di misura da utilizzare nelle elaborazioni di inventario. | [optional] 
**fattore_conversione_unit_misura** | **float** | Fattore di conversione tra unità di movimento e unità di inventario. | [optional] 
**note** | **str** | Note. | [optional] 
**media_file** | [**ArticoloMediaFile**](ArticoloMediaFile.md) |  | [optional] 
**conto_raw_vendita** | **str** | Conto da utilizzare nelle registrazioni contabili di vendita. | [optional] 
**conto_raw_acquisto** | **str** | Conto da utilizzare nelle registrazioni contabili di acquisto. | [optional] 
**distinta_base** | [**List[Componente]**](Componente.md) | Distinta base. | [optional] 

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


