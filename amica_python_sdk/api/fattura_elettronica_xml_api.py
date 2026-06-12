# coding: utf-8

"""
    Customers API

    La Customers API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare la Customers API registra la tua applicazione sull'**App Store di Amica**. Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  - **Authorization Code con PKCE** (consigliato per app che operano per conto di un utente Amica): l'utente autorizza la tua app tramite la pagina di consenso dell'identity provider; la tua app riceve un `code` da scambiare con un access token.    ```   GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256   POST {identity-provider}/connect/token        grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri>   ```  - **Client Credentials** (per integrazioni server-to-server, senza utente interattivo):    ```   POST {identity-provider}/connect/token   Content-Type: application/x-www-form-urlencoded    grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=read write documenti contabilita   ```    > **Nota:** il flusso Client Credentials è disponibile solo per le **app private**, non per quelle pubblicate sul marketplace.  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: v3
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr
from typing import List, Optional, Tuple, Union
from typing_extensions import Annotated
from amica_python_sdk.models.allegato_documento import AllegatoDocumento
from amica_python_sdk.models.fattura_elettronica_export_options import FatturaElettronicaExportOptions
from amica_python_sdk.models.fattura_elettronica_export_result import FatturaElettronicaExportResult
from amica_python_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult
from amica_python_sdk.models.fattura_elettronica_upload_options import FatturaElettronicaUploadOptions
from amica_python_sdk.models.fattura_elettronica_upload_result import FatturaElettronicaUploadResult
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_date_range_options import FatturaElettronicaXmlGetArchiveByDateRangeOptions
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_file_name_options import FatturaElettronicaXmlGetArchiveByFileNameOptions
from amica_python_sdk.models.fattura_elettronica_xml_style_sheet_data import FatturaElettronicaXmlStyleSheetData

from amica_python_sdk.api_client import ApiClient, RequestSerialized
from amica_python_sdk.api_response import ApiResponse
from amica_python_sdk.rest import RESTResponseType


class FatturaElettronicaXmlApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_get_archive_by_date_range_options: Annotated[Optional[FatturaElettronicaXmlGetArchiveByDateRangeOptions], Field(description="Opzioni di download.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.

        Non è possibile scaricare più di 350 file alla volta.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_get_archive_by_date_range_options: Opzioni di download.
        :type fattura_elettronica_xml_get_archive_by_date_range_options: FatturaElettronicaXmlGetArchiveByDateRangeOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_get_archive_by_date_range_options=fattura_elettronica_xml_get_archive_by_date_range_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_get_archive_by_date_range_options: Annotated[Optional[FatturaElettronicaXmlGetArchiveByDateRangeOptions], Field(description="Opzioni di download.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.

        Non è possibile scaricare più di 350 file alla volta.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_get_archive_by_date_range_options: Opzioni di download.
        :type fattura_elettronica_xml_get_archive_by_date_range_options: FatturaElettronicaXmlGetArchiveByDateRangeOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_get_archive_by_date_range_options=fattura_elettronica_xml_get_archive_by_date_range_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_get_archive_by_date_range_options: Annotated[Optional[FatturaElettronicaXmlGetArchiveByDateRangeOptions], Field(description="Opzioni di download.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.

        Non è possibile scaricare più di 350 file alla volta.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_get_archive_by_date_range_options: Opzioni di download.
        :type fattura_elettronica_xml_get_archive_by_date_range_options: FatturaElettronicaXmlGetArchiveByDateRangeOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_get_archive_by_date_range_options=fattura_elettronica_xml_get_archive_by_date_range_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post_serialize(
        self,
        version,
        company_id,
        fattura_elettronica_xml_get_archive_by_date_range_options,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_xml_get_archive_by_date_range_options is not None:
            _body_params = fattura_elettronica_xml_get_archive_by_date_range_options


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/zip'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/archivebydaterange',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_get_archive_by_file_name_options: Annotated[Optional[FatturaElettronicaXmlGetArchiveByFileNameOptions], Field(description="Opzioni di download.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Scarica un archivio ZIP di fatture XML, filtrate per nome file.

        Non è possibile scaricare più di 350 file alla volta.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_get_archive_by_file_name_options: Opzioni di download.
        :type fattura_elettronica_xml_get_archive_by_file_name_options: FatturaElettronicaXmlGetArchiveByFileNameOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_get_archive_by_file_name_options=fattura_elettronica_xml_get_archive_by_file_name_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_get_archive_by_file_name_options: Annotated[Optional[FatturaElettronicaXmlGetArchiveByFileNameOptions], Field(description="Opzioni di download.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Scarica un archivio ZIP di fatture XML, filtrate per nome file.

        Non è possibile scaricare più di 350 file alla volta.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_get_archive_by_file_name_options: Opzioni di download.
        :type fattura_elettronica_xml_get_archive_by_file_name_options: FatturaElettronicaXmlGetArchiveByFileNameOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_get_archive_by_file_name_options=fattura_elettronica_xml_get_archive_by_file_name_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_get_archive_by_file_name_options: Annotated[Optional[FatturaElettronicaXmlGetArchiveByFileNameOptions], Field(description="Opzioni di download.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Scarica un archivio ZIP di fatture XML, filtrate per nome file.

        Non è possibile scaricare più di 350 file alla volta.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_get_archive_by_file_name_options: Opzioni di download.
        :type fattura_elettronica_xml_get_archive_by_file_name_options: FatturaElettronicaXmlGetArchiveByFileNameOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_get_archive_by_file_name_options=fattura_elettronica_xml_get_archive_by_file_name_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post_serialize(
        self,
        version,
        company_id,
        fattura_elettronica_xml_get_archive_by_file_name_options,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_xml_get_archive_by_file_name_options is not None:
            _body_params = fattura_elettronica_xml_get_archive_by_file_name_options


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/zip'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/archivebyfilename',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_delete(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Elimina in blocco tutte le fatture XML dell'azienda.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_delete_serialize(
            company_id=company_id,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_delete_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Elimina in blocco tutte le fatture XML dell'azienda.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_delete_serialize(
            company_id=company_id,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_delete_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Elimina in blocco tutte le fatture XML dell'azienda.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_delete_serialize(
            company_id=company_id,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_bulk_delete_serialize(
        self,
        company_id,
        version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if version is not None:
            _path_params['version'] = version
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/bulk',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_get(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Scarica tutte le fatture XML come archivio ZIP.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_get_serialize(
            company_id=company_id,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_get_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Scarica tutte le fatture XML come archivio ZIP.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_get_serialize(
            company_id=company_id,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_get_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Scarica tutte le fatture XML come archivio ZIP.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_get_serialize(
            company_id=company_id,
            version=version,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_bulk_get_serialize(
        self,
        company_id,
        version,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if version is not None:
            _path_params['version'] = version
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/zip'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/bulk',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_post(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Archivio ZIP contenente i file XML.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Carica in blocco fatture XML da un archivio ZIP.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param file: Archivio ZIP contenente i file XML.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_post_serialize(
            company_id=company_id,
            version=version,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_post_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Archivio ZIP contenente i file XML.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Carica in blocco fatture XML da un archivio ZIP.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param file: Archivio ZIP contenente i file XML.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_post_serialize(
            company_id=company_id,
            version=version,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_bulk_post_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        version: StrictStr,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Archivio ZIP contenente i file XML.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Carica in blocco fatture XML da un archivio ZIP.


        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param version: (required)
        :type version: str
        :param file: Archivio ZIP contenente i file XML.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_bulk_post_serialize(
            company_id=company_id,
            version=version,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_bulk_post_serialize(
        self,
        company_id,
        version,
        file,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['companyId'] = company_id
        if version is not None:
            _path_params['version'] = version
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if file is not None:
            _files['file'] = file
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/bulk',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_export_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_export_options: Annotated[Optional[FatturaElettronicaExportOptions], Field(description="Opzioni di esportazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaExportResult:
        """Esporta uno o più documenti in una fattura XML.

        Tutti i documenti devono riferirsi alla stessa <a href=\"#tag/Anagrafica\">Anagrafica</a>.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_export_options: Opzioni di esportazione.
        :type fattura_elettronica_export_options: FatturaElettronicaExportOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_export_post_serialize(
            version=version,
            company_id=company_id,
            validation_override=validation_override,
            fattura_elettronica_export_options=fattura_elettronica_export_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaExportResult",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_export_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_export_options: Annotated[Optional[FatturaElettronicaExportOptions], Field(description="Opzioni di esportazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaExportResult]:
        """Esporta uno o più documenti in una fattura XML.

        Tutti i documenti devono riferirsi alla stessa <a href=\"#tag/Anagrafica\">Anagrafica</a>.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_export_options: Opzioni di esportazione.
        :type fattura_elettronica_export_options: FatturaElettronicaExportOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_export_post_serialize(
            version=version,
            company_id=company_id,
            validation_override=validation_override,
            fattura_elettronica_export_options=fattura_elettronica_export_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaExportResult",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_export_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_export_options: Annotated[Optional[FatturaElettronicaExportOptions], Field(description="Opzioni di esportazione.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Esporta uno o più documenti in una fattura XML.

        Tutti i documenti devono riferirsi alla stessa <a href=\"#tag/Anagrafica\">Anagrafica</a>.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_export_options: Opzioni di esportazione.
        :type fattura_elettronica_export_options: FatturaElettronicaExportOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_export_post_serialize(
            version=version,
            company_id=company_id,
            validation_override=validation_override,
            fattura_elettronica_export_options=fattura_elettronica_export_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaExportResult",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_export_post_serialize(
        self,
        version,
        company_id,
        validation_override,
        fattura_elettronica_export_options,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_export_options is not None:
            _body_params = fattura_elettronica_export_options


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/export',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[StrictStr, Field(description="Nome del file.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[AllegatoDocumento]:
        """Scarica i file allegati di una fattura XML.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file. (required)
        :type file_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AllegatoDocumento]",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[StrictStr, Field(description="Nome del file.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[AllegatoDocumento]]:
        """Scarica i file allegati di una fattura XML.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file. (required)
        :type file_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AllegatoDocumento]",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[StrictStr, Field(description="Nome del file.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Scarica i file allegati di una fattura XML.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file. (required)
        :type file_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[AllegatoDocumento]",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get_serialize(
        self,
        version,
        company_id,
        file_name,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        if file_name is not None:
            _path_params['fileName'] = file_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/{fileName}/attachments',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_file_name_get(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[StrictStr, Field(description="Nome del file.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Recupera una fattura XML per nome file.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file. (required)
        :type file_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_file_name_get_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_file_name_get_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[StrictStr, Field(description="Nome del file.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Recupera una fattura XML per nome file.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file. (required)
        :type file_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_file_name_get_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_file_name_get_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[StrictStr, Field(description="Nome del file.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Recupera una fattura XML per nome file.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file. (required)
        :type file_name: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_file_name_get_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_file_name_get_serialize(
        self,
        version,
        company_id,
        file_name,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        if file_name is not None:
            _path_params['fileName'] = file_name
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/xml'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/{fileName}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_get(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        skip_total_count: Annotated[Optional[StrictBool], Field(description="Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.")] = None,
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[FatturaElettronicaXml]:
        """Restituisce una lista di elementi.

         La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param skip: Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param skip_total_count: Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.
        :type skip_total_count: bool
        :param filter: Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.
        :type filter: str
        :param order: Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.
        :type order: str
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_get_serialize(
            version=version,
            company_id=company_id,
            skip=skip,
            take=take,
            skip_total_count=skip_total_count,
            filter=filter,
            order=order,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaXml]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_get_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        skip_total_count: Annotated[Optional[StrictBool], Field(description="Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.")] = None,
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[FatturaElettronicaXml]]:
        """Restituisce una lista di elementi.

         La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param skip: Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param skip_total_count: Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.
        :type skip_total_count: bool
        :param filter: Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.
        :type filter: str
        :param order: Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.
        :type order: str
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_get_serialize(
            version=version,
            company_id=company_id,
            skip=skip,
            take=take,
            skip_total_count=skip_total_count,
            filter=filter,
            order=order,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaXml]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_get_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        skip: Annotated[Optional[StrictInt], Field(description="Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.")] = None,
        take: Annotated[Optional[StrictInt], Field(description="Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.")] = None,
        skip_total_count: Annotated[Optional[StrictBool], Field(description="Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.")] = None,
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce una lista di elementi.

         La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param skip: Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione.
        :type skip: int
        :param take: Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione.
        :type take: int
        :param skip_total_count: Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`.
        :type skip_total_count: bool
        :param filter: Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`.
        :type filter: str
        :param order: Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`.
        :type order: str
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_get_serialize(
            version=version,
            company_id=company_id,
            skip=skip,
            take=take,
            skip_total_count=skip_total_count,
            filter=filter,
            order=order,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaXml]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_get_serialize(
        self,
        version,
        company_id,
        skip,
        take,
        skip_total_count,
        filter,
        order,
        expand,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'Expand': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if skip is not None:
            
            _query_params.append(('Skip', skip))
            
        if take is not None:
            
            _query_params.append(('Take', take))
            
        if skip_total_count is not None:
            
            _query_params.append(('SkipTotalCount', skip_total_count))
            
        if filter is not None:
            
            _query_params.append(('Filter', filter))
            
        if order is not None:
            
            _query_params.append(('Order', order))
            
        if expand is not None:
            
            _query_params.append(('Expand', expand))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_delete(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da eliminare.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaXml:
        """Elimina un elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da eliminare. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_delete_serialize(
            version=version,
            company_id=company_id,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_delete_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da eliminare.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaXml]:
        """Elimina un elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da eliminare. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_delete_serialize(
            version=version,
            company_id=company_id,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_delete_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da eliminare.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Elimina un elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da eliminare. (required)
        :type id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_delete_serialize(
            version=version,
            company_id=company_id,
            id=id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_id_delete_serialize(
        self,
        version,
        company_id,
        id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_get(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da recuperare.")],
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaXml:
        """Restituisce un elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da recuperare. (required)
        :type id: int
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_get_serialize(
            version=version,
            company_id=company_id,
            id=id,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_get_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da recuperare.")],
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaXml]:
        """Restituisce un elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da recuperare. (required)
        :type id: int
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_get_serialize(
            version=version,
            company_id=company_id,
            id=id,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_get_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID dell'elemento da recuperare.")],
        expand: Annotated[Optional[List[StrictStr]], Field(description="Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce un elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID dell'elemento da recuperare. (required)
        :type id: int
        :param expand: Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata.
        :type expand: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_get_serialize(
            version=version,
            company_id=company_id,
            id=id,
            expand=expand,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_id_get_serialize(
        self,
        version,
        company_id,
        id,
        expand,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'Expand': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('Expand', expand))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_put(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID univoco dell'elemento da aggiornare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_xml: Annotated[Optional[FatturaElettronicaXml], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaXml:
        """Aggiorna un elemento esistente.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID univoco dell'elemento da aggiornare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_xml: Istanza dell'elemento da salvare.
        :type fattura_elettronica_xml: FatturaElettronicaXml
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_put_serialize(
            version=version,
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            fattura_elettronica_xml=fattura_elettronica_xml,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '422': "ProblemDetails",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_put_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID univoco dell'elemento da aggiornare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_xml: Annotated[Optional[FatturaElettronicaXml], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaXml]:
        """Aggiorna un elemento esistente.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID univoco dell'elemento da aggiornare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_xml: Istanza dell'elemento da salvare.
        :type fattura_elettronica_xml: FatturaElettronicaXml
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_put_serialize(
            version=version,
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            fattura_elettronica_xml=fattura_elettronica_xml,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '422': "ProblemDetails",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_id_put_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        id: Annotated[StrictInt, Field(description="ID univoco dell'elemento da aggiornare.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_xml: Annotated[Optional[FatturaElettronicaXml], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Aggiorna un elemento esistente.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param id: ID univoco dell'elemento da aggiornare. (required)
        :type id: int
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_xml: Istanza dell'elemento da salvare.
        :type fattura_elettronica_xml: FatturaElettronicaXml
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_id_put_serialize(
            version=version,
            company_id=company_id,
            id=id,
            validation_override=validation_override,
            fattura_elettronica_xml=fattura_elettronica_xml,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '422': "ProblemDetails",
            '404': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_id_put_serialize(
        self,
        version,
        company_id,
        id,
        validation_override,
        fattura_elettronica_xml,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_xml is not None:
            _body_params = fattura_elettronica_xml


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_import_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        data_consegna_sdi: Annotated[Optional[datetime], Field(description="Data di consegna del Sistema di Interscambio (SdI).")] = None,
        identificativo_sdi: Annotated[Optional[StrictStr], Field(description="Identificativo assegnato dal Sistema di Interscambio (SdI).")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Contenuto del file.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[FatturaElettronicaImportResult]:
        """Importa una fattura XML.

        Viene creato un nuovo <a href=\"#tag/Documento\">Documento</a> corrispondente al contenuto XML.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param data_consegna_sdi: Data di consegna del Sistema di Interscambio (SdI).
        :type data_consegna_sdi: datetime
        :param identificativo_sdi: Identificativo assegnato dal Sistema di Interscambio (SdI).
        :type identificativo_sdi: str
        :param file: Contenuto del file.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_import_post_serialize(
            version=version,
            company_id=company_id,
            data_consegna_sdi=data_consegna_sdi,
            identificativo_sdi=identificativo_sdi,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_import_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        data_consegna_sdi: Annotated[Optional[datetime], Field(description="Data di consegna del Sistema di Interscambio (SdI).")] = None,
        identificativo_sdi: Annotated[Optional[StrictStr], Field(description="Identificativo assegnato dal Sistema di Interscambio (SdI).")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Contenuto del file.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[FatturaElettronicaImportResult]]:
        """Importa una fattura XML.

        Viene creato un nuovo <a href=\"#tag/Documento\">Documento</a> corrispondente al contenuto XML.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param data_consegna_sdi: Data di consegna del Sistema di Interscambio (SdI).
        :type data_consegna_sdi: datetime
        :param identificativo_sdi: Identificativo assegnato dal Sistema di Interscambio (SdI).
        :type identificativo_sdi: str
        :param file: Contenuto del file.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_import_post_serialize(
            version=version,
            company_id=company_id,
            data_consegna_sdi=data_consegna_sdi,
            identificativo_sdi=identificativo_sdi,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_import_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        data_consegna_sdi: Annotated[Optional[datetime], Field(description="Data di consegna del Sistema di Interscambio (SdI).")] = None,
        identificativo_sdi: Annotated[Optional[StrictStr], Field(description="Identificativo assegnato dal Sistema di Interscambio (SdI).")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Contenuto del file.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Importa una fattura XML.

        Viene creato un nuovo <a href=\"#tag/Documento\">Documento</a> corrispondente al contenuto XML.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param data_consegna_sdi: Data di consegna del Sistema di Interscambio (SdI).
        :type data_consegna_sdi: datetime
        :param identificativo_sdi: Identificativo assegnato dal Sistema di Interscambio (SdI).
        :type identificativo_sdi: str
        :param file: Contenuto del file.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_import_post_serialize(
            version=version,
            company_id=company_id,
            data_consegna_sdi=data_consegna_sdi,
            identificativo_sdi=identificativo_sdi,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_import_post_serialize(
        self,
        version,
        company_id,
        data_consegna_sdi,
        identificativo_sdi,
        file,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if data_consegna_sdi is not None:
            _form_params.append(('DataConsegnaSdi', data_consegna_sdi))
        if identificativo_sdi is not None:
            _form_params.append(('IdentificativoSdi', identificativo_sdi))
        if file is not None:
            _files['file'] = file
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/import',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_new_get(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaXml:
        """Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_new_get_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_new_get_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaXml]:
        """Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_new_get_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_new_get_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_new_get_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaXml",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_new_get_serialize(
        self,
        version,
        company_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/new',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_pair_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[Optional[StrictStr], Field(description="Nome del file.")] = None,
        progressivo: Annotated[Optional[StrictStr], Field(description="Progressivo del Sistema di Interscambio (SdI).")] = None,
        documento_id: Annotated[Optional[StrictInt], Field(description="Identificativo del Amica.Documento da abbinare.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Contenuto del file.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Associa una fattura XML a un documento esistente.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file.
        :type file_name: str
        :param progressivo: Progressivo del Sistema di Interscambio (SdI).
        :type progressivo: str
        :param documento_id: Identificativo del Amica.Documento da abbinare.
        :type documento_id: int
        :param file: Contenuto del file.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_pair_post_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            progressivo=progressivo,
            documento_id=documento_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_pair_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[Optional[StrictStr], Field(description="Nome del file.")] = None,
        progressivo: Annotated[Optional[StrictStr], Field(description="Progressivo del Sistema di Interscambio (SdI).")] = None,
        documento_id: Annotated[Optional[StrictInt], Field(description="Identificativo del Amica.Documento da abbinare.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Contenuto del file.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Associa una fattura XML a un documento esistente.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file.
        :type file_name: str
        :param progressivo: Progressivo del Sistema di Interscambio (SdI).
        :type progressivo: str
        :param documento_id: Identificativo del Amica.Documento da abbinare.
        :type documento_id: int
        :param file: Contenuto del file.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_pair_post_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            progressivo=progressivo,
            documento_id=documento_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_pair_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        file_name: Annotated[Optional[StrictStr], Field(description="Nome del file.")] = None,
        progressivo: Annotated[Optional[StrictStr], Field(description="Progressivo del Sistema di Interscambio (SdI).")] = None,
        documento_id: Annotated[Optional[StrictInt], Field(description="Identificativo del Amica.Documento da abbinare.")] = None,
        file: Annotated[Optional[Union[StrictBytes, StrictStr, Tuple[StrictStr, StrictBytes]]], Field(description="Contenuto del file.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Associa una fattura XML a un documento esistente.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param file_name: Nome del file.
        :type file_name: str
        :param progressivo: Progressivo del Sistema di Interscambio (SdI).
        :type progressivo: str
        :param documento_id: Identificativo del Amica.Documento da abbinare.
        :type documento_id: int
        :param file: Contenuto del file.
        :type file: bytearray
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_pair_post_serialize(
            version=version,
            company_id=company_id,
            file_name=file_name,
            progressivo=progressivo,
            documento_id=documento_id,
            file=file,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_pair_post_serialize(
        self,
        version,
        company_id,
        file_name,
        progressivo,
        documento_id,
        file,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if file_name is not None:
            _form_params.append(('FileName', file_name))
        if progressivo is not None:
            _form_params.append(('Progressivo', progressivo))
        if documento_id is not None:
            _form_params.append(('DocumentoId', documento_id))
        if file is not None:
            _files['file'] = file
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'multipart/form-data'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/pair',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_xml: Annotated[Optional[FatturaElettronicaXml], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaXml:
        """Salva un nuovo elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_xml: Istanza dell'elemento da salvare.
        :type fattura_elettronica_xml: FatturaElettronicaXml
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_post_serialize(
            version=version,
            company_id=company_id,
            validation_override=validation_override,
            fattura_elettronica_xml=fattura_elettronica_xml,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "FatturaElettronicaXml",
            '409': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_xml: Annotated[Optional[FatturaElettronicaXml], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaXml]:
        """Salva un nuovo elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_xml: Istanza dell'elemento da salvare.
        :type fattura_elettronica_xml: FatturaElettronicaXml
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_post_serialize(
            version=version,
            company_id=company_id,
            validation_override=validation_override,
            fattura_elettronica_xml=fattura_elettronica_xml,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "FatturaElettronicaXml",
            '409': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        validation_override: Annotated[Optional[StrictBool], Field(description="Se applicare eventualmente l'override della validazione.")] = None,
        fattura_elettronica_xml: Annotated[Optional[FatturaElettronicaXml], Field(description="Istanza dell'elemento da salvare.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Salva un nuovo elemento.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param validation_override: Se applicare eventualmente l'override della validazione.
        :type validation_override: bool
        :param fattura_elettronica_xml: Istanza dell'elemento da salvare.
        :type fattura_elettronica_xml: FatturaElettronicaXml
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_post_serialize(
            version=version,
            company_id=company_id,
            validation_override=validation_override,
            fattura_elettronica_xml=fattura_elettronica_xml,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "FatturaElettronicaXml",
            '409': "ProblemDetails",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_post_serialize(
        self,
        version,
        company_id,
        validation_override,
        fattura_elettronica_xml,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        if validation_override is not None:
            
            _query_params.append(('validationOverride', validation_override))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_xml is not None:
            _body_params = fattura_elettronica_xml


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[FatturaElettronicaImportResult]:
        """Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[FatturaElettronicaImportResult]]:
        """Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post_serialize(
        self,
        version,
        company_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/sdi/download/esiti',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[FatturaElettronicaImportResult]:
        """Scarica le nuove fatture dal Sistema di Interscambio (SDI).

        Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in !:ImpostazioniSdi.SdiApiKey.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[FatturaElettronicaImportResult]]:
        """Scarica le nuove fatture dal Sistema di Interscambio (SDI).

        Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in !:ImpostazioniSdi.SdiApiKey.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Scarica le nuove fatture dal Sistema di Interscambio (SDI).

        Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in !:ImpostazioniSdi.SdiApiKey.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post_serialize(
            version=version,
            company_id=company_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[FatturaElettronicaImportResult]",
            '400': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post_serialize(
        self,
        version,
        company_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/sdi/download/fatture',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_upload_options: Annotated[Optional[FatturaElettronicaUploadOptions], Field(description="Opzioni di invio.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> FatturaElettronicaUploadResult:
        """Invia una o più fatture al Sistema di Interscambio (SDI).

        Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in !:ImpostazioniSdi.SdiApiKey.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_upload_options: Opzioni di invio.
        :type fattura_elettronica_upload_options: FatturaElettronicaUploadOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_upload_options=fattura_elettronica_upload_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaUploadResult",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_upload_options: Annotated[Optional[FatturaElettronicaUploadOptions], Field(description="Opzioni di invio.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[FatturaElettronicaUploadResult]:
        """Invia una o più fatture al Sistema di Interscambio (SDI).

        Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in !:ImpostazioniSdi.SdiApiKey.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_upload_options: Opzioni di invio.
        :type fattura_elettronica_upload_options: FatturaElettronicaUploadOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_upload_options=fattura_elettronica_upload_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaUploadResult",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_upload_options: Annotated[Optional[FatturaElettronicaUploadOptions], Field(description="Opzioni di invio.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Invia una o più fatture al Sistema di Interscambio (SDI).

        Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in !:ImpostazioniSdi.SdiApiKey.

        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_upload_options: Opzioni di invio.
        :type fattura_elettronica_upload_options: FatturaElettronicaUploadOptions
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_upload_options=fattura_elettronica_upload_options,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "FatturaElettronicaUploadResult",
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post_serialize(
        self,
        version,
        company_id,
        fattura_elettronica_upload_options,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_upload_options is not None:
            _body_params = fattura_elettronica_upload_options


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/sdi/upload',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_stylesheet_post(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_style_sheet_data: Annotated[Optional[FatturaElettronicaXmlStyleSheetData], Field(description="Opzioni di corrispondenza e stile.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_style_sheet_data: Opzioni di corrispondenza e stile.
        :type fattura_elettronica_xml_style_sheet_data: FatturaElettronicaXmlStyleSheetData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_stylesheet_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_style_sheet_data=fattura_elettronica_xml_style_sheet_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_stylesheet_post_with_http_info(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_style_sheet_data: Annotated[Optional[FatturaElettronicaXmlStyleSheetData], Field(description="Opzioni di corrispondenza e stile.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_style_sheet_data: Opzioni di corrispondenza e stile.
        :type fattura_elettronica_xml_style_sheet_data: FatturaElettronicaXmlStyleSheetData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_stylesheet_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_style_sheet_data=fattura_elettronica_xml_style_sheet_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def api_vversion_company_id_fattura_elettronica_xml_stylesheet_post_without_preload_content(
        self,
        version: Annotated[StrictStr, Field(description="Versione API.")],
        company_id: Annotated[StrictStr, Field(description="ID univoco dell'azienda.")],
        fattura_elettronica_xml_style_sheet_data: Annotated[Optional[FatturaElettronicaXmlStyleSheetData], Field(description="Opzioni di corrispondenza e stile.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.


        :param version: Versione API. (required)
        :type version: str
        :param company_id: ID univoco dell'azienda. (required)
        :type company_id: str
        :param fattura_elettronica_xml_style_sheet_data: Opzioni di corrispondenza e stile.
        :type fattura_elettronica_xml_style_sheet_data: FatturaElettronicaXmlStyleSheetData
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._api_vversion_company_id_fattura_elettronica_xml_stylesheet_post_serialize(
            version=version,
            company_id=company_id,
            fattura_elettronica_xml_style_sheet_data=fattura_elettronica_xml_style_sheet_data,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': None,
            '400': "ProblemDetails",
            '404': "ProblemDetails",
            '429': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _api_vversion_company_id_fattura_elettronica_xml_stylesheet_post_serialize(
        self,
        version,
        company_id,
        fattura_elettronica_xml_style_sheet_data,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if version is not None:
            _path_params['version'] = version
        if company_id is not None:
            _path_params['companyId'] = company_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if fattura_elettronica_xml_style_sheet_data is not None:
            _body_params = fattura_elettronica_xml_style_sheet_data


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/xml'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'bearer', 
            'oauth2', 
            'oauth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/api/v{version}/{companyId}/FatturaElettronicaXml/stylesheet',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


