# 微信数据接口（WeChat API）：公众号文章和阅读数、视频号、微信搜一搜、微信指数

**公众号文章 API · 公众号历史文章 · 公众号阅读数 · 公众号评论 · 视频号数据 · 视频号作品和评论 · 微信搜一搜 · 微信指数**

这个仓库是 [DataXAPI](https://dataxapi.com/zh/?ref=gh-wechat-api) 的微信接口说明和能直接跑的脚本：31 个接口，一把 Key，按次付费，$0.015 起，**出错不收费**。不用登录平台账号，不用 Cookie，不开浏览器。

[免费拿 Key：试用最多 333 次，不用绑卡](https://dataxapi.com/zh/signin/?button=gh-wechat-api) · [全部接口文档](https://dataxapi.com/zh/apis/?ref=gh-wechat-api) · [接进 AI（MCP）](#接进-aimcp) · [English](#english)

最低充 $10，余额不过期；支持支付宝、微信支付和银行卡。

## 最常用的接口

DataXAPI 的客户近 30 天里调用最多的几个，从多到少：

| 接口 | 拿到什么 | 价格 |
|---|---|---|
| [微信公众号文章列表](https://dataxapi.com/zh/apis/wechat_mp/accounts/articles/list/?ref=gh-wechat-api) | 按公众号原始编号取一页它发布的文章，从新到旧：标题、摘要、链接、发布时间、头条还是次条、内容形态、封面。默认取主页的“文章”栏，也可取“视频”“贴图”栏。 | $0.02 一次 |
| [微信公众号文章详情](https://dataxapi.com/zh/apis/wechat_mp/articles/get/?ref=gh-wechat-api) | 按文章链接取一篇公众号文章：标题、正文、发布时间、公众号的名称和编号，以及头条还是次条、内容形态、封面、摘要、署名作者、阅读原文链接和发文 IP 属地。 | $0.02 一次 |
| [微信搜一搜综合搜索](https://dataxapi.com/zh/apis/wechat/posts/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里取一页结果，公众号文章和视频号视频混在一起，每条用 type 标明是文章还是视频；可按相关、最新或最热排、按发布时间筛，也可只搜文章或只搜视频：标题或文案、来源账号名称、发布时间，文章带链接（有的带阅读数档位），视频带点赞和收藏数。搜一搜不给账号编号。 | $0.02 一次 |
| [微信搜一搜视频号视频搜索](https://dataxapi.com/zh/apis/wechat_channels/videos/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里取一页视频号视频，可按相关、最新或最热排、按发布时间筛：文案、发布账号的名称和头像、发布时间、点赞和收藏数、时长、封面。搜一搜不给账号编号，作品编号是 export/ 开头的加密编号：传给 wechat_channels.videos.get 的 export_id 可换出数字编号、视频文件地址和解密密钥，会过期，要尽快用。 | $0.02 一次 |
| [微信公众号实时查找](https://dataxapi.com/zh/apis/wechat/accounts/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里找公众号和服务号，最像的排前面，后面可能跟着不太相关的账号：原始编号、微信号、名称、简介、头像、是否认证、主体名称、原创文章数。按次计费；不带粉丝和阅读数，要这些的估计值用 wechat_mp.accounts.search。 | $0.02 一次 |
| [微信视频号作品详情](https://dataxapi.com/zh/apis/wechat_channels/videos/get/?ref=gh-wechat-api) | 按作品编号、搜索结果的 export/ 编号或分享链接取一条视频号作品：文案、作者、发布时间、点赞、评论、转发、收藏数，以及视频文件地址和解密密钥。 | $0.02 一次 |
| [微信视频号用户作品](https://dataxapi.com/zh/apis/wechat_channels/users/videos/list/?ref=gh-wechat-api) | 按视频号账号编号取一页它发布的视频，从新到旧：文案、发布时间、点赞、评论、转发、收藏数、视频时长。 | $0.02 一次 |
| [微信视频号账号搜索](https://dataxapi.com/zh/apis/wechat_channels/users/search/?ref=gh-wechat-api) | 按名称找视频号账号：名称要一字不差，同名的都返回。给账号编号、名称、简介、头像、是否认证和认证信息；账号编号可以传给视频号的资料、作品列表、直播回放等接口。 | $0.06 一次 |

## 全部 31 个接口

### 公众号

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [微信公众号文章列表](https://dataxapi.com/zh/apis/wechat_mp/accounts/articles/list/?ref=gh-wechat-api) | 按公众号原始编号取一页它发布的文章，从新到旧：标题、摘要、链接、发布时间、头条还是次条、内容形态、封面。默认取主页的“文章”栏，也可取“视频”“贴图”栏。 | $0.02 一次 | `wechat_mp.accounts.articles.list` |
| [微信公众号文章详情](https://dataxapi.com/zh/apis/wechat_mp/articles/get/?ref=gh-wechat-api) | 按文章链接取一篇公众号文章：标题、正文、发布时间、公众号的名称和编号，以及头条还是次条、内容形态、封面、摘要、署名作者、阅读原文链接和发文 IP 属地。 | $0.02 一次 | `wechat_mp.articles.get` |
| [微信公众号实时查找](https://dataxapi.com/zh/apis/wechat/accounts/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里找公众号和服务号，最像的排前面，后面可能跟着不太相关的账号：原始编号、微信号、名称、简介、头像、是否认证、主体名称、原创文章数。按次计费；不带粉丝和阅读数，要这些的估计值用 wechat_mp.accounts.search。 | $0.02 一次 | `wechat.accounts.search` |
| [微信公众号文章互动数据](https://dataxapi.com/zh/apis/wechat_mp/articles/metrics/?ref=gh-wechat-api) | 按文章长链接取这篇公众号文章此刻的数字：阅读、点赞、推荐、分享、收藏、评论。 | $0.02 一次 | `wechat_mp.articles.metrics` |
| [微信公众号资料](https://dataxapi.com/zh/apis/wechat_mp/accounts/get/?ref=gh-wechat-api) | 按公众号原始编号取资料：名称、IP 属地、原创文章数、关联的视频号、是否被封禁。 | $0.02 一次 | `wechat_mp.accounts.get` |
| [微信公众号文章评论](https://dataxapi.com/zh/apis/wechat_mp/articles/comments/list/?ref=gh-wechat-api) | 按文章链接取一页公众号文章的精选评论：正文、评论者、点赞数、回复数、发布时间、IP 属地、是否置顶。 | $0.02 一次 | `wechat_mp.articles.comments.list` |
| [微信公众号评论回复](https://dataxapi.com/zh/apis/wechat_mp/comments/replies/list/?ref=gh-wechat-api) | 按评论编号和文章链接取公众号文章一条评论下面的回复：正文、回复者、点赞数、发布时间、IP 属地、回复的是哪一条。只给前面的一批，不翻页。 | $0.02 一次 | `wechat_mp.comments.replies.list` |
| [微信公众号账号搜索](https://dataxapi.com/zh/apis/wechat_mp/accounts/search/?ref=gh-wechat-api) | 按名字或关键词找公众号，最像的排前面：原始编号、微信号、名称、头像、主体名称，和第三方数据库的预估活跃粉丝、头条平均阅读和点赞、每周发文数（估计值，非官方，可能滞后数月）。按条计费，limit 定条数（默认 5，最多 15）。只要编号不要估计值，用按次计费的 wechat.accounts.search 更省。 | 每条 $0.05635，一次最多 $0.84525 | `wechat_mp.accounts.search` |
| [微信公众号主体信息](https://dataxapi.com/zh/apis/wechat_mp/accounts/owner/get/?ref=gh-wechat-api) | 按公众号原始编号取它的主体（背后的公司、机构或个人）：名称、类型、登记证照号码、国家或地区、认证状态、种类和日期，以及公众号的注册日期、授权过的第三方服务商。 | $0.1 一次 | `wechat_mp.accounts.owner.get` |

### 视频号

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [微信搜一搜视频号视频搜索](https://dataxapi.com/zh/apis/wechat_channels/videos/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里取一页视频号视频，可按相关、最新或最热排、按发布时间筛：文案、发布账号的名称和头像、发布时间、点赞和收藏数、时长、封面。搜一搜不给账号编号，作品编号是 export/ 开头的加密编号：传给 wechat_channels.videos.get 的 export_id 可换出数字编号、视频文件地址和解密密钥，会过期，要尽快用。 | $0.02 一次 | `wechat_channels.videos.search` |
| [微信视频号作品详情](https://dataxapi.com/zh/apis/wechat_channels/videos/get/?ref=gh-wechat-api) | 按作品编号、搜索结果的 export/ 编号或分享链接取一条视频号作品：文案、作者、发布时间、点赞、评论、转发、收藏数，以及视频文件地址和解密密钥。 | $0.02 一次 | `wechat_channels.videos.get` |
| [微信视频号用户作品](https://dataxapi.com/zh/apis/wechat_channels/users/videos/list/?ref=gh-wechat-api) | 按视频号账号编号取一页它发布的视频，从新到旧：文案、发布时间、点赞、评论、转发、收藏数、视频时长。 | $0.02 一次 | `wechat_channels.users.videos.list` |
| [微信视频号账号搜索](https://dataxapi.com/zh/apis/wechat_channels/users/search/?ref=gh-wechat-api) | 按名称找视频号账号：名称要一字不差，同名的都返回。给账号编号、名称、简介、头像、是否认证和认证信息；账号编号可以传给视频号的资料、作品列表、直播回放等接口。 | $0.06 一次 | `wechat_channels.users.search` |
| [微信视频号作品评论](https://dataxapi.com/zh/apis/wechat_channels/videos/comments/list/?ref=gh-wechat-api) | 按作品编号取一页视频号作品的一级评论：正文、评论者、点赞数、发布时间、IP 属地。 | $0.02 一次 | `wechat_channels.videos.comments.list` |
| [微信视频号作品分享链接](https://dataxapi.com/zh/apis/wechat_channels/videos/share_link/get/?ref=gh-wechat-api) | 按作品编号生成一条能在微信里打开的分享链接（weixin.qq.com/sph/ 开头）。同一作品每次生成的链接不同，旧链接仍然指向这个作品；链接不能用编号拼出来。 | $0.02 一次 | `wechat_channels.videos.share_link.get` |
| [微信视频号账号资料](https://dataxapi.com/zh/apis/wechat_channels/users/get/?ref=gh-wechat-api) | 按视频号账号编号取资料：名称、简介、头像、IP 属地、作品数。 | $0.02 一次 | `wechat_channels.users.get` |
| [微信视频号账号的合集](https://dataxapi.com/zh/apis/wechat_channels/users/collections/list/?ref=gh-wechat-api) | 按视频号账号编号取这个账号公开的全部合集：名称、简介、封面、视频数、最近更新时间。合集编号可以传给取合集里视频的接口。 | $0.02 一次 | `wechat_channels.users.collections.list` |
| [微信视频号合集里的视频](https://dataxapi.com/zh/apis/wechat_channels/collections/videos/list/?ref=gh-wechat-api) | 按合集编号取一页视频号合集里的视频，按合集自己的顺序（从最早的开始），每页 20 条：文案、作者、发布时间、点赞、评论、转发、收藏数。 | $0.02 一次 | `wechat_channels.collections.videos.list` |
| [微信视频号作品互动数据](https://dataxapi.com/zh/apis/wechat_channels/videos/metrics/?ref=gh-wechat-api) | 按作品编号取视频号作品最近的数字：点赞、评论、转发、收藏，带作品文案和发布账号。数字不是调用这一刻的，可能是几个小时前的，返回里写明是什么时候取的。比取整个作品详情便宜。 | $0.015 一次 | `wechat_channels.videos.metrics` |
| [微信视频号评论回复](https://dataxapi.com/zh/apis/wechat_channels/comments/replies/list/?ref=gh-wechat-api) | 按评论编号和作品编号取一页视频号评论下面的回复（二级评论）：正文、回复者、点赞数、发布时间、IP 属地、回复的是哪一条。一页约 10 条，可翻页。 | $0.015 一次 | `wechat_channels.comments.replies.list` |
| [微信视频号直播回放](https://dataxapi.com/zh/apis/wechat_channels/users/live_replays/list/?ref=gh-wechat-api) | 按视频号账号编号取它的直播回放，从新到旧，只给第一页（实测一页最多 48 条）：标题、开播时间、时长、封面，以及回放视频的点赞、评论、转发、收藏数（是回放这条视频的数，不是直播间的观看、在线或点赞人数）。 | $0.02 一次 | `wechat_channels.users.live_replays.list` |
| [视频号视频下载（文件地址和解密）](https://dataxapi.com/zh/apis/wechat_channels/videos/media/get/?ref=gh-wechat-api) | 给一条视频号作品的编号、分享链接或搜索结果的 export/ 编号，返回视频文件地址（带宽高、大小、时长）、封面，以及解密方法和密钥：视频号的文件只有开头 131072 字节加了密，按 decrypt 给的方法解开就是能播放的 MP4。地址和密钥要用同一次返回的那一对，不用带请求头；地址失效了再调一次即可。 | $0.02 一次 | `wechat_channels.videos.media.get` |
| [视频号视频转文字（逐字稿）](https://dataxapi.com/zh/apis/wechat_channels/videos/transcript/get/?ref=gh-wechat-api) | 给一条视频号作品的分享链接、编号或搜索结果的 export/ 编号，返回视频里说的话：全文、每一句的起止时间和现成的 SRT 字幕，连同文案、作者和时长；可以区分说话人。视频号文件的解密由我们完成，不用自己处理。每次收费，识别语音的另按视频分钟数收，没人说话不收。5 分钟以内的视频直接返回文字；超过 5 分钟、2 小时以内的先回一个凭证（job），过一会儿带着它再调这个接口取文字，按实际分钟数收，只在取到文字时收。 | $0.02 一次 | `wechat_channels.videos.transcript.get` |

### 微信搜一搜、微信指数和小程序

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [微信搜一搜综合搜索](https://dataxapi.com/zh/apis/wechat/posts/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里取一页结果，公众号文章和视频号视频混在一起，每条用 type 标明是文章还是视频；可按相关、最新或最热排、按发布时间筛，也可只搜文章或只搜视频：标题或文案、来源账号名称、发布时间，文章带链接（有的带阅读数档位），视频带点赞和收藏数。搜一搜不给账号编号。 | $0.02 一次 | `wechat.posts.search` |
| [微信指数](https://dataxapi.com/zh/apis/wechat/index/keywords/history/?ref=gh-wechat-api) | 按关键词取它最近 30 天的微信指数，一天一个数。微信指数是微信综合搜索、文章、朋友圈等算出的热度分，不是搜索次数，不能和抖音、小红书的指数比；日期是中国时间（UTC+8）的自然日。 | $0.1 一次 | `wechat.index.keywords.history` |
| [微信搜一搜推荐词](https://dataxapi.com/zh/apis/wechat/keywords/related/?ref=gh-wechat-api) | 按关键词取微信搜一搜在搜索框里给的联想推荐词，按搜一搜列出的顺序排，一次约 10 个。只有词和名次，没有指数。 | $0.1 一次 | `wechat.keywords.related` |
| [微信小程序搜索](https://dataxapi.com/zh/apis/wechat/miniprograms/search/?ref=gh-wechat-api) | 按搜索词在微信搜一搜里找小程序，取第一页（约 25 个）：名称、简介、图标、原始编号和 AppID、主体名称和是否认证、平台显示的最近使用人数、是否小游戏。 | $0.1 一次 | `wechat.miniprograms.search` |

### 备用版：原接口取不到时改调

| 接口 | 拿到什么 | 价格 | 编号 |
|---|---|---|---|
| [微信视频号账号资料（备用版）](https://dataxapi.com/zh/apis/wechat_channels/backup/users/get/?ref=gh-wechat-api) | wechat_channels.users.get 的备用版：参数和返回相同，另一来源，单独计价。不给作品数。 | $0.03 一次 | `wechat_channels.backup.users.get` |
| [微信视频号用户作品（备用版）](https://dataxapi.com/zh/apis/wechat_channels/backup/users/videos/list/?ref=gh-wechat-api) | wechat_channels.users.videos.list 的备用版：参数和返回相同，另一来源，单独计价。 | $0.06 一次 | `wechat_channels.backup.users.videos.list` |
| [微信搜一搜综合搜索（备用版）](https://dataxapi.com/zh/apis/wechat/backup/posts/search/?ref=gh-wechat-api) | wechat.posts.search 的备用版：参数和返回相同，另一来源，单独计价。视频不带收藏数。 | $0.1 一次 | `wechat.backup.posts.search` |
| [微信搜一搜视频号视频搜索（备用版）](https://dataxapi.com/zh/apis/wechat_channels/backup/videos/search/?ref=gh-wechat-api) | wechat_channels.videos.search 的备用版：参数和返回相同，另一来源，单独计价。不带收藏数。 | $0.1 一次 | `wechat_channels.backup.videos.search` |

## 真实返回长什么样

**微信公众号文章互动数据**（`wechat_mp.articles.metrics`，参数 `{"url":"https://mp.weixin.qq.com/s?__biz=MjM5MjAxNDM4MA==&mid=2667038683&idx=1&sn=0422127e651acd7f6cf6ef7e1cff04bc"}`），录下的真实返回，个人信息换成了 …：

```json
{
  "data": {
    "item": {
      "id": "…",
      "metrics": {
        "likes": 2235,
        "comments": 6,
        "shares": 9041,
        "favorites": 97,
        "views": 100001
      },
      "approximate": [
        {
          "field": "metrics.views",
          "kind": "lower_bound"
        }
      ]
    }
  }
}
```

每个接口都是同一种结构：列表在 `data.items`，单个在 `data.item`，下一页用 `page.next_cursor`，这次扣了多少在 `meta.billing.amount`，平台不给的字段为 `null` 并在 `meta.unavailable` 里写明。

## 快速开始

1. [拿一把 Key](https://dataxapi.com/zh/signin/?button=gh-wechat-api)（`dx_` 开头），放进环境变量：`export DATAXAPI_API_KEY=dx_...`
2. 调一次接口：

```bash
curl -G "https://api.dataxapi.com/v1/wechat_mp/accounts/articles/list" \
  -H "Authorization: Bearer $DATAXAPI_API_KEY" \
  --data-urlencode 'id=gh_13c97ab93ce8'
```

3. 或者跑 `examples/` 里的脚本。只用 Python 标准库（3.9 以上）；不加 `--yes` 只报价、不调用，加了才真跑，跑完告诉你实际花了多少：

| 脚本 | 做什么 | 先看要花多少 |
|---|---|---|
| [quickstart.py](examples/quickstart.py) | 给一个公众号名字，取它最近的文章，存成 CSV（发布时间、标题、链接、头条还是次条） | `cd examples && python3 quickstart.py 36氪` |
| [article_stats_csv.py](examples/article_stats_csv.py) | 一批文章链接，导出阅读、点赞、推荐、分享、收藏、评论数 | `cd examples && python3 article_stats_csv.py links.txt` |

更完整的小工具：

- [data-x-api/wechat-article-export](https://github.com/data-x-api/wechat-article-export)：公众号历史文章批量导出成 Markdown 和 CSV，带全文
- [data-x-api/wechat-rss](https://github.com/data-x-api/wechat-rss)：把公众号变成 RSS 订阅

## 接进 AI（MCP）

Claude Code：

```bash
claude mcp add --transport http --scope user dataxapi https://api.dataxapi.com/mcp --header "Authorization: Bearer $DATAXAPI_API_KEY"
```

Cursor、Cherry Studio、WorkBuddy 等支持远程 MCP 的客户端：

```json
{
  "mcpServers": {
    "dataxapi": {
      "url": "https://api.dataxapi.com/mcp",
      "headers": {
        "Authorization": "Bearer dx_..."
      }
    }
  }
}
```

接上以后直接用中文问，比如“帮我看看这个关键词最近一个月在抖音上的热度”。AI 花钱前可以先免费查接口和价格。也可以装成技能：`npx skills add data-x-api/skills`。

## 常见问题

**要不要扫码登录、公众号后台或 Cookie？**

都不要。只要一把 DataXAPI Key，也就不会碰到 `200013` 频率限制、不用换号。

**公众号的原始编号（gh_ 开头）怎么拿？**

用“微信公众号实时查找”按名字搜，结果里的 `id` 就是。

**阅读数显示 10万+ 怎么办？**

平台只给“10万+”时记成 100001，并在返回的 `approximate` 里标明这是下限。

**调用出错扣钱吗？**

不扣。每次返回里的 `meta.billing.amount` 写明这次扣了多少（美元）。

**同一篇文章两次拿到的链接不一样？**

公众号每次给的链接可能不同，去重请认文章的 `id`。

**怎么翻页？**

列表接口一次返回一页，把返回里的 `page.next_cursor` 作为 `cursor` 传回去取下一页，每一页单独计费。

## English

WeChat API: Official Account articles, reads and comments, Channels videos and accounts, WeChat Search and the WeChat index, through one key, no QR login, paid per call.

No platform account, cookie or QR login. Paid per call from $0.015; errors are not charged. Free trial: up to 333 calls, no card. [Get a key](https://dataxapi.com/signin/?button=gh-wechat-api) · [All endpoints](https://dataxapi.com/apis/?ref=gh-wechat-api) · MCP: `https://api.dataxapi.com/mcp`.

## License

MIT

<sub>接口和价格取自 DataXAPI 的目录 e43c3e964bcc3fc3、价格版本 21；以 [dataxapi.com/zh/apis](https://dataxapi.com/zh/apis/?ref=gh-wechat-api) 为准。</sub>
