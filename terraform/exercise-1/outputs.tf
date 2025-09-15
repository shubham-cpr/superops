# output.tf

output "vpc_id" {
  value = aws_vpc.superops.id
}

output "vpc_name" {
  value = aws_vpc.superops.tags["Name"]
}

output "internet_gateway_id" {
  value = aws_internet_gateway.my-internet-gw.id
}

output "internet_gateway_name" {
  value = aws_internet_gateway.my-internet-gw.tags["Name"]
}

output "subnet_1_id" {
  value = aws_subnet.subnet_1.id
}

output "subnet_1_name" {
  value = aws_subnet.subnet_1.tags["Name"]
}

output "subnet_2_id" {
  value = aws_subnet.subnet_2.id
}

output "subnet_2_name" {
  value = aws_subnet.subnet_2.tags["Name"]
}

output "route_table_id" {
  value = aws_route_table.public.id
}

output "route_table_association_id_subnet_1" {
  value = aws_route_table_association.subnet_1.id
}

output "route_table_association_id_subnet_2" {
  value = aws_route_table_association.subnet_2.id
}

output "security_group_id" {
  value = aws_security_group.nginx_sg.id
}

output "security_group_name" {
  value = aws_security_group.nginx_sg.name
}

output "instance_ids" {
  value = aws_instance.nginx[*].id
}

output "instance_names" {
  value = [for i in aws_instance.nginx : i.tags["Name"]]
}

output "alb_id" {
  value = aws_lb.nginx_lb.id
}

output "alb_name" {
  value = aws_lb.nginx_lb.name
}

output "load_balancer_dns" {
  value = aws_lb.nginx_lb.dns_name
  description = "DNS of the load balancer"
}

output "target_group_id" {
  value = aws_lb_target_group.nginx_tg.id
}

output "target_group_arn" {
  value = aws_lb_target_group.nginx_tg.arn
}

output "listener_id" {
  value = aws_lb_listener.nginx_listener.id
}