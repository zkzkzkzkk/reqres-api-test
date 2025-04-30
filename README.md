# Reqres API 接口功能测试项目

本项目基于 https://reqres.in 模拟平台，使用 Postman 和 Python + Pytest 对用户登录与注册接口进行功能性测试，验证系统在正常与异常输入下的响应行为。

## 功能
- 登录成功测试
- 缺失密码场景测试
- 注册失败测试
- 可接入更多用户接口如查询、删除等

## 运行方式
```bash
pip install pytest requests
pytest test_cases/test_user_api.py
```
