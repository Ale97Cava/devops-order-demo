terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

provider "local" {
}

resource "local_file" "environment" {
  filename = "${path.module}/environment.txt"
  content  = "Environment created by Terraform!"
}