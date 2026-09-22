# Documento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**anagrafica** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**causale_documento_id** | **int** |  | [optional] 
**causale_documento** | [**CausaleDocumento**](CausaleDocumento.md) |  | [optional] 
**agente_id** | **int** |  | [optional] 
**agente** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**pagamento_id** | **int** |  | [optional] 
**pagamento** | [**Pagamento**](Pagamento.md) |  | [optional] 
**vettore_id** | **int** |  | [optional] 
**vettore** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**cassa_previdenziale_causale_iva_id** | **int** |  | [optional] 
**modello_id** | **int** |  | [optional] 
**cassa_previdenziale_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**destinazione_id** | **int** |  | [optional] 
**destinazione** | [**Indirizzo**](Indirizzo.md) |  | [optional] 
**valuta_id** | **int** |  | [optional] 
**valuta** | [**Valuta**](Valuta.md) |  | [optional] 
**causale_magazzino_id** | **int** |  | [optional] 
**causale_magazzino** | [**CausaleMagazzino**](CausaleMagazzino.md) |  | [optional] 
**iva1_causale_iva_id** | **int** |  | [optional] 
**iva1_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**iva2_causale_iva_id** | **int** |  | [optional] 
**iva2_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**iva3_causale_iva_id** | **int** |  | [optional] 
**iva3_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**iva4_causale_iva_id** | **int** |  | [optional] 
**iva4_causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**tipo_documento** | **str** |  | [optional] 
**documento_fiscale** | **str** |  | [optional] 
**destinazione_diversa** | **bool** |  | [optional] 
**iva_esclusa** | **bool** |  | [optional] 
**ritenuta_include_cassa_previdenziale** | **bool** |  | [optional] 
**classe_documento** | **str** |  | [optional] 
**contatto** | **int** |  | [optional] 
**numero_parte_testo** | **str** |  | [optional] 
**numero_parte_numerica** | **int** |  | [optional] 
**data** | **datetime** |  | [optional] 
**stato** | **str** |  | [optional] 
**data_scadenza_preventivo** | **datetime** |  | [optional] 
**data_inizio_scadenze** | **datetime** |  | [optional] 
**sconto_percentuale** | **float** |  | [optional] 
**sconto_incondizionato_importo** | **float** |  | [optional] 
**abbuono_importo** | **float** |  | [optional] 
**ritenuta_percentuale** | **float** |  | [optional] 
**enasarco_percentuale** | **float** |  | [optional] 
**enasarco_importo** | **float** |  | [optional] 
**quota_ritenuta_su_imponibile** | **float** |  | [optional] 
**cambio** | **float** |  | [optional] 
**cassa_previdenziale_nome** | **str** |  | [optional] 
**cassa_previdenziale_percentuale** | **float** |  | [optional] 
**note** | **str** |  | [optional] 
**sconto_pagamento_percentuale** | **float** |  | [optional] 
**iva1_imponibile** | **float** |  | [optional] 
**iva2_imponibile** | **float** |  | [optional] 
**iva3_imponibile** | **float** |  | [optional] 
**iva4_imponibile** | **float** |  | [optional] 
**iva1_imponibile_lordo** | **float** |  | [optional] 
**iva2_imponibile_lordo** | **float** |  | [optional] 
**iva3_imponibile_lordo** | **float** |  | [optional] 
**iva4_imponibile_lordo** | **float** |  | [optional] 
**iva1_imposta** | **float** |  | [optional] 
**iva2_imposta** | **float** |  | [optional] 
**iva3_imposta** | **float** |  | [optional] 
**iva4_imposta** | **float** |  | [optional] 
**totale_ritenuta** | **float** |  | [optional] 
**totale_cassa_previdenziale** | **float** |  | [optional] 
**totale_spese** | **float** |  | [optional] 
**totale_spese_esenti** | **float** |  | [optional] 
**totale_spese_non_esenti** | **float** |  | [optional] 
**totale_merce** | **float** |  | [optional] 
**totale_merce_scontata** | **float** |  | [optional] 
**totale_imponibile** | **float** |  | [optional] 
**totale_imposta** | **float** |  | [optional] 
**totale_esente** | **float** |  | [optional] 
**totale_documento** | **float** |  | [optional] 
**netto_a_pagare** | **float** |  | [optional] 
**totale_split_payment** | **float** |  | [optional] 
**bollo** | **float** |  | [optional] 
**xml_file_name** | **str** |  | [optional] 
**riferimento_amministrazione** | **str** |  | [optional] 
**banca** | [**BancaDocumento**](BancaDocumento.md) |  | [optional] 
**dati_trasporto** | [**DatiTrasporto**](DatiTrasporto.md) |  | [optional] 
**dati_sdi** | [**DatiSdi**](DatiSdi.md) |  | [optional] 
**dati_pa** | [**DatiPA**](DatiPA.md) |  | [optional] 
**righe** | [**List[BeneServizio]**](BeneServizio.md) |  | [optional] 
**spese_documento** | [**List[SpesaDocumento]**](SpesaDocumento.md) |  | [optional] 
**scadenze** | [**List[Scadenza]**](Scadenza.md) |  | [optional] 
**numero** | **str** |  | [optional] 
**media_file** | [**DocumentoMediaFile**](DocumentoMediaFile.md) |  | [optional] 
**allegato** | **str** |  | [optional] 
**bonus_fiscale_causale** | **str** |  | [optional] 
**bonus_fiscale_importo** | **float** |  | [optional] 
**bonus_fiscale_percentuale** | **float** |  | [optional] 
**progressivo_invio** | [**List[ProgressivoInvio]**](ProgressivoInvio.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.documento import Documento

# TODO update the JSON string below
json = "{}"
# create an instance of Documento from a JSON string
documento_instance = Documento.from_json(json)
# print the JSON string representation of the object
print(Documento.to_json())

# convert the object into a dict
documento_dict = documento_instance.to_dict()
# create an instance of Documento from a dict
documento_from_dict = Documento.from_dict(documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


