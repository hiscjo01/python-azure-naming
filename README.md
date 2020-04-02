
RBA Naming Conventions for Azure
================================

# Overview


This is the overview section.  Blah blah blahmore blah blah
# RBA Entities


This can describe the purpose for the RBA entities. It is meant asa placeholder for whatever we want to say about them.
## rba.azureRegion

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Central US|global|az[7]|uscent1|
|East US|global|az[7]|useast1|
|East US 2|global|az[7]|useast2|
|North Central US|global|az[7]|usnoce1|
|South Central US|global|az[7]|ussoce1|
|West US 2|global|az[7]|uswest2|
|West Central US|global|az[7]|uswece1|
|West US|global|az[7]|uswest1|
|US DoD Central|global|az[7]|docent1|
|US DoD East|global|az[7]|doeast1|
|US Gov Arizona|global|az[7]|gvariz1|
|US Gov Virginia|global|az[7]|gvvirg1|
|US Gov Texas|global|az[7]|gvtexs1|
|US Gov Iowa|global|az[7]|gviowa1|
|US Sec East|global|az[7]|sceast1|
|US Sec West|global|az[7]|scwest1|
|Canada Central|global|az[7]|cacent1|
|Canada East|global|az[7]|caeast1|
|Brazil South|global|az[7]|brsout1|
|Mexico Central|global|az[7]|mxcent1|
|North Europe|global|az[7]|eunort1|
|West Europe|global|az[7]|euwest1|
|France Central|global|az[7]|frcent1|
|France South|global|az[7]|frsout1|
|UK South|global|az[7]|gbsout1|
|UK West|global|az[7]|gbwest1|
|Germany North|global|az[7]|denort1|
|Germany West Central|global|az[7]|dewece1|
|Germany Northeast|global|az[7]|denoea1|
|Germany Central|global|az[7]|decent1|
|Switzerland North|global|az[7]|chnort1|
|Switzerland West|global|az[7]|chwest1|
|Norway West|global|az[7]|nowest1|
|â€‹Norway East|global|az[7]|noeast1|
|Spain Central|global|az[7]|escent1|
|East Asia|global|az[7]|aseast1|
|Southeast Asia|global|az[7]|assoea1|
|Australia Central|global|az[7]|aucent1|
|Australia Central 2|global|az[7]|aucent2|
|Australia East|global|az[7]|aueast1|
|Australia Southeast|global|az[7]|ausoea1|
|â€‹China East|global|az[7]|cneast1|
|China North|global|az[7]|cnnort1|
|China East 2|global|az[7]|cneast1|
|China North 2|global|az[7]|cnnort1|
|Central India|global|az[7]|incent1|
|West India|global|az[7]|inwest1|
|South India|global|az[7]|insout1|
|Japan East|global|az[7]|jpeast1|
|Japan West|global|az[7]|jpwest1|
|Korea Central|global|az[7]|krcent1|
|Korea South|global|az[7]|krsout1|
|South Africa North|global|az[7]|zanort1|
|South Africa West|global|az[7]|zawest1|
|Israel Central|global|az[7]|ilcent1|
|UAE Central|global|az[7]|aecent1|
|UAE North|global|az[7]|aenort1|
|Qatar Central|global|az[7]|qacent1|

## rba.businessUnit

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Business Services|global|az[12]|businesssvc|
|Insurance|global|az[12]|insurance|
|Healthcare|global|az[12]|healthcare|
|Government|global|az[12]|government|
|Infrastructure & Operations|global|az[12]|iog|
|Back Office|global|az[12]|backoffice|
|Data Science|global|az[12]|datasci|
|Linking|global|az[12]|linking|
|Data Engineering|global|az[12]|dataeng|
|Security|global|az[12]|security|
|HPCC Platform|global|az[12]|hpccplat|
|HPCC Systems|global|az[12]|hpccsyst|

## rba.environment

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Sandbox|global|az[7]|sandbox|
|Development|global|az[7]|dev|
|Testing (QA CERT)|global|az[7]|test|
|Staging|global|az[7]|staging|
|UAT (CT)|global|az[7]|uat|
|Production|global|az[7]|prod|
|Disaster Recovery|global|az[7]|dr|

