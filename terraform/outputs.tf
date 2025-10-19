
output "alb_dns_name" {
  description = "Public DNS name of the ALB"
  value       = aws_lb.alb.dns_name
}

output "vpc_id" {
  value = aws_vpc.main.id
}

output "target_group_arn" {
  value = aws_lb_target_group.tg.arn
}
