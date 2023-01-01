
variable "instance_name" {
        description = "Name of the instance to be created"
        default = "web_client3"
}

variable "instance_type" {
        default = "t2.micro"
}

variable "subnet_id" {
        description = "The VPC subnet the instance(s) will be created in"
        default = "subnet-3d779c40"
}

variable "ami_id" {
        description = "The AMI to use"
        default = "ami-000e7ce4dd68e7a11"
}

variable "number_of_instances" {
        description = "number of instances to be created"
        default = 1
}


variable "ami_key_pair_name" {
        default = "K8s"
}