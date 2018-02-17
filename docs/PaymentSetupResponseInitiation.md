# PaymentSetupResponseInitiation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instruction_identification** | **str** | Unique identification as assigned by an instructing party for an instructed party to unambiguously identify the instruction. Usage: the  instruction identification is a point to point reference that can be used between the instructing party and the instructed party to refer to the individual instruction. It can be included in several messages related to the instruction. | 
**end_to_end_identification** | **str** | Unique identification assigned by the initiating party to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain. Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the transaction. It can be included in several messages related to the transaction. OB: The Faster Payments Scheme can only access 31 characters for the EndToEndIdentification field. | 
**instructed_amount** | [**PaymentSetupInitiationInstructedAmount**](PaymentSetupInitiationInstructedAmount.md) |  | 
**debtor_agent** | [**DebtorAgent**](DebtorAgent.md) |  | [optional] 
**debtor_account** | [**DebtorAccount**](DebtorAccount.md) |  | [optional] 
**creditor_agent** | [**CreditorAgent**](CreditorAgent.md) |  | [optional] 
**creditor_account** | [**CreditorAccount**](CreditorAccount.md) |  | 
**remittance_information** | [**RemittanceInformation**](RemittanceInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


