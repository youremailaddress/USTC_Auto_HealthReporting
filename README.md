# USTC_Auto_HealthReporting
中国歪比巴卜大学自动健康打卡服务器脚本</br>
感谢xbb1973/USTC-ncov-AutoReport的启发</br>
(虽然那个脚本貌似已经因为CAS的升级而失效了</br>
(不过2021年了，打卡的人也更少了((</br>
仅供学习参考使用</br>
写了一个2021年6月可用的python脚本,需要挂在服务器上(以后或许会琢磨其他更方便的途径)</br>
- ## 使用方法
```shell
nohup python/python3 report.py jsonfile.json logfile.log >/dev/null 2>&1 &
```
使用前**确保安装**对应的python库:request 和 pytz</br>
jsonfile.json为配置地址，logfile.log为记录运行情况</br>
示例jsonfile.json已经上传,data字段为列表,列表中每个集合的key解释如下
> username:学号，字符串</br>
> password:密码，字符串</br>
> max_retry_times：最大重试次数，也就是失败了之后会自动重复多少次，数字非字符串</br>
> time_hour：几点打卡，24小时制，不用补0，是数字形式</br>
> time_minute：几分打卡，不用补0，数字形式</br>

支持多人、并发处理，但是具体并发性怎么样没有机会测试过</br>
默认是中区正常在校，目前还没做快速修改的接口，不过可以自行修改源码
