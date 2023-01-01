terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  shared_credentials_file = "/home/centos/.aws/credentials"
  profile = "default"
  region = "us-east-2"
}

resource "aws_instance" "pen-test-server" {
  ami = lookup(var.awsprops, "ami")
  instance_type = lookup(var.awsprops, "itype")
  subnet_id = lookup(var.awsprops, "subnet")
  associate_public_ip_address = lookup(var.awsprops, "publicip")
  key_name = lookup(var.awsprops, "keyname")
  vpc_security_group_ids = lookup(var.awsprops,"secgroupId")
  
  root_block_device {
    delete_on_termination = true
    volume_size = 15
    volume_type = "gp2"
  }
  tags = {
    Name = "Kali-linux"
  }


}

output "ec2instance" {
  value = aws_instance.pen-test-server.public_ip
}

