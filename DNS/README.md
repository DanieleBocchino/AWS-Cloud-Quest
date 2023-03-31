# AWS DNS Quest

[![AWS](https://img.shields.io/badge/AWS-100000?style=flat&logo=amazon&logoColor=FFFFFF&labelColor=5C5C5C&color=FF7300)](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html)
[![IAM](https://img.shields.io/badge/AWS_IAM-100000?style=flat&logo=drone&logoColor=white&labelColor=494949&color=ED1C24)](https://aws.amazon.com/iam/)
[![AURORA](https://img.shields.io/badge/AWS_Aurora-100000?style=flat&logo=AmazonRDS&logoColor=white&labelColor=494949&color=527FFF)](https://aws.amazon.com/aurora/)
[![S3](https://img.shields.io/badge/AWS_Quicksight-100000?style=flat&logo=AmazonS3&logoColor=white&labelColor=494949&color=569A31)](https://aws.amazon.com/s3/)
[![Postgres](https://img.shields.io/badge/PosgreSQL-100000?style=flat&logo=postgresql&logoColor=white&labelColor=494949&color=4169E1)](https://aws.amazon.com/quicksight/)

This quest is designed to demonstrate how to create a private hosted zone for your VPC server domain names using Amazon Route 53. It also covers how to attach A records and CNAME records to your local domain name.
## Table of Contents

- [Requirements](#requirements)
- [Steps](#Steps)
- [Conclusion](#conclusion)
- [Contributors](#contributors)


## Requirements
To complete this quest, you will need an AWS account with access to the following services:
- Amazon Route 53
- Amazon EC2
- Amazon VPC

##Steps
###Step 1: Create a VPC
Create a new VPC in the AWS Management Console. Make sure that you assign a CIDR block to your VPC and create at least one subnet.

###Step 2: Create an EC2 Instance
Launch a new EC2 instance in your VPC. This instance will be used to host your private DNS zone.

###Step 3: Create a Private Hosted Zone
Create a new private hosted zone in Amazon Route 53. Give it a name that matches the domain name of your server. For example, if your server's domain name is "example.com", name your hosted zone "example.com".

###Step 4: Update VPC DNS Settings
Update the DNS settings for your VPC to use the private hosted zone that you just created. This will ensure that your VPC's DNS queries are resolved within the hosted zone.

###Step 5: Attach A Records
Create A records within your local domain name that point to your EC2 instance's private IP address. This will allow you to resolve your server's domain name to the EC2 instance within your VPC.

###Step 6: Attach CNAME Records
Create CNAME records within your local domain name that point to other resources within your VPC. For example, you can create a CNAME record that points to a load balancer's DNS name.ConclusionBy completing this quest, you should have a better understanding of how to create a private hosted zone for your VPC server domain names using Amazon Route 53. You should also be familiar with how to attach A records and CNAME records to your local domain name.

##Conclusion
By completing this quest, you should have a better understanding of how to create a private hosted zone for your VPC server domain names using Amazon Route 53. You should also be familiar with how to attach A records and CNAME records to your local domain name.

## Contributors

[Daniele Bocchino](https://danielebocchino.github.io/)

[![GitHub Followers](https://img.shields.io/github/followers/DanieleBocchino?style=social)](https://github.com/DanieleBocchino)  
[![LinkedIn Connect](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/daniele-bocchino-aa602a20b/)
