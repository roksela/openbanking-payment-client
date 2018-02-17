# openbanking-payment-client
Python client for Payment Initiation API. It allows to initiate payments from personal and business current accounts.

## API Specification

https://www.openbanking.org.uk/read-write-apis/

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/roksela/openbanking-payment-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/roksela/openbanking-payment-client.git`)

Then import the package:
```python
import openbanking_payment_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openbanking_payment_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openbanking_payment_client
from openbanking_payment_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PSUOAuth2Security
openbanking_payment_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = openbanking_payment_client.PaymentsApi()
x_idempotency_key = 'x_idempotency_key_example' # str | Every request will be processed only once per x-idempotency-key.  The Idempotency Key will be valid for 24 hours.
x_fapi_financial_id = 'x_fapi_financial_id_example' # str | The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB.
authorization = 'authorization_example' # str | An Authorisation Token as per https://tools.ietf.org/html/rfc6750
body = openbanking_payment_client.PaymentSubmissionPOSTRequest() # PaymentSubmissionPOSTRequest | Setup a single immediate payment
x_fapi_customer_last_logged_time = 'x_fapi_customer_last_logged_time_example' # str | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The PSU's IP address if the PSU is currently logged in with the TPP. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An RFC4122 UID used as a correlation id. (optional)
x_jws_signature = 'x_jws_signature_example' # str | DO NOT USE. Header containing a detached JWS signature of the body of the payload. (optional)

try:
    # Create a payment submission
    api_response = api_instance.create_payment_submission(x_idempotency_key, x_fapi_financial_id, authorization, body, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_jws_signature=x_jws_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment_submission: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/open-banking/v1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PaymentsApi* | [**create_payment_submission**](docs/PaymentsApi.md#create_payment_submission) | **POST** /payment-submissions | Create a payment submission
*PaymentsApi* | [**create_single_immediate_payment**](docs/PaymentsApi.md#create_single_immediate_payment) | **POST** /payments | Create a single immediate payment
*PaymentsApi* | [**get_payment_submission**](docs/PaymentsApi.md#get_payment_submission) | **GET** /payment-submissions/{PaymentSubmissionId} | Get a payment submission
*PaymentsApi* | [**get_single_immediate_payment**](docs/PaymentsApi.md#get_single_immediate_payment) | **GET** /payments/{PaymentId} | Get a single immediate payment


## Documentation For Models

 - [CreditorAccount](docs/CreditorAccount.md)
 - [CreditorAgent](docs/CreditorAgent.md)
 - [DebtorAccount](docs/DebtorAccount.md)
 - [DebtorAgent](docs/DebtorAgent.md)
 - [PaymentSetup](docs/PaymentSetup.md)
 - [PaymentSetupInitiation](docs/PaymentSetupInitiation.md)
 - [PaymentSetupInitiationInstructedAmount](docs/PaymentSetupInitiationInstructedAmount.md)
 - [PaymentSetupPOSTRequest](docs/PaymentSetupPOSTRequest.md)
 - [PaymentSetupPOSTResponse](docs/PaymentSetupPOSTResponse.md)
 - [PaymentSetupPOSTResponseLinks](docs/PaymentSetupPOSTResponseLinks.md)
 - [PaymentSetupPOSTResponseMeta](docs/PaymentSetupPOSTResponseMeta.md)
 - [PaymentSetupResponse](docs/PaymentSetupResponse.md)
 - [PaymentSetupResponse1](docs/PaymentSetupResponse1.md)
 - [PaymentSetupResponseInitiation](docs/PaymentSetupResponseInitiation.md)
 - [PaymentSubmission](docs/PaymentSubmission.md)
 - [PaymentSubmissionPOSTRequest](docs/PaymentSubmissionPOSTRequest.md)
 - [PaymentSubmitPOST201Response](docs/PaymentSubmitPOST201Response.md)
 - [RemittanceInformation](docs/RemittanceInformation.md)
 - [Risk](docs/Risk.md)
 - [Risk1](docs/Risk1.md)
 - [RiskDeliveryAddress](docs/RiskDeliveryAddress.md)


## Documentation For Authorization


## PSUOAuth2Security

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authserver.example/authorization
- **Scopes**: 
 - **payments**: Generic payment scope

## TPPOAuth2Security

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **payments**: Generic payment scope

## Code Generator

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.1.1
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

