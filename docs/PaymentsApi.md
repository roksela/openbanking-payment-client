# openbanking_payment_client.PaymentsApi

All URIs are relative to *https://localhost/open-banking/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_submission**](PaymentsApi.md#create_payment_submission) | **POST** /payment-submissions | Create a payment submission
[**create_single_immediate_payment**](PaymentsApi.md#create_single_immediate_payment) | **POST** /payments | Create a single immediate payment
[**get_payment_submission**](PaymentsApi.md#get_payment_submission) | **GET** /payment-submissions/{PaymentSubmissionId} | Get a payment submission
[**get_single_immediate_payment**](PaymentsApi.md#get_single_immediate_payment) | **GET** /payments/{PaymentId} | Get a single immediate payment


# **create_payment_submission**
> PaymentSubmitPOST201Response create_payment_submission(x_idempotency_key, x_fapi_financial_id, authorization, body, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_jws_signature=x_jws_signature)

Create a payment submission

Submit a previously setup payment

### Example
```python
from __future__ import print_function
import time
import openbanking_payment_client
from openbanking_payment_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PSUOAuth2Security
configuration = openbanking_payment_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openbanking_payment_client.PaymentsApi(openbanking_payment_client.ApiClient(configuration))
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_idempotency_key** | **str**| Every request will be processed only once per x-idempotency-key.  The Idempotency Key will be valid for 24 hours. | 
 **x_fapi_financial_id** | **str**| The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB. | 
 **authorization** | **str**| An Authorisation Token as per https://tools.ietf.org/html/rfc6750 | 
 **body** | [**PaymentSubmissionPOSTRequest**](PaymentSubmissionPOSTRequest.md)| Setup a single immediate payment | 
 **x_fapi_customer_last_logged_time** | **str**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **x_fapi_interaction_id** | **str**| An RFC4122 UID used as a correlation id. | [optional] 
 **x_jws_signature** | **str**| DO NOT USE. Header containing a detached JWS signature of the body of the payload. | [optional] 

### Return type

[**PaymentSubmitPOST201Response**](PaymentSubmitPOST201Response.md)

### Authorization

[PSUOAuth2Security](../README.md#PSUOAuth2Security)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_single_immediate_payment**
> PaymentSetupPOSTResponse create_single_immediate_payment(x_idempotency_key, x_fapi_financial_id, authorization, body, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_jws_signature=x_jws_signature)

Create a single immediate payment

Create a single immediate payment

### Example
```python
from __future__ import print_function
import time
import openbanking_payment_client
from openbanking_payment_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: TPPOAuth2Security
configuration = openbanking_payment_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openbanking_payment_client.PaymentsApi(openbanking_payment_client.ApiClient(configuration))
x_idempotency_key = 'x_idempotency_key_example' # str | Every request will be processed only once per x-idempotency-key.  The Idempotency Key will be valid for 24 hours.
x_fapi_financial_id = 'x_fapi_financial_id_example' # str | The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB.
authorization = 'authorization_example' # str | An Authorisation Token as per https://tools.ietf.org/html/rfc6750
body = openbanking_payment_client.PaymentSetupPOSTRequest() # PaymentSetupPOSTRequest | Setup a single immediate payment
x_fapi_customer_last_logged_time = 'x_fapi_customer_last_logged_time_example' # str | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The PSU's IP address if the PSU is currently logged in with the TPP. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An RFC4122 UID used as a correlation id. (optional)
x_jws_signature = 'x_jws_signature_example' # str | DO NOT USE. Header containing a detached JWS signature of the body of the payload. (optional)

try:
    # Create a single immediate payment
    api_response = api_instance.create_single_immediate_payment(x_idempotency_key, x_fapi_financial_id, authorization, body, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id, x_jws_signature=x_jws_signature)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_single_immediate_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_idempotency_key** | **str**| Every request will be processed only once per x-idempotency-key.  The Idempotency Key will be valid for 24 hours. | 
 **x_fapi_financial_id** | **str**| The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB. | 
 **authorization** | **str**| An Authorisation Token as per https://tools.ietf.org/html/rfc6750 | 
 **body** | [**PaymentSetupPOSTRequest**](PaymentSetupPOSTRequest.md)| Setup a single immediate payment | 
 **x_fapi_customer_last_logged_time** | **str**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **x_fapi_interaction_id** | **str**| An RFC4122 UID used as a correlation id. | [optional] 
 **x_jws_signature** | **str**| DO NOT USE. Header containing a detached JWS signature of the body of the payload. | [optional] 

### Return type

[**PaymentSetupPOSTResponse**](PaymentSetupPOSTResponse.md)

### Authorization

[TPPOAuth2Security](../README.md#TPPOAuth2Security)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_submission**
> PaymentSubmitPOST201Response get_payment_submission(payment_submission_id, x_fapi_financial_id, authorization, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id)

Get a payment submission

Get payment submission

### Example
```python
from __future__ import print_function
import time
import openbanking_payment_client
from openbanking_payment_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PSUOAuth2Security
configuration = openbanking_payment_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: TPPOAuth2Security
configuration = openbanking_payment_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openbanking_payment_client.PaymentsApi(openbanking_payment_client.ApiClient(configuration))
payment_submission_id = 'payment_submission_id_example' # str | Unique identification as assigned by the ASPSP to uniquely identify the payment submission resource.
x_fapi_financial_id = 'x_fapi_financial_id_example' # str | The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB.
authorization = 'authorization_example' # str | An Authorisation Token as per https://tools.ietf.org/html/rfc6750
x_fapi_customer_last_logged_time = 'x_fapi_customer_last_logged_time_example' # str | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The PSU's IP address if the PSU is currently logged in with the TPP. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An RFC4122 UID used as a correlation id. (optional)

try:
    # Get a payment submission
    api_response = api_instance.get_payment_submission(payment_submission_id, x_fapi_financial_id, authorization, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_submission_id** | **str**| Unique identification as assigned by the ASPSP to uniquely identify the payment submission resource. | 
 **x_fapi_financial_id** | **str**| The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB. | 
 **authorization** | **str**| An Authorisation Token as per https://tools.ietf.org/html/rfc6750 | 
 **x_fapi_customer_last_logged_time** | **str**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **x_fapi_interaction_id** | **str**| An RFC4122 UID used as a correlation id. | [optional] 

### Return type

[**PaymentSubmitPOST201Response**](PaymentSubmitPOST201Response.md)

### Authorization

[PSUOAuth2Security](../README.md#PSUOAuth2Security), [TPPOAuth2Security](../README.md#TPPOAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_single_immediate_payment**
> PaymentSetupPOSTResponse get_single_immediate_payment(payment_id, x_fapi_financial_id, authorization, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id)

Get a single immediate payment

Get a single immediate payment

### Example
```python
from __future__ import print_function
import time
import openbanking_payment_client
from openbanking_payment_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PSUOAuth2Security
configuration = openbanking_payment_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: TPPOAuth2Security
configuration = openbanking_payment_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = openbanking_payment_client.PaymentsApi(openbanking_payment_client.ApiClient(configuration))
payment_id = 'payment_id_example' # str | Unique identification as assigned by the ASPSP to uniquely identify the payment setup resource.
x_fapi_financial_id = 'x_fapi_financial_id_example' # str | The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB.
authorization = 'authorization_example' # str | An Authorisation Token as per https://tools.ietf.org/html/rfc6750
x_fapi_customer_last_logged_time = 'x_fapi_customer_last_logged_time_example' # str | The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC (optional)
x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The PSU's IP address if the PSU is currently logged in with the TPP. (optional)
x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An RFC4122 UID used as a correlation id. (optional)

try:
    # Get a single immediate payment
    api_response = api_instance.get_single_immediate_payment(payment_id, x_fapi_financial_id, authorization, x_fapi_customer_last_logged_time=x_fapi_customer_last_logged_time, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_fapi_interaction_id=x_fapi_interaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_single_immediate_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Unique identification as assigned by the ASPSP to uniquely identify the payment setup resource. | 
 **x_fapi_financial_id** | **str**| The unique id of the ASPSP to which the request is issued. The unique id will be issued by OB. | 
 **authorization** | **str**| An Authorisation Token as per https://tools.ietf.org/html/rfc6750 | 
 **x_fapi_customer_last_logged_time** | **str**| The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC | [optional] 
 **x_fapi_customer_ip_address** | **str**| The PSU&#39;s IP address if the PSU is currently logged in with the TPP. | [optional] 
 **x_fapi_interaction_id** | **str**| An RFC4122 UID used as a correlation id. | [optional] 

### Return type

[**PaymentSetupPOSTResponse**](PaymentSetupPOSTResponse.md)

### Authorization

[PSUOAuth2Security](../README.md#PSUOAuth2Security), [TPPOAuth2Security](../README.md#TPPOAuth2Security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

