
variable "awsprops" {
    type = "map"
    default = {
    region = "us-east-2"
    vpc = "vpc-5234832d"
    ami = "ami-09361c0961e24e0eb"
    itype = "t2.micro"
    subnet = "subnet-3d779c40"
    publicip = true
    keyname = "K8s"
  }
}
variable "vpc_security_group_ids" {
  type = map(list(string))
  default = {
    "launch-wizard-2"     = ["sg-0eb39133d03a284ca"]
    "launch-wizard-1" = ["sg-041173b04ccbaaaad"]
  }
}

