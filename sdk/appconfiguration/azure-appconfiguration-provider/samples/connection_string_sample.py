# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------

from azure.appconfiguration.provider import (
    AzureAppConfigurationProvider,
    SettingSelector
)
import os

connection_string = os.environ.get("AZURE_APPCONFIG_CONNECTION_STRING")

# Connecting to Azure App Configuration using connection string
config = AzureAppConfigurationProvider.load(
    connection_string=connection_string)

print(config["message"])
print(config["my_json"]["key"])

# Connecting to Azure App Configuration using connection string and trimmed key prefixes
trimmed = {"test."}
config = AzureAppConfigurationProvider.load(
    connection_string=connection_string, trimmed_key_prefixes=trimmed)

print(config["message"])

# Connection to Azure App Configuration using SettingSelector
selects = {SettingSelector("message*", "\0")}
config = AzureAppConfigurationProvider.load(
    connection_string=connection_string, selects=selects)

print("message found: " + str("message" in config))
print("test.message found: " + str("test.message" in config))