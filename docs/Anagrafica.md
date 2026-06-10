# Anagrafica

Anagrafica di cliente, fornitore, agente o vettore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**modello_id** | **int** | Identificativo univoco di &#x60;Modello&#x60;. Sempre null. Questa proprietà è usata solo dal client desktop Amica 20 per Windows ed è da considerarsi obsoleta. | [optional] 
**nazione_id** | **int** | Identificativo univoco di Amica.Anagrafica.Nazione (nazione). | [optional] 
**nazione** | [**Nazione**](Nazione.md) |  | [optional] 
**area_geografica_id** | **int** | Identificativo univoco di Amica.Anagrafica.AreaGeografica (area geografica). | [optional] 
**area_geografica** | [**AreaGeografica**](AreaGeografica.md) |  | [optional] 
**valuta_id** | **int** | Identificativo univoco di Amica.Anagrafica.Valuta (valuta). | [optional] 
**valuta** | [**Valuta**](Valuta.md) |  | [optional] 
**indirizzo_predefinito_id** | **int** | Identificativo univoco dell&#39;Amica.Indirizzo (indirizzo) predefinito. | [optional] 
**indirizzi** | [**List[Indirizzo]**](Indirizzo.md) | Elenco degli Amica.Indirizzo dell&#39;anagrafica. | [optional] 
**scheda_cliente** | [**SchedaCliente**](SchedaCliente.md) |  | [optional] 
**scheda_fornitore** | [**SchedaFornitore**](SchedaFornitore.md) |  | [optional] 
**stato** | **bool** | Indica se l&#39;anagrafica è attiva o meno. | [optional] 
**cliente** | **bool** | Indica se l&#39;anagrafica è un cliente. | [optional] 
**fornitore** | **bool** | Indica se l&#39;anagrafica è un fornitore. | [optional] 
**agente** | **bool** | Indica se l&#39;anagrafica opera come agente di vendita per conto dell&#39;azienda. | [optional] 
**vettore** | **bool** | Indica se l&#39;anagrafica opera come vettore. | [optional] 
**capo_area** | **bool** | Indica se l&#39;anagrafica opera come capo area. | [optional] 
**persona_giuridica** | **bool** | Indica se l&#39;anagrafica è una persona giuridica o meno. &#x60;true&#x60; indica una persona giuridica, &#x60;false&#x60; una persona fisica. | [optional] 
**banca** | [**Banca**](Banca.md) |  | [optional] 
**nominativo1** | [**AnagraficaNominativo1**](AnagraficaNominativo1.md) |  | [optional] 
**nominativo2** | [**AnagraficaNominativo2**](AnagraficaNominativo2.md) |  | [optional] 
**sede_legale** | [**AnagraficaSedeLegale**](AnagraficaSedeLegale.md) |  | [optional] 
**codice** | **str** | Codice assegnato all&#39;anagrafica. | [optional] 
**data_inserimento** | **datetime** | Data di primo inserimento. | [optional] 
**ragione_sociale1** | **str** | Ragione sociale, oppure nome e cognome della persona fisica. | 
**ragione_sociale2** | **str** | Eventuale seconda riga della ragione sociale. Usata principalmente nelle stampe, quando si vuole suddividere la ragione sociale su due righe. | [optional] 
**e_mail** | **str** | Indirizzo email. | [optional] 
**sito_web** | **str** | Indirizzo web. | [optional] 
**partita_iva** | **str** | Partita IVA. | [optional] 
**codice_fiscale** | **str** | Codice fiscale. Solitamente diverso dalla Amica.Anagrafica.PartitaIva. | [optional] 
**note** | **str** | Note. | [optional] 
**note_importanti** | **str** | Note rilevanti. I client ufficiali Amica le evidenziano alla creazione di un nuovo documento fiscale. | [optional] 
**pec** | **str** | Indirizzo Pec (posta elettronica certificata). | [optional] 
**codice_destinatario** | **str** | Codice destinatario per il sistema fiscale italiano. Usato per il recapito delle fatture elettroniche italiane. | [optional] 
**dichiarazione_intento** | **str** | Numero di protocollo della dichiarazione d&#39;intento. | [optional] 
**riferimento_amministrazione** | **str** | Solitamente necessario quando si ha a che fare con enti della Pubblica Amministrazione italiana. Identifica univocamente l&#39;ufficio di destinazione all&#39;interno della PA. | [optional] 

## Example

```python
from amica_sdk.models.anagrafica import Anagrafica

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


