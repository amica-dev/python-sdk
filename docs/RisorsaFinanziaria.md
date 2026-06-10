# RisorsaFinanziaria

Risorsa finanziaria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome o descrizione. | 
**indirizzo** | **str** | Indirizzo. | [optional] 
**localit** | **str** | Città, comune o altra denominazione di località. | [optional] 
**cap** | **str** | CAP o codice di zona. | [optional] 
**provincia** | **str** | Provincia o denominazione dell&#39;area. | [optional] 
**telefono1** | **str** | Numero di telefono principale. | [optional] 
**telefono2** | **str** | Numero di telefono secondario. | [optional] 
**fax** | **str** | Numero di fax. | [optional] 
**contatto1_nome** | **str** | Nome del contatto. | [optional] 
**contatto1_incarico** | **str** | Qualifica o ruolo del contatto. | [optional] 
**contatto1_telefono1** | **str** | Telefono principale del contatto. | [optional] 
**contatto1_telefono2** | **str** | Telefono secondario del contatto. | [optional] 
**contatto1_e_mail** | **str** | Email del contatto. | [optional] 
**contatto2_nome** | **str** | Nome del contatto secondario. | [optional] 
**contatto2_incarico** | **str** | Qualifica o ruolo del contatto secondario. | [optional] 
**contatto2_telefono1** | **str** | Numero di telefono del contatto secondario. | [optional] 
**contatto2_telefono2** | **str** | Numero di telefono alternativo del contatto secondario. | [optional] 
**contatto2_e_mail** | **str** | Email del contatto secondario. | [optional] 
**codice_abi** | **str** | Codice ABI. | [optional] 
**codice_cab** | **str** | Codice CAB. | [optional] 
**conto_corrente** | **str** | Numero di conto corrente. | [optional] 
**codice_cin** | **str** | Codice CIN. | [optional] 
**codice_cin_eur** | **str** | CIN EUR. | [optional] 
**codice_cin_paese** | **str** | Codice CIN della nazione. | [optional] 
**codice_swift** | **str** | Codice SWIFT. | [optional] 
**codice_iban** | **str** | Codice IBAN. | [optional] 
**web** | **str** | Sito web. | [optional] 
**tipologia** | **str** | Tipologia di risorsa finanziaria. | [optional] 

## Example

```python
from amica_sdk.models.risorsa_finanziaria import RisorsaFinanziaria

# TODO update the JSON string below
json = "{}"
# create an instance of RisorsaFinanziaria from a JSON string
risorsa_finanziaria_instance = RisorsaFinanziaria.from_json(json)
# print the JSON string representation of the object
print(RisorsaFinanziaria.to_json())

# convert the object into a dict
risorsa_finanziaria_dict = risorsa_finanziaria_instance.to_dict()
# create an instance of RisorsaFinanziaria from a dict
risorsa_finanziaria_from_dict = RisorsaFinanziaria.from_dict(risorsa_finanziaria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