## rba.market

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|United States|global|az[2]|us|
|United Kingdom|global|az[2]|uk|
|India|global|az[2]|in|
|Brazil|global|az[2]|br|
|China|global|az[2]|cn|

## rba.onPrem

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Boca Raton, FL, USA Datacenter 1|global|az[16]|bocadc1|
|Alpharetta GA, USA Datacenter 1|global|az[16]|alphadc1|
|King of Prussia, PA USA Office 1|global|az[16]|kingofprussia1|

## rba.productGroup

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Accurint Delivery Platform|global|az[12]|accurint|
|Bridger Delivery Platform|global|az[12]|bridger|
|Iyetek Delivery Platform|global|az[12]|iyetek|

## rba.productName

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Accurint Web Product|global|az[16]|accurintweb|
|Accurint API Product|global|az[16]|accurintapi|
|Accurint for Law Enforcement|global|az[16]|accurintle|

## rba.resourceGroupType

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Shared Services|global|az[12]|shared|
|Application|global|az[12]|app|

## rba.serviceName

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Esp for Accurint Web|global|az[12]|webesp|

## rba.subnetType

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Application Gateway|global|a-z[24]|azure-appgateway|
|VPN Gateway|global|a-z[24]|azure-vpngateway|
|Azure Firewall|global|a-z[24]|azure-firewall|
|Redis Cache|global|a-z[24]|azure-rediscache|
|Azure SQL Database|global|a-z[24]|azure-sqldatabase|
|Azure Container Instance|global|a-z[24]|azure-containers|
|API Management|global|a-z[24]|azure-apimanagement|
|App Service Environment|global|a-z[24]|azure-appservice|
|Azure Logic Apps|global|a-z[24]|azure-logicapps|
|Azure Dedicated HSM|global|a-z[24]|azure-dedicatedhsm|
|Azure Netapp Files|global|a-z[24]|azure-netappfiles|
|IaaS Public|global|a-z[24]|iaas-public|
|IaaS Outbound|global|a-z[24]|iaas-outbound|
|IaaS Private|global|a-z[24]|iaas-private|

## rba.subscriptionType

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Production|global|az[12]|production|
|Non-Production|global|az[12]|nonprod|

## rba.tagName

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Environment|global|a-z[24]|environment|
|Business Unit|global|a-z[24]|business-unit|

## rba.virtualNetGwType

|Full Text|Scope|Rule|Value|
| ------ | ------ | ------ | ------ |
|Express Route Connection|global|az[12]|expressroute|
|Virtual Private Network|global|az[12]|vpn|

# Azure Entities


This can describe the purpose for the custom entities. It is meant asa placeholder for whatever we want to say about them.
## azure.AnalysisServices

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|servers|resource group|a9[63]|||

## azure.ApiManagement

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|service|global|a9[50]|||
|api-version-sets|service|a-9[256]|||
|apis|service|a-9[256]|||
|issues|api|a-9[256]|||
|attachments|issue|a-9[256]|||
|comments|issue|a-9[256]|||
|operations|api|a-9[256]|||
|tags|operation|a-9[256]|||
|releases|api|a-9[80]|||
|schemas|api|a-9[256]|||
|tagDescriptions|api|a-9[256]|||
|tags|api|a-9[256]|||
|authorizationServers|service|a-9[256]|||
|backends|service|a-9[256]|||
|certificates|service|a-9[256]|||
|diagnostics|service|a-9[256]|||
|groups|service|a-9[256]|||
|users|group|a-9[256]|||
|identityProviders|service|a-9[256]|||
|loggers|service|a-9[256]|||
|notifications|service|a-9[256]|||
|recipientEmails|notification|a-9[256]|||
|openidConnectProviders|service|a-9[256]|||
|policies|service|a-9[256]|||
|products|service|a-9[256]|||
|apis|product|a-9[256]|||
|groups|product|a-9[256]|||
|tags|product|a-9[256]|||
|properties|service|a-9[256]|||
|subscriptions|service|a-9[256]|||
|tags|service|a-9[256]|||
|templates|service|a-9[256]|||
|users|service|a-9[256]|||

