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

SSH key issue with mobaxterm in connecting to servers
The ky need to be created with Ed25519 more advanced type of key
https://superuser.com/questions/1678830/server-refused-our-key-only-from-mobaxterm-bookmark-setup

Edit sshd_config file sudo vi /etc/ssh/sshd_config.
Search for PasswordAuthentication
If it is no, change it to yes. For me it was commented. If so, uncomment it.
Restart sshd service sudo systemctl restart sshd.service

==================================================
Creating a AWS instance with user-data
Refer instance-user-data.tf script