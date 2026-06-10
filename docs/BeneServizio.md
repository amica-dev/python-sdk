# BeneServizio

Bene o servizio fatturato.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**documento_id** | **int** | Identificativo univoco del Amica.Documento (documento). | [optional] 
**articolo_id** | **int** | Identificativo univoco dell&#39;Amica.BeneServizio.Articolo (articolo o prodotto). | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**prestazione_id** | **int** | Identificativo univoco della Amica.BeneServizio.Prestazione (prestazione). | [optional] 
**prestazione** | [**Articolo**](Articolo.md) |  | [optional] 
**magazzino_id** | **int** | Identificativo univoco del Amica.BeneServizio.Magazzino (magazzino). Obbligatorio quando viene usato Amica.BeneServizio.Codice. | [optional] 
**magazzino** | [**Magazzino**](Magazzino.md) |  | [optional] 
**causale_iva_id** | **int** | Identificativo univoco della Amica.BeneServizio.CausaleIva. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**listino_id** | **int** | Identificativo univoco del Amica.BeneServizio.Listino (listino). | [optional] 
**listino** | [**Listino**](Listino.md) |  | [optional] 
**ordine_id** | **int** | Identificativo univoco del Amica.Documento (ordine). | [optional] 
**bene_servizio_ordine_id** | **int** | Identificativo univoco del Amica.BeneServizio (bene o servizio) all&#39;interno dell&#39;ordine referenziato da Amica.BeneServizio.OrdineId. | [optional] 
**taglia_id** | **int** | Identificativo univoco della Amica.BeneServizio.Taglia (taglia). | [optional] 
**taglia** | [**Taglia**](Taglia.md) |  | [optional] 
**ritenuta_fiscale** | **bool** | Indica se al bene o servizio deve essere applicata una ritenuta fiscale. &#x60;true&#x60; se deve essere applicata, &#x60;false&#x60; altrimenti. | [optional] 
**posizione** | **int** | Indice di riga all&#39;interno del documento. Questa proprietà è utilizzata solo dal client desktop Amica 20 per Windows e deve essere considerata obsoleta. | [optional] 
**codice** | **str** | Codice del bene o servizio. | [optional] 
**descrizione** | **str** | Descrizione. | 
**unit_misura** | **str** | Unità di misura. | [optional] 
**quantit** | **float** | Quantità movimentata. | [optional] 
**quantit_evasa** | **float** | Quantità dell&#39;ordine evasa. Questo valore viene aggiornato automaticamente quando viene emessa una fattura o un DDT che contiene un riferimento a un ordine ed è attivo &lt;a href&#x3D;\&quot;https://gestionaleamica.com/Software/GestioneOrdiniPreventivi\&quot;&gt;Ordini e Preventivi&lt;/a&gt;. | [optional] 
**quantit_da_evadere** | **float** | Quantità che resta da evadere. | [optional] [readonly] 
**sconto1** | **float** | Primo sconto percentuale, applicato al prezzo del bene o servizio. | [optional] 
**sconto2** | **float** | Secondo sconto percentuale, applicato dopo l&#39;applicazione di Amica.BeneServizio.Sconto1 | [optional] 
**sconto3** | **float** | Terzo sconto percentuale, applicato dopo l&#39;applicazione di Amica.BeneServizio.Sconto2 | [optional] 
**sconto4** | **float** | Quarto sconto percentuale, applicato dopo l&#39;applicazione di Amica.BeneServizio.Sconto3 | [optional] 
**sconto_incondizionato** | **float** | Sconto incondizionato, in valuta, applicato al prezzo del bene o servizio. | [optional] 
**provvigione_agente** | **float** | Provvigione corrisposta all&#39;agente, in percentuale. | [optional] 
**provvigione_capo_area** | **float** | Provvigione corrisposta al capo area, in percentuale. | [optional] 
**prezzo_id** | **int** | Identificativo univoco del Amica.BeneServizio.Prezzo (prezzo). | [optional] 
**prezzo** | **float** | Prezzo. | [optional] 
**prezzo_scontato** | **float** | Prezzo scontato, cioè al netto degli sconti percentuali indicati e dello sconto incondizionato. | [optional] 
**prezzo_ivato** | **float** | Prezzo comprensivo di IVA. | [optional] 
**importo** | **float** | Importo, determinato come prodotto di Amica.BeneServizio.Quantità e Amica.BeneServizio.PrezzoScontato. | [optional] 
**dati_aggiuntivi** | [**DatiAggiuntivi**](DatiAggiuntivi.md) |  | [optional] 
**sconto** | **str** | Descrizione di tutti gli sconti combinati (es: \&quot;10,5%+5€\&quot;). | [optional] [readonly] 

## Example

```python
from amica_sdk.models.bene_servizio import BeneServizio

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