## azure.AppConfiguration

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|configurationStores|resource group|a-9[50]|||

## azure.Authorization

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|locks|scope of assignment|a-9[90]|||
|policySetDefinitions|scope of definition|a-9[255]|||
|policyassignments|scope of assignment|a-9[255]|||
|policydefinitions|scope of definition|a-9[255]|||

## azure.Automation

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|automationAccounts|resource group|a-9[50]|||
|certificates|automation account|a-9[128]|||
|connections|automation account|a-9[128]|||
|credentials|automation account|a-9[128]|||
|runbooks|automation account|a-9[63]|||
|schedules|automation account|a-9[128]|||
|variables|automation account|a-9[128]|||
|watchers|automation account|a-9[63]|||
|webhooks|automation account|a-9[128]|||

## azure.Batch

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|batchAccounts|Region|a9[24]|||
|applications|batch account|a-9[64]|||
|certificates|batch account|a-9[45]|||
|pools|batch account|a-9[64]|||

## azure.Blockchain

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|blockchainMembers|global|a9[20]|||

## azure.BotService

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|botServices|global|a-9[64]|||
|Connections|bot service|a-9[64]|||
|channels|bot service|a-9[64]|||
|enterpriseChannels|resource group|a-9[64]|||

## azure.Cache

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|Redis|global|a-9[63]|||
|firewallRules|Redis|a9[256]|||

## azure.Cdn

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|profiles|resource group|a-9[260]|||
|endpoints|global|a-9[50]|||

## azure.CertificateRegistration

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|certificateOrders|resource group|a9[30]|||

## azure.CognitiveServices

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|accounts|resource group|a-9[64]|||

## azure.Compute

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|availabilitySets|resource group|a-9[80]|||
|diskEncryptionSets|resource group|a9[80]|||
|disks|resource group|a9[80]|||
|galleries|resource group|a9[80]|||
|applications|gallery|a-9[80]|||
|versions|application|0.9[64]|||
|images|gallery|a-9[80]|||
|versions|image|0.9[64]|||
|images|resource group|a-9[80]|||
|snapshots|resource group|a-9[80]|||
|virtualMachineScaleSets|resource group|a-9[64]|||
|virtualMachines|resource group|a-9[64]|||

## azure.ContainerInstance

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|containerGroups|resource group|a-9[63]|||

## azure.ContainerRegistry

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|registries|global|a9[50]|||
|buildTasks|registry|a9[50]|||
|steps|build task|a9[50]|||
|replications|registry|a9[50]|||
|scopeMaps|registry|a-9[50]|||
|tasks|registry|a-9[50]|||
|tokens|registry|a-9[50]|||
|webhooks|registry|a9[50]|||

## azure.ContainerService

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|managedClusters|resource group|a-9[63]|||
|openShiftManagedClusters|resource group|a9[30]|||

## azure.CustomProviders

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|associations|resource group|a-9[180]|||
|resourceProviders|resource group|a-9[64]|||

## azure.CustomerInsights

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|hubs|resource group|a9[64]|||
|authorizationPolicies|hub|a9[50]|||
|connectors|hub|a9[128]|||
|mappings|connector|a9[128]|||
|interactions|hub|a9[128]|||
|kpi|hub|a9[512]|||
|links|hub|a9[512]|||
|predictions|hub|a9[512]|||
|profiles|hub|a9[128]|||
|relationshipLinks|hub|a9[512]|||
|relationships|hub|a9[512]|||
|roleAssignments|hub|a9[128]|||
|views|hub|a9[512]|||

## azure.DBforMariaDB

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|servers|global|a-9[63]|||
|databases|servers|a-9[63]|||
|firewallRules|servers|a-9[128]|||
|virtualNetworkRules|servers|a-9[128]|||

## azure.DBforMySQL

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|servers|global|a-9[63]|||
|databases|servers|a-9[63]|||
|firewallRules|servers|a-9[128]|||
|virtualNetworkRules|servers|a-9[128]|||

