Before using the AWS EC2 plugin, ensure the following:

AWS CLI Installed: Install and configure the AWS CLI with access credentials.

aws configure
This will store your AWS credentials in ~/.aws/credentials.

Install Python Packages: Install the necessary Python packages for Ansible AWS integration:


pip install boto3 botocore

Ansible Installed: Ensure Ansible is installed on your system. Install it if needed:

pip install ansible

2. Enable the AWS EC2 Plugin
Ansible includes an AWS EC2 dynamic inventory plugin (amazon.aws.aws_ec2) by default.

Create a Configuration File
Create a YAML file named aws_ec2.yml in your working directory:


Explanation:
plugin: Specifies the dynamic inventory plugin to use.
aws_profile: The AWS CLI profile to use for authentication.
regions: AWS regions to query for EC2 instances.
filters: Filters instances (e.g., running state only).
keyed_groups: Organizes inventory into groups based on tags.
hostnames: Defines which field to use as the hostname (e.g., private IP).

3. Test the Dynamic Inventory
Test if the plugin is working by running the following command:

bash
Copy code
ansible-inventory -i aws_ec2.yml --list
