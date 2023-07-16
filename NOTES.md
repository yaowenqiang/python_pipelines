> https://github.com/kjam/data-pipelines-course
> 
> https://kjamistan.com
> 
> Data Wrangling with Python(Book)
> 
> Data Wrangling and Analysis with Python - Learning Pandas and How to Import, Export, clean, Analyze and Visualize Data(Course)
> 
> https://github.com/yaowenqiang/self-hosted-mailserver/blob/master/docs/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers.md

> apt-get install fail2ban
> 
> adduser jack
> 
> vim /etc/ssh/sshd_config
> 
> PermitRootLogin no
> 
> AllowUsers username

The Twelve-Factor App
http://www.charleshooper.net/blog/briefly-operator-requirements/

Monitor

> getcentry.com
> 
> datadog
> 
> newrelic.com

> https://jvns.ca/blog/2016/09/07/new-zine-linux-debugging-tools-youll-love/
> 
> https://www.datadoghq.com/blog/the-docker-monitoring-problem/
> 
> Tech Talks for Pythonistas: performance Testing and Profiling 
> 
> https://github.com/twitter-archive/iago

> Parallel Programming with Python(Book)

# Celery

> mkirtualenv --python=/usr/bin/python3 data_pipelines
> 
> brew install rabbitmq
> 
> 

webui address

localhost:15672

default   username and password
guest/guest

> 
> pip install celery[rabbitmq]
> 
> pip install pandas
> pip install pandas-datareader
> 
> pip install jupyter
> 
> /opt/homebrew/Cellar/rabbitmq/3.12.1/sbin/rabbitmqctl
> 
> rabbitqctl add_user celery_user mypassword
> 
> rabbitqctl add_vhost celery_vhost
> 
> rabbitqctl set_permissions -p celery_vhost celery_user ".*" ".*" ".*"
> 
> 
## Install anaconda

> https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/
> 
> 
> conda clean -i 
> 
> conda activate myenv
> 
> conda deactivate
> 
> celery -A task worker --loglevel=INFO
> 
> res = get_stock_info.delay('FB', datetime=(2016,1,1), datetime.today())
> 
> res
> 
> res.status
> 
> res.info
> 
> res.get()
> 
> res.failed()
> 
> 
> automation framework
> 
> conda install ansible
> 
> /etc/ansible/hosts
> 
> 
[pipelines]
ip ansible_user=deploy 


> ansible-playbook pipelines_playbook.yml --ask-sudo-pass -vv
> 
> jupyterhub
> 



## Install docker

> export DOWNLOAD_URL="https://mirrors.tuna.tsinghua.edu.cn/docker-ce"

> curl -fsSL https://get.docker.com/ | sudo -E sh
> 
> https://cloud.tencent.com/developer/article/2232804?areaSource=102001.8&traceId=w5HyzmIUxnuQmldhKmudH
