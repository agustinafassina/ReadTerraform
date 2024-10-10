terraform {
    required_version = "1.2.3"
}

 provider "aws" {
  shared_credentials_files = ["$HOME/.aws/credentials"]
}

locals  {
    instance_name                               = "instance-name-terraform-test"
    environment                                 = terraform.workspace
}

module "ecs-cluster" {
    source                                      = "./modules/ecs-cluster"
    environment                                 = local.environment
}