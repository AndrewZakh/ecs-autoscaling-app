# provider.tf

# Specify the provider and access details
provider "aws" {
  shared_config_files      = ["$HOME/.aws/config"]
  shared_credentials_files = ["$HOME/.aws/credentials"]
  profile                 = "aws_study"
  region                  = var.aws_region
}

module "ecr_pipeline" {
  source = "github.com/globeandmail/aws-codepipeline-ecr?ref=1.9"

  name               = "factorial"
  ecr_name           = "factorial"
  github_repo_owner  = "AndrewZakh"
  github_repo_name   = "ecs-autoscaling-app"
  github_oauth_token = data.aws_ssm_parameter.github_token.value
  tags = {
    Env = "prod"
  }
  use_repo_access_github_token = true
  svcs_account_github_token_aws_secret_arn = svcs-account-github-token-aws-secret-arn
  svcs_account_github_token_aws_kms_cmk_arn = svcs-account-github-token-aws-kms-cmk-arn
  s3_block_public_access = true
}
