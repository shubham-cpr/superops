provider "aws" {
  region = var.aws_region
}
###############################################################
###############################################################
########## Creating VPC infrastructure ########################

# VPC
resource "aws_vpc" "superops" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = var.vpc_name
  }
}

# Internet Gateway
resource "aws_internet_gateway" "my-internet-gw" {
  vpc_id = aws_vpc.superops.id
  tags = {
    Name = var.internet_gateway_name
  }
}

# Subnet
resource "aws_subnet" "subnet_1" {
  vpc_id                  = aws_vpc.superops.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
  tags = {
    Name = var.subnet_1_name
  }
}

resource "aws_subnet" "subnet_2" {
  vpc_id                  = aws_vpc.superops.id
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1b"
  tags = {
    Name = var.subnet_2_name
  }
}

# Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.superops.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.my-internet-gw.id
  }
}

resource "aws_route_table_association" "subnet_1" {
  subnet_id      = aws_subnet.subnet_1.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "subnet_2" {
  subnet_id      = aws_subnet.subnet_2.id
  route_table_id = aws_route_table.public.id
}

###############################################################
###############################################################
########## Create nginx-server infrastructure #################

# Security Group

resource "aws_security_group" "nginx_sg" {
  name        = "nginx-sg"
  description = "Allow HTTP and SSH"
  vpc_id      = aws_vpc.superops.id

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Allow SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "nginx" {
  count         = 2
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = element([aws_subnet.subnet_1.id, aws_subnet.subnet_2.id],count.index)
  key_name      = var.key_name
  vpc_security_group_ids = [aws_security_group.nginx_sg.id]
  associate_public_ip_address = true
  user_data = file("userdata.sh")

  tags = {
    Name = "nginx-${count.index + 1}"
  }
}

# Load Balancer

resource "aws_lb" "nginx_lb" {
  name               = "nginx-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.nginx_sg.id]
  subnets            = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
  enable_deletion_protection = false
}

# Target Group
resource "aws_lb_target_group" "nginx_tg" {
  name     = "nginx-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.superops.id

  health_check {
    path                = "/"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
    matcher             = "200"
  }
}

# Attach EC2 Instances to Target Group
resource "aws_lb_target_group_attachment" "nginx_attachment" {
  count            = 2
  target_group_arn = aws_lb_target_group.nginx_tg.arn
  target_id        = aws_instance.nginx[count.index].id
  port             = 80
}

# Listener
resource "aws_lb_listener" "nginx_listener" {
  load_balancer_arn = aws_lb.nginx_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.nginx_tg.arn
  }
}