## azure.DBforPostgreSQL

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|servers|global|a-9[63]|||
|databases|servers|a-9[63]|||
|firewallRules|servers|a-9[128]|||
|virtualNetworkRules|servers|a-9[128]|||

## azure.DataBox

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|jobs|resource group|a-9[24]|||

## azure.DataFactory

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|factories|global|a-9[63]|||
|dataflows|factory|a-9[260]|||
|datasets|factory|a-9[260]|||
|integrationRuntimes|factory|a-9[63]|||
|linkedservices|factory|a-9[260]|||
|pipelines|factory|a-9[260]|||
|triggers|factory|a-9[260]|||
|rerunTriggers|trigger|a-9[260]|||

## azure.DataLakeAnalytics

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|accounts|global|a9[24]|||
|computePolicies|account|a-9[60]|||
|dataLakeStoreAccounts|account|a9[24]|||
|firewallRules|account|a-9[50]|||
|storageAccounts|account|a-9[60]|||

## azure.DataLakeStore

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|accounts|global|a9[24]|||
|firewallRules|account|a-9[50]|||
|virtualNetworkRules|account|a-9[50]|||

## azure.DataMigration

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|services|resource group|a-9[62]|||
|projects|service|a-9[57]|||

## azure.Databricks

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|workspaces|resource group|a-9[30]|||

## azure.DevTestLab

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|labs|resource group|a-9[50]|||
|customimages|lab|a-9[80]|||
|formulas|lab|a-9[80]|||
|virtualmachines|lab|a-9[64]|||

## azure.Devices

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|IotHubs|global|a-9[50]|||
|certificates|IoT hub|a-9[64]|||
|ConsumerGroups|eventHubEndpoints|a-9[50]|||
|provisioningServices|resource group|a-9[64]|||
|certificates|provisioningServices|a-9[64]|||

## azure.DocumentDB

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|databaseAccounts|global|a-9[31]|||

## azure.EventGrid

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|domains|resource group|a-9[50]|||
|topics|domain|a-9[50]|||
|eventSubscriptions|resource group|a-9[64]|||
|topics|resource group|a-9[50]|||

## azure.EventHub

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|clusters|resource group|a-9[50]|||
|namespaces|global|a-9[50]|||
|AuthorizationRules|namespace|a-9[50]|||
|disasterRecoveryConfigs|namespace|a-9[50]|||
|eventhubs|namespace|a-9[50]|||
|authorizationRules|event hub|a-9[50]|||
|consumergroups|event hub|a-9[50]|||

## azure.HDInsight

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|clusters|global|a-9[59]|||

## azure.ImportExport

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|jobs|resource group|a-9[64]|||

## azure.IoTCentral

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|IoTApps|global|a-9[63]|||

## azure.KeyVault

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|vaults|global|a-9[24]|||
|secrets|Vault|a-9[127]|||

## azure.Kusto

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|databases|cluster|a-9[260]|||
|dataConnections|database|a-9[40]|||
|eventhubconnections|database|a-9[40]|||
|clusters|global|a9[22]|||

## azure.Logic

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|integrationAccounts|resource group|a-9[80]|||
|assemblies|integration account|a-9[80]|||
|batchConfigurations|integration account|a9[20]|||
|certificates|integration account|a-9[80]|||
|maps|integration account|a-9[80]|||
|partners|integration account|a-9[80]|||
|rosettanetprocessconfigurations|integration account|a-9[80]|||
|schemas|integration account|a-9[80]|||
|sessions|integration account|a-9[80]|||
|integrationServiceEnvironments|resource group|a-9[80]|||
|managedApis|integration service environment|a-9[80]|||
|workflows|resource group|a-9[80]|||

## azure.MachineLearning

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|commitmentPlans|resource group|a-9[260]|||
|webServices|resource group|a-9[260]|||
|workspaces|resource group|a-9[260]|||

## azure.MachineLearningServices

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|workspaces|resource group|a-9[33]|||
|computes|workspace|a-9[16]|||

