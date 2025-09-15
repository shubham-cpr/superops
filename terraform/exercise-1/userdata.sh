#!/bin/bash
yum update -y
yum install -y nginx
echo "Hello SuperOps from $(hostname)" > /usr/share/nginx/html/index.html
systemctl enable nginx
systemctl restart nginx