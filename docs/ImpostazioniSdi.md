# ImpostazioniSdi

Impostazioni del servizio di interscambio fatture (SdI).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**api_key_sdi** | **str** | Chiave di licenza del servizio di interscambio fatture. | [optional] 
**ultimo_download_sdi** | **datetime** | Data e ora dell&#39;ultimo aggiornamento ricevuto dal servizio di interscambio fatture (SdI). | [optional] 
**includi_pdf_sdi** | **bool** | Indica se allegare il PDF della fattura a ciascun XML inviato al sistema di interscambio fatture (SdI). | [optional] 
**abbina_articoli_sdi** | **bool** | Per le fatture di acquisto scaricate dal servizio di interscambio fatture (SdI), indica se si desidera tentare l&#39;abbinamento degli articoli/prodotti della fattura con quelli presenti nei magazzini aziendali. | [optional] 

## Example

```python
from amica_sdk.models.impostazioni_sdi import ImpostazioniSdi

# TODO update the JSON string below
json = "{}"
# create an instance of ImpostazioniSdi from a JSON string
impostazioni_sdi_instance = ImpostazioniSdi.from_json(json)
# print the JSON string representation of the object
print(ImpostazioniSdi.to_json())

# convert the object into a dict
impostazioni_sdi_dict = impostazioni_sdi_instance.to_dict()
# create an instance of ImpostazioniSdi from a dict
impostazioni_sdi_from_dict = ImpostazioniSdi.from_dict(impostazioni_sdi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


