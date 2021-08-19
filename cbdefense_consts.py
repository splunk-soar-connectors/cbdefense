# File: cbdefense_consts.py
# Copyright (c) 2018-2021 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.

ERROR_CODE_EXCEPTION = "Error code unavailable"
ERROR_MSG_EXCEPTIOIN = "Unknown error occurred. Please check the asset configuration and|or action parameters."
EXCEPTION_OCCURRED = "Exception occured: "
CBD_EMPTY_RESPONSE_NO_HEADER = "Empty response and no information in the header"
CBD_ERROR_TEXT = "Cannot parse error details"
CBD_SEIM_ERROR = "The asset configuration parameters siem_key and siem_connector_id are required to run this action."
CBD_CUSTOM_API_ERROR = "The asset configuration parameters custom_api_key and custom_api_connector_id are required to run this action."
CBD_ORG_KEY_ERROR = "The asset configuration parameter org_key is required to run this action."
CBD_API_ERROR = "The asset configuration parameters api_key and api_connector_id are required to run this action."
CBD_POLICY_API = "/integrationServices/v3/policy"
CBD_POLICY_API_DEL = "/integrationServices/v3/policy/{0}"
CBD_POLICY_DELETED = "Policy successfully deleted"
CBD_RULE_DELETED = "Rule successfully deleted"
CBD_ADD_RULE_API = "/integrationServices/v3/policy/{0}/rule"
CBD_DEL_RULE_API = "/integrationServices/v3/policy/{0}/rule/{1}"
CBD_LIST_DEVICE_API = "/appservices/v6/orgs/{0}/devices/_search"
CBD_UPDATE_DEVICE_API = "/appservices/v6/orgs/{0}/device_actions"
CBD_UPDATED_DEVICE_POLICY = "Successfully updated device's policy"

CBD_LIST_PROCESS_GET_JOB_API = "/api/investigate/v2/orgs/{0}/processes/search_jobs"
CBD_LIST_PROCESS_VERIFY_JOB_API = "/api/investigate/v1/orgs/{0}/processes/search_jobs/{1}"
CBD_LIST_PROCESS_RESULT_API = "/api/investigate/v2/orgs/{0}/processes/search_jobs/{1}/results"

CBD_LIST_EVENT_GET_JOB_API = "/api/investigate/v2/orgs/{0}/enriched_events/search_jobs"

CBD_EVENT_JOB_DETAILS_API = "/api/investigate/v2/orgs/{1}/enriched_events/{2}/{0}"
CBD_EVENT_JOB_SEARCH_API = "/api/investigate/v1/orgs/{1}/enriched_events/{2}/{0}"
CBD_EVENT_JOB_RESULT_API = "/api/investigate/v2/orgs/{1}/enriched_events/{2}/{0}/results"

CBD_COMPLETED_NOT_EQ_CONTACTED = ", process still not completed so results may vary. please re-try after sometime."

CBD_GET_ALERT_API = "/appservices/v6/orgs/{1}/alerts/{0}"
CBD_GET_EVENT_API = "/api/investigate/v2/orgs/{0}/enriched_events/detail_jobs"

CBD_NOTIFICATION_API = "/integrationServices/v3/notification"

CBD_POLICY_UPDATED_SUCCESS = "Policy updated successfully"
CBD_POLICY_RETRIEVED_SUCCESS = "Policy retrieved successfully"

CBD_REQUIRED_FIELD_MESSAGE = "Add at-least value in one of following fields: event_type, ip, host name, hash, application, owner"
CBD_REQUIRED_FIELD_MESSAGE_PROCESS = "Add at-least value in one of following fields: ip, host name, owner"

TEST_CONNECTIVITY_FAILED = "Test Connectivity Failed"
TEST_CONNECTIVITY_PASSED = "Test Connectivity Passed"
