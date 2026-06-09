# Operation Manual Pattern

## When to Use

- Personal tools
- Practical utilities
- Projects needing quick start
- Tools with specific use cases
- Chinese-language projects

## Structure

```markdown
# Project Name (with Logo)

[Badges]

Description + Use Cases

## Quick Start
## Installation (multiple methods)
## Configuration
## Usage (with API table)
## Extension Guide
## Contributing
## License
```

## Example: proxy_pool Style

```markdown
# 🔒 Proxy Pool

[![Tests](https://github.com/user/proxy-pool/actions/workflows/test.yml/badge.svg)](https://github.com/user/proxy-pool/actions)
[![codecov](https://codecov.io/gh/user/proxy-pool/branch/main/graph/badge.svg)](https://codecov.io/gh/user/proxy-pool)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> 一个轻量级的代理池系统，自动抓取、验证和管理代理。

**功能特性：**
- 自动抓取免费代理
- 实时验证代理可用性
- 提供 RESTful API 接口
- 支持多种代理协议（HTTP/HTTPS/SOCKS5）

**适用场景：**
- 爬虫开发
- 数据采集
- 接口测试

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/user/proxy-pool.git
cd proxy-pool
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置

复制配置文件：

```bash
cp config.example.py config.py
```

编辑 `config.py`：

```python
# 数据库配置
DB_HOST = "localhost"
DB_PORT = 6379
DB_PASSWORD = ""

# 代理验证
VALIDATE_INTERVAL = 300  # 验证间隔（秒）
```

### 4. 启动

```bash
python run.py
```

服务将在 `http://localhost:5000` 启动。

## 📦 安装方式

### 方式一：pip 安装（推荐）

```bash
pip install proxy-pool
```

### 方式二：Docker 安装

```bash
docker pull user/proxy-pool:latest
docker run -d -p 5000:5000 user/proxy-pool
```

### 方式三：docker-compose

```bash
git clone https://github.com/user/proxy-pool.git
cd proxy-pool
docker-compose up -d
```

### 方式四：源码安装

```bash
git clone https://github.com/user/proxy-pool.git
cd proxy-pool
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## ⚙️ 配置说明

| 配置项 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `DB_HOST` | string | `localhost` | Redis 主机地址 |
| `DB_PORT` | int | `6379` | Redis 端口 |
| `DB_PASSWORD` | string | `""` | Redis 密码 |
| `DB_DB` | int | `0` | Redis 数据库 |
| `VALIDATE_INTERVAL` | int | `300` | 代理验证间隔（秒） |
| `PROXY_FETCH_INTERVAL` | int | `600` | 代理抓取间隔（秒） |
| `API_HOST` | string | `0.0.0.0` | API 服务监听地址 |
| `API_PORT` | int | `5000` | API 服务端口 |
| `MAX_PROXIES` | int | `1000` | 最大代理数量 |

## 📖 使用方法

### API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/proxy` | GET | 获取一个代理 |
| `/api/proxy?protocol=https` | GET | 获取 HTTPS 代理 |
| `/api/proxy?count=10` | GET | 获取 10 个代理 |
| `/api/proxies` | GET | 获取所有代理 |
| `/api/status` | GET | 获取代理池状态 |
| `/api/refresh` | POST | 强制刷新代理池 |

### 获取代理

```bash
# 获取一个代理
curl http://localhost:5000/api/proxy

# 获取 HTTPS 代理
curl http://localhost:5000/api/proxy?protocol=https

# 获取 10 个代理
curl http://localhost:5000/api/proxy?count=10
```

### Python 使用示例

```python
import requests

# 获取代理
response = requests.get("http://localhost:5000/api/proxy")
proxy = response.json()

# 使用代理
proxies = {
    "http": f"http://{proxy['ip']}:{proxy['port']}",
    "https": f"http://{proxy['ip']}:{proxy['port']}",
}

response = requests.get("https://httpbin.org/ip", proxies=proxies)
print(response.json())
```

### 爬虫使用示例

```python
import requests
from bs4 import BeautifulSoup

def get_proxy():
    response = requests.get("http://localhost:5000/api/proxy")
    return response.json()

def crawl(url):
    proxy = get_proxy()
    proxies = {
        "http": f"http://{proxy['ip']}:{proxy['port']}",
        "https": f"http://{proxy['ip']}:{proxy['port']}",
    }
    
    response = requests.get(url, proxies=proxies, timeout=10)
    return BeautifulSoup(response.text, 'html.parser')

# 使用
html = crawl("https://example.com")
print(html.title.string)
```

## 🔧 扩展代理源

### 添加自定义代理源

1. 创建代理源文件 `sources/my_source.py`：

```python
from sources.base import BaseSource

class MySource(BaseSource):
    """我的自定义代理源"""
    
    async def fetch(self):
        """抓取代理"""
        proxies = []
        
        # 实现抓取逻辑
        # ...
        
        return proxies
```

2. 注册代理源：

编辑 `config.py`：

```python
SOURCES = [
    "sources.free_proxy_list.FreeProxyList",
    "sources.my_source.MySource",  # 添加这一行
]
```

### 代理源接口

```python
class BaseSource:
    """代理源基类"""
    
    async def fetch(self) -> list:
        """
        抓取代理
        
        Returns:
            list: 代理列表，每个代理格式如下：
            {
                "ip": "127.0.0.1",
                "port": 8080,
                "protocol": "http",  # http/https/socks5
                "country": "CN",
                "anonymity": "high",  # high/medium/low
            }
        """
        raise NotImplementedError
```

## 📊 免费代理源

| 代理源 | 状态 | 更新速度 | 可用率 |
|--------|------|----------|--------|
| free-proxy-list.net | ✅ | 10分钟 | 30% |
| proxylist.download | ✅ | 5分钟 | 25% |
| api.proxyscrape.com | ✅ | 1分钟 | 35% |
| geonode.com | ✅ | 30分钟 | 20% |

## 🐛 问题反馈

- [GitHub Issues](https://github.com/user/proxy-pool/issues)
- [博客文章](https://example.com/blog/proxy-pool)

## 🤝 贡献代码

欢迎提交 Pull Request！

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/my-feature`
3. 提交更改：`git commit -m 'Add my feature'`
4. 推送分支：`git push origin feature/my-feature`
5. 提交 Pull Request

### 贡献者

<a href="https://github.com/user/proxy-pool/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=user/proxy-pool" />
</a>

## 📝 更新日志

See [CHANGELOG.md](./CHANGELOG.md)

## 📄 License

[MIT](./LICENSE)
```

## Key Principles

1. **Practical Focus**: Users want to "install → run → use"
2. **Multiple Installation Methods**: pip, Docker, docker-compose, source
3. **API Documentation Inline**: Don't make users jump to docs
4. **Extension Guide**: How to add custom features
5. **Chinese-Friendly**: Clear, direct language
6. **Visual Elements**: Tables, emojis, status indicators

## Checklist

- [ ] Title with emoji or logo
- [ ] Badges (CI, coverage, license)
- [ ] One-line description
- [ ] Feature list
- [ ] Use case scenarios
- [ ] Quick start (3 steps)
- [ ] Multiple installation methods
- [ ] Configuration table
- [ ] API documentation
- [ ] Usage examples
- [ ] Extension guide
- [ ] Problem feedback channels
- [ ] Contributing guide
- [ ] Contributors section
- [ ] License
