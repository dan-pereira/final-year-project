# bulk push whole repo to EC2 instance serving the application

start:
	aws ec2 start-instances --instance-ids i-07f811e984fc90a3b

stop:
	aws ec2 stop-instances --instance-ids i-07f811e984fc90a3b

ech:
	echo 'heee'

push:
	scp -r ../server  ubuntu@ec2-18-200-112-1.eu-west-1.compute.amazonaws.com:~/.

pull:
	scp -r ubuntu@ec2-18-200-112-1.eu-west-1.compute.amazonaws.com:~/server/ ../
