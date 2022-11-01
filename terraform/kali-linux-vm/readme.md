To create AWS instance using hashicorp
Connect to AWS instance
Run CLI by aws configure. COnfigure connection
Install terrafrom cli if not installed
Import the files instace.tf, variables.tf, vars.tfvars to a new folder
switch to the new folder
run terraform init
run terraform plan
run terraform apply (To create resources)
After making configuration changes in instance.tf or varaibles.tf,
run terraform apply to apply the changes

If you want to destroy resources
run terraform destroy