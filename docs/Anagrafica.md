# Anagrafica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**modello_id** | **int** |  | [optional] 
**nazione_id** | **int** |  | [optional] 
**nazione** | [**Nazione**](Nazione.md) |  | [optional] 
**area_geografica_id** | **int** |  | [optional] 
**area_geografica** | [**AreaGeografica**](AreaGeografica.md) |  | [optional] 
**valuta_id** | **int** |  | [optional] 
**valuta** | [**Valuta**](Valuta.md) |  | [optional] 
**indirizzo_predefinito_id** | **int** |  | [optional] 
**indirizzi** | [**List[Indirizzo]**](Indirizzo.md) |  | [optional] 
**scheda_cliente** | [**SchedaCliente**](SchedaCliente.md) |  | [optional] 
**scheda_fornitore** | [**SchedaFornitore**](SchedaFornitore.md) |  | [optional] 
**stato** | **bool** |  | [optional] 
**cliente** | **bool** |  | [optional] 
**fornitore** | **bool** |  | [optional] 
**agente** | **bool** |  | [optional] 
**vettore** | **bool** |  | [optional] 
**capo_area** | **bool** |  | [optional] 
**persona_giuridica** | **bool** |  | [optional] 
**banca** | [**Banca**](Banca.md) |  | [optional] 
**nominativo1** | [**AnagraficaNominativo1**](AnagraficaNominativo1.md) |  | [optional] 
**nominativo2** | [**AnagraficaNominativo2**](AnagraficaNominativo2.md) |  | [optional] 
**sede_legale** | [**AnagraficaSedeLegale**](AnagraficaSedeLegale.md) |  | [optional] 
**codice** | **str** |  | [optional] 
**data_inserimento** | **datetime** |  | [optional] 
**ragione_sociale1** | **str** |  | 
**ragione_sociale2** | **str** |  | [optional] 
**e_mail** | **str** |  | [optional] 
**sito_web** | **str** |  | [optional] 
**partita_iva** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**note_importanti** | **str** |  | [optional] 
**pec** | **str** |  | [optional] 
**codice_destinatario** | **str** |  | [optional] 
**dichiarazione_intento** | **str** |  | [optional] 
**riferimento_amministrazione** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.anagrafica import Anagrafica

# TODO update the JSON string below
json = "{}"
# create an instance of Anagrafica from a JSON string
anagrafica_instance = Anagrafica.from_json(json)
# print the JSON string representation of the object
print(Anagrafica.to_json())

# convert the object into a dict
anagrafica_dict = anagrafica_instance.to_dict()
# create an instance of Anagrafica from a dict
anagrafica_from_dict = Anagrafica.from_dict(anagrafica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


