
variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "tf-mini-3tier"
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "asg_min" {
  type    = number
  default = 1
}

variable "asg_max" {
  type    = number
  default = 2
}

variable "asg_desired" {
  type    = number
  default = 1
}
