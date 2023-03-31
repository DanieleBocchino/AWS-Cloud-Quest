
# API with Database

[![AWS](https://img.shields.io/badge/AWS-100000?style=flat&logo=amazon&logoColor=FFFFFF&labelColor=5C5C5C&color=FF7300)](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html)
[![EBS](https://img.shields.io/badge/AWS_EBS-100000?style=flat&logo=amazonebs&logoColor=white&labelColor=494949&color=ED1C24)](https://aws.amazon.com/route53/)
[![Aurora](https://img.shields.io/badge/AWS_Aurora-100000?style=flat&logo=AmazonRDS&logoColor=white&labelColor=494949&color=527FFF)](https://aws.amazon.com/aurora/)
[![Backup](https://img.shields.io/badge/AWS_backup-100000?style=flat&logo=awsbackup&logoColor=white&labelColor=494949&color=569A31)](https://aws.amazon.com/vpc/)
[![EC2](https://img.shields.io/badge/AWS_EC2-100000?style=flat&logo=amazonec2&logoColor=white&labelColor=494949&color=FF7300)](https://aws.amazon.com/vpc/)
[![KMS](https://img.shields.io/badge/AWS_KMS-100000?style=flat&logo=awsKMS&logoColor=white&labelColor=494949&color=ED1C24)](https://aws.amazon.com/kms/)


This repository contains scripts and configuration files for backing up data on AWS using various services such as Amazon EBS volumes and Aurora Serverless clustering.

<p align="center">
  <img src="./img/1.png" alt="" style="display: block; margin: auto;" />
</p>

## Table of Contents

- [Requirements](#requirements)
- [Steps](#Steps)
- [Conclusion](#conclusion)
- [Contributors](#contributors)


## Requirements
To complete this quest, you will need an AWS account with access to the following services:
- Amazon Aurora Serverless 
- Amazon Backup
- Amazon KMS
- Amazon EBS
- Amazon EC2

## Steps
### Step 1: Create a custom backup vault
<p align="center">
  <img src="./img/2.png" alt="" style="display: block; margin: auto;" />
</p>

### Step 2:Creating a backup plans
Create automated backup plans for EC2 attached Amazon EBS volumes using tags

<p align="center">
  <img src="./img/3.png" alt="" style="display: block; margin: auto;" />
</p>

### Step 3:Configure an AWS backup plan for an Amazon Aurora
Configure an AWS backup plan for an Amazon Aurora Serverless clustering by using the default backup vault

Assign the Aurora Serverless cluster as a resource by using the tag "Backup-DIY" = "TRUE"
<p align="center">
  <img src="./img/4.png" alt="" style="display: block; margin: auto;" />
</p>


## Conclusion
In conclusion, backing up your data is essential to ensure its safety and continuity in the event of an unexpected event. AWS provides multiple solutions for backing up your data, including creating a custom backup vault, configuring automated backup plans, and using tags to manage resources. With the knowledge gained from this guide, you can now confidently create and manage backup solutions for your AWS resources, ensuring that your data is always protected and available. Remember to regularly review and test your backup plans to ensure their effectiveness and make any necessary adjustments.

<p align="center">
  <img src="./img/5.png" alt="" style="display: block; margin: auto;" />
</p>

## Contributors

[Daniele Bocchino](https://danielebocchino.github.io/)

[![GitHub Followers](https://img.shields.io/github/followers/DanieleBocchino?style=social)](https://github.com/DanieleBocchino)  
[![LinkedIn Connect](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/daniele-bocchino-aa602a20b/)
