# PaymentSetupResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | OB: Unique identification as assigned by the ASPSP to uniquely identify the payment setup resource. | 
**status** | **str** | Specifies the status of the payment resource. | [optional] 
**creation_date_time** | **datetime** | Date and time at which the resource was created.  All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | 
**initiation** | [**PaymentSetupResponseInitiation**](PaymentSetupResponseInitiation.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


