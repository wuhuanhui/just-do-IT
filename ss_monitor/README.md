##简单的端口连接监控 发送告警邮件 脚本
### systemctl 配置

---
执行步骤：

```
 cp -f ss_monitor.service /etc/systemd/system/
 systemctl daemon-reload
 systemctl start ss_monitor.service
 systemctl enable ss_monitor.service
```
查看日志：
```
journalctl -xu auto_release
```