## azure.ManagedIdentity

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|userAssignedIdentities|resource group|a-9[128]|||

## azure.Maps

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|accounts|resource group|a-9[98]|||

## azure.Media

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|mediaservices|resource group|a9[24]|||
|liveEvents|Media service|a-9[32]|||
|liveOutputs|Live event|a-9[256]|||
|streamingEndpoints|Media service|a-9[24]|||

## azure.Network

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|applicationGateways|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-<[rba.azureRegion[7]](README.md#rbaazureRegion)>-appgateway<##>|accurint-production-useast2-appgateway01|
|applicationSecurityGroups|resource group|a-9[80]|<[rba.serviceName[12]](README.md#rbaserviceName)>-app-security-group<##>|webesp-app-security-group01|
|azureFirewalls|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-<[rba.azureRegion[7]](README.md#rbaazureRegion)>-firewall<##>|accurint-production-useast2-firewall01|
|bastionHosts|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-bastion<##>|accurint-production-useast2-bastion01|
|connections|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-to-<[rba.onPrem[16]](README.md#rbaonPrem)>-connection|accurint-production-to-bocab1-connection|
|dnsZones|resource group|a-9[63]|||
|expressRouteCircuits|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-expressroute-circuit<##>|accurint-production-useast2-expressroute-circuit01|
|firewallPolicies|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-<[rba.azureRegion[7]](README.md#rbaazureRegion)>-waf-policy<##>|accurint-production-useast2-waf-policy01|
|ruleGroups|firewall policy|a-9[80]|<rule_group_purpose[64]>-rule-group|permitwebservers-rule-group|
|frontDoors|global|a-9[64]|||
|loadBalancers|resource group|a-9[80]|<[rba.serviceName[12]](README.md#rbaserviceName)>-<[rba.environment[7]](README.md#rbaenvironment)>-loadbalancer<##>|webesp-prod-loadbalancer01|
|inboundNatRules|load balancer|a-9[80]|||
|localNetworkGateways|resource group|a-9[80]|<[rba.onPrem[16]](README.md#rbaonPrem)>-<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-local-network-gateway|bocab1-accurint-nonprod-local-network-gateway|
|networkInterfaces|resource group|a-9[80]|||
|networkSecurityGroups|resource group|a-9[80]|||
|securityRules|network security group|a-9[80]|||
|networkWatchers|resource group|a-9[80]|||
|privateDnsZones|resource group|a-9[63]|||
|virtualNetworkLinks|private DNS zone|a-9[80]|||
|publicIPAddresses|resource group|a-9[80]|<[rba.serviceName[12]](README.md#rbaserviceName)>-<[rba.environment[7]](README.md#rbaenvironment)>-publicip<##>|webesp-prod-publicip01|
|publicIPPrefixes|resource group|a-9[80]|||
|routeFilters|resource group|a-9[80]|||
|routeFilterRules|route filter|a-9[80]|||
|routeTables|resource group|a-9[80]|||
|routes|route table|a-9[80]|||
|serviceEndpointPolicies|resource group|a-9[80]|||
|trafficmanagerprofiles|global|a-9[63]|||
|virtualNetworkGateways|resource group|a-9[80]|||
|virtualNetworks|resource group|a-9[64]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-<[rba.azureRegion[7]](README.md#rbaazureRegion)>-vnet|accurint-nonprod-useast2-vnet|
|virtualNetworkPeerings|virtual network|a-9[80]|||
|virtualWans|resource group|a-9[80]|||
|subnets|virtual network|a-9[80]|<[rba.subnetType[24]](README.md#rbasubnetType)>-subnet<##>|private-subnet01|
|vpnGateways|resource group|a-9[80]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-<[rba.virtualNetGwType[12]](README.md#rbavirtualNetGwType)>|accurint-nonprod-expressroute|
|vpnConnections|VPN gateway|a-9[80]|||
|vpnSites|resource group|a-9[80]|||

## azure.NotificationHubs

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|namespaces|global|a-9[50]|||
|AuthorizationRules|namespace|a-9[256]|||
|notificationHubs|namespace|a-9[260]|||
|AuthorizationRules|notification hub|a-9[256]|||

## azure.OperationalInsights

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|clusters|resource group|a-9[63]|||
|workspaces|resource group|a-9[63]|||

## azure.Portal

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|dashboards|resource group|a-9[160]|||

## azure.PowerBI

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|workspaceCollections|region|a-9[63]|||

## azure.PowerBIDedicated

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|capacities|region|a9[63]|||

## azure.RecoveryServices

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|vaults|resource group|a-9[50]|||
|backupPolicies|vault|a-9[150]|||

## azure.Relay

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|namespaces|global|a-9[50]|||
|AuthorizationRules|namespace|a-9[50]|||
|HybridConnections|namespace|a-9[260]|||
|authorizationRules|hybrid connection|a-9[50]|||
|WcfRelays|namespace|a-9[260]|||
|authorizationRules|Wcf relay|a-9[50]|||

## azure.Resources

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|deployments|resource group|a-9[64]|<[rba.productGroup[12]](README.md#rbaproductGroup)>-<[rba.subscriptionType[12]](README.md#rbasubscriptionType)>-<[rba.azureRegion[7]](README.md#rbaazureRegion)>-deployment<###>|accurint-nonprod-useast2-deployment001|
|resourcegroups|subscription|a-9[90]|<[rba.resourceGroupType[12]](README.md#rbaresourceGroupType)>-<[rba.productName[16]](README.md#rbaproductName)>-<[rba.environment[7]](README.md#rbaenvironment)>|app-accurintweb-dev|
|tagNames|resource|a-9[512]|<[rba.tagName[24]](README.md#rbatagName)>|environment|
|tagValues|tag name|a-9[256]|<rba.* value>|production|

## azure.ServiceBus

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|namespaces|global|a-9[50]|||
|AuthorizationRules|namespace|a-9[50]|||
|disasterRecoveryConfigs|global|a-9[50]|||
|migrationConfigurations|namespace|default[63]|||
|queues|namespace|a-9[260]|||
|authorizationRules|queue|a-9[50]|||
|topics|namespace|a-9[260]|||
|authorizationRules|topic|a-9[50]|||
|subscriptions|topic|a-9[50]|||
|rules|subscription|a-9[50]|||

## azure.ServiceFabric

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|clusters|region|a-9[23]|||

## azure.SignalRService

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|signalR|global|a-9[63]|||

## azure.Sql

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|managedInstances|global|a-9[63]|||
|servers|global|a-9[63]|||
|databases|server|a-9[128]|||
|syncGroups|database|a-9[150]|||
|elasticPools|server|a-9[128]|||
|failoverGroups|global|a-9[63]|||
|firewallRules|server|a-9[128]|||

## azure.StorSimple

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|managers|resource group|a-9[50]|||

## azure.Storage

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|blob|container|a-9[1024]|||
|queue|storage account|a-9[63]|||
|storageAccounts|global|a9[24]|||
|blobServices|storage account|default[63]|||
|containers|storage account|a-9[63]|||
|fileServices|storage account|default[63]|||
|shares|storage account|a-9[63]|||
|managementPolicies|storage account|default[63]|||
|table|storage account|a9[63]|||

## azure.StorageSync

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|storageSyncServices|resource group|a-9[260]|||
|syncGroups|storage sync service|a-9[260]|||

## azure.StreamAnalytics

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|streamingjobs|resource group|a-9[63]|||
|functions|streaming job|a-9[63]|||
|inputs|streaming job|a-9[63]|||
|outputs|streaming job|a-9[63]|||
|transformations|streaming job|a-9[63]|||

## azure.TimeSeriesInsights

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|environments|resource group|a-9[90]|||
|accessPolicies|environment|a-9[90]|||
|eventSources|environment|a-9[90]|||
|referenceDataSets|environment|a9[63]|||

## azure.Web

|Entity|Scope|Rule|Convention|Example|
| ------ | ------ | ------ | ------ | ------ |
|serverfarms|resource group|a-9[40]|||
|sites|global|a-9[60]|||
|slots|site|a-9[59]|||
