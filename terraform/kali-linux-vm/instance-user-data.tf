provider "aws" {
  region = "us-east-2"
  profile = "default"
}

variable "prefix" {
  description = "servername prefix"
  default = "signfxapp"
}

resource "aws_instance" "web" {
  ami           = "ami-0a59f0e26c55590e9"
  instance_type = "t3.medium"
  count = 1
  vpc_security_group_ids = [
    "sg-0eb3913-replace with your sg"
  ]
  user_data = <<EOF
#!/bin/bash
echo "Copying the SSH Key Of ubuntu to the server"
echo -e "ssh-ed25519 ************0fIGXAoB7aJAnbxRs9PY3ULouWZakXPcdh9m2vMz ed25519-key-20221106" >> /home/ubuntu/.ssh/authorized_keys

echo "Mount NFS"
echo "sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-******.efs.us-east-1.amazonaws.com:/ /sharedrive"

echo "Installing NodeExporter"
mkdir /home/ubuntu/node_exporter
cd /home/ubuntu/node_exporter
wget https://github.com/prometheus/node_exporter/releases/download/v1.2.2/node_exporter-1.2.2.linux-amd64.tar.gz
tar node_exporter-1.2.2.linux-amd64.tar.gz
cd node_exporter-1.2.2.linux-amd64
./node_exporter &

echo "Changing Hostname"
hostname "${var.prefix}${count.index+1}"
echo "${var.prefix}${count.index+1}" > /etc/hostname



EOF
  subnet_id = "subnet-3d7-replace with corect subnetid"
  tags = {
    Name = "${var.prefix}${count.index}"
  }
}

output "instances" {
  value       = "${aws_instance.web.*.private_ip}"
  description = "PrivateIP address details"
}