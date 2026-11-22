#!/usr/bin/env python3
"""给一个公众号名字，取它最近发的文章，存成 CSV：发布时间、标题、链接、头条还是次条、摘要。

    python3 quickstart.py 36氪 --pages 1          # 只报价，不调用
    python3 quickstart.py 36氪 --pages 1 --yes    # 真跑

先用名字找到公众号的原始编号（gh_ 开头，1 次），再一页一页取文章（每页 1 次）。都是 $0.02 一次，出错不收费。
名字对不上时不猜，会列出相近的号让你换。已经知道 gh_ 编号就直接填编号，省一次。
要导出全文和 Markdown，用 https://github.com/data-x-api/wechat-article-export 。
"""

from __future__ import annotations

import argparse
import csv
import sys
from decimal import Decimal
from pathlib import Path

from dataxapi import Api, ApiError, need_key

SOURCE = "gh-wechat-api"
SIGN_UP = f"https://dataxapi.com/zh/signin/?button={SOURCE}"
PRICE = Decimal("0.02")  # 现价见 https://dataxapi.com/zh/apis/wechat_mp/accounts/articles/list/?ref=gh-wechat-api
COLUMNS = ["发布时间", "标题", "链接", "位置", "摘要", "编号"]


def resolve(api: Api, account: str) -> str:
    if account.startswith("gh_"):
        return account
    items = api.call("wechat.accounts.search", query=account)["data"]["items"]
    for item in items:
        if item.get("name") == account:
            return item["id"]
    near = "、".join(f"{i.get('name')}（{i.get('id')}）" for i in items[:5]) or "没有"
    raise ApiError(f"没有名字完全是“{account}”的公众号。相近的：{near}")


def main() -> None:
    parser = argparse.ArgumentParser(description="取一个公众号最近发的文章")
    parser.add_argument("account", help="公众号名字，或 gh_ 开头的原始编号")
    parser.add_argument("--pages", type=int, default=1, help="取几页文章，每页一次调用")
    parser.add_argument("--out", default="wechat_articles.csv")
    parser.add_argument("--yes", action="store_true", help="确认调用（不加只报价）")
    args = parser.parse_args()

    calls = args.pages + (0 if args.account.startswith("gh_") else 1)
    print(f"最多调用 {calls} 次、${PRICE * calls}，出错不收费。")
    if not args.yes:
        print("加 --yes 真跑。")
        return
    need_key(SIGN_UP)

    api, rows, cursor = Api(SOURCE), [], None
    try:
        account_id = resolve(api, args.account)
    except ApiError as error:
        sys.exit(str(error))
    for page in range(args.pages):
        try:
            answer = api.call("wechat_mp.accounts.articles.list", id=account_id, cursor=cursor, view="full")  # full 才带头条还是次条，价格一样
        except ApiError as error:
            print(f"第 {page + 1} 页没取到：{error}（出错不扣费，已取到的照常保存）", file=sys.stderr)
            break
        for item in answer["data"]["items"]:
            ext = item.get("ext") or {}
            rows.append({
                "发布时间": item.get("published_at"),
                "标题": item.get("title"),
                "链接": item.get("url"),
                "位置": {1: "头条"}.get(ext.get("position"), f"第 {ext.get('position')} 条" if ext.get("position") else ""),
                "摘要": item.get("text"),
                "编号": item.get("id"),
            })
        cursor = (answer.get("page") or {}).get("next_cursor")
        if not cursor:
            break

    with Path(args.out).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"写好 {args.out}：{len(rows)} 篇，调用 {api.calls} 次，实际花费 ${api.charged}。")


if __name__ == "__main__":
    main()
