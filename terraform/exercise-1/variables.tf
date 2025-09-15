variable "aws_region" {
  default     = "us-east-1"
  description = "AWS region to deploy to"
}

variable "vpc_name" {
  default = "superops-vpc"
  description = "Name of VPC"
}

variable "internet_gateway_name" {
  default = "superops-igw"
  description = "Name of internet gateway"
}

variable "subnet_1_name" {
  default = "superops-subnet-1"
  description = "Name of subnet"
}

variable "subnet_2_name" {
  default = "superops-subnet-2"
  description = "Name of subnet"
}

variable "instance_type" {
  default     = "t2.micro"
  description = "EC2 instance type"
}

variable "ami_id" {
  default = "ami-00ca32bbc84273381"
  description = "Ubuntu AMI ID (e.g., for us-east-1: ami-0fc5d935ebf8bc3bc)"
}

variable "key_name" {
  default     = "superops-pem"
  description = "The name of the SSH key pair"
}