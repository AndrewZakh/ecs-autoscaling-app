# provider.tf

# Specify the provider and access details
provider "aws" {
  shared_config_files      = ["$HOME/.aws/config"]
  shared_credentials_files = ["$HOME/.aws/credentials"]
  profile                 = "aws_study"
  region                  = var.aws_region
}

