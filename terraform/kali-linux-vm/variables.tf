variable "ami_id" {
   description = "AMI ID"
   default = "ami-09361c0961e24e0eb"

}
variable "subnet_prv1" {
  description = "Private Subnet 1"
  default = "subnet-3d779c40"
}
variable "sg_group" {
  description = "Security Group"
  default = "sg-0eb39133d03a284ca"
}
variable "key_pair" {
  description = "key pair"
  default = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCA/v1VD9mUh6DL7jAayzhYEBZbYN4JP6TEOjLJVPTJvkYMG+FgpMIXjctZA+mMeeIbS7zhBOExkRn6Mrri4izcZao5KaW8v/nPGOTprq9a2fykyklBSusdlntwM3ZaOTBcpN3AGOmJNQ0OjFe/0dQn9GPoPVfs5PY/6GOWCg+GkviUK8KUl//ypzZmDFYHKRDk5H1Wx0gCc58p09+LHY9nbok+a2oelwGl4D9Qh1rK8BYZiiMIiKGus9MPE59cAHn87V995xoqR1r0YZbkc6RNktWKxA61TBh9Mg271MSAgieX6zZz7mI3rpV8xrelUA//hRvBWPaofhqHX0DzaRQF K8s"
}

