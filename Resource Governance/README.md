
# Resources Governance

[![AWS](https://img.shields.io/badge/AWS-100000?style=flat&logo=amazon&logoColor=FFFFFF&labelColor=5C5C5C&color=FF7300)](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html)
[![Cloud Config](https://img.shields.io/badge/AWS_Cloud_Config-100000?style=flat&logo=amazoncloudWatch&logoColor=white&labelColor=494949&color=ED1C24)](https://aws.amazon.com/cloudconfig/)
[![EC2](https://img.shields.io/badge/AWS_EC2-100000?style=flat&logo=amazonec2&logoColor=white&labelColor=494949&color=FF7300)](https://aws.amazon.com/cloudwatch/)
[![S3](https://img.shields.io/badge/AWS_S3-100000?style=flat&logo=amazons3&logoColor=white&labelColor=494949&color=FF7300)](https://aws.amazon.com/cloudwatch/)


This AWS Cloud Quest focuses on configuring AWS Config managed rules for S3 KMS encryption, tagged resources, and S3 bucket versioning. The following are the steps to complete this quest.
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
- Amazon Cloud Config
- Amazon EC2
- Amazon S3

## Steps
### Step 1: Create an AWS Config Managed Rule for S3 KMS Encryption
In this step, you need to create an AWS Config managed rule that verifies that all S3 buckets in your account are encrypted using KMS. To create this rule, follow the below steps::

1. Open the AWS Config console and choose "Managed rules".
2. Choose "Add rule".
3. Select the AWS managed rule "s3-bucket-server-side-encryption-by-default".
4. Choose the "AWS Config managed" option for remediation.
5. Review the rule and choose "Add rule".
6. Check compliance status and noncompliant rules on AWS Config Dashboard

<p align="center">
  <img src="./img/2.png" alt="" style="display: block; margin: auto;" />
</p>

### Step 2: Configure an AWS Config Managed Rule for Tagged Resources
In this step, you need to create an AWS Config managed rule that verifies that all resources in your account are tagged with a specific tag. To create this rule, follow the below steps:

1. Open the AWS Config console and choose "Managed rules".
2. Choose "Add rule".
3. Select the AWS managed rule "required-tags".
4. Choose the "AWS Config managed" option for remediation.
5. Specify the tag key and value that you want to use for the rule.
6. Review the rule and choose "Add rule".

<p align="center">
  <img src="./img/4.png" alt="" style="display: block; margin: auto;" />
</p>

### Step 3: Configure an AWS Config Managed Rule for S3 Bucket Versioning
In this step, you need to create an AWS Config managed rule that verifies that all S3 buckets in your account have versioning enabled. To create this rule, follow the below steps:

1. Open the AWS Config console and choose "Managed rules".
2. Choose "Add rule".
3. Select the AWS managed rule "s3-bucket-versioning-enabled".
4. Choose the "AWS Config managed" option for remediation.
5. Review the rule and choose "Add rule".
6. Check compliance status and noncompliant rules on AWS Config Dashboard

<p align="center">
  <img src="./img/5.png" alt="" style="display: block; margin: auto;" />
</p>
By completing the above steps, you will have successfully configured AWS Config managed rules for S3 KMS encryption, tagged resources, and S3 bucket versioning.

## Conclusion
This AWS quest has taught us how to effectively govern our AWS resources by implementing several managed rules using AWS Config. By setting up rules for S3 KMS encryption, resource tagging, and S3 bucket versioning, we have increased the security and compliance of our resources while also ensuring that they are properly configured and easily managed. With AWS Config, we can easily monitor our resources and take action when necessary to maintain a secure and well-governed AWS environment.

<p align="center">
  <img src="./img/6.png" alt="" style="display: block; margin: auto;" />
</p>

## Contributors

[Daniele Bocchino](https://danielebocchino.github.io/)

[![GitHub Followers](https://img.shields.io/github/followers/DanieleBocchino?style=social)](https://github.com/DanieleBocchino)  
[![LinkedIn Connect](https://img.shields.io/badge/LinkedIn-Connect-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/daniele-bocchino-aa602a20b/)
