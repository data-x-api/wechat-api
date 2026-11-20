#!/usr/bin/env python3
"""一批公众号文章的阅读、点赞、推荐、分享、收藏、评论数导出成 CSV，读的是此刻的数。

    python3 article_stats_csv.py links.txt          # 只报价，不调用
    python3 article_stats_csv.py links.txt --yes    # 真跑

links.txt 一行一条文章链接，原样粘贴即可（带 __biz、mid、idx、sn 的长链接）。每篇 $0.02，出错不收费；
没取到的那篇写进 CSV 的“没取到”一列，其余照常。阅读数超过 10 万时平台只给“10万+”，这里记 100001，并在“约数”一列标出。
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
PRICE = Decimal("0.02")  # 现价见 https://dataxapi.com/zh/apis/wechat_mp/articles/metrics/
COLUMNS = ["链接", "阅读", "点赞", "推荐", "分享", "收藏", "评论", "约数", "没取到"]


def main() -> None:
    parser = argparse.ArgumentParser(description="公众号文章互动数导出成 CSV")
    parser.add_argument("links", help="一行一条文章链接的文本文件")
    parser.add_argument("--out", default="wechat_article_stats.csv")
    parser.add_argument("--yes", action="store_true", help="确认调用（不加只报价）")
    args = parser.parse_args()

    links = [l.strip() for l in Path(args.links).read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"{len(links)} 篇文章：调用 {len(links)} 次，最多 ${PRICE * len(links)}，出错不收费。")
    if not args.yes:
        print("加 --yes 真跑。")
        return
    need_key(SIGN_UP)

    api = Api(SOURCE)
    with Path(args.out).open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for n, link in enumerate(links, 1):
            row = {"链接": link}
            try:
                item = api.call("wechat_mp.articles.metrics", url=link, view="full")["data"]["item"]  # full 才带推荐数，价格一样
                m = item.get("metrics") or {}
                row.update({
                    "阅读": m.get("views"), "点赞": m.get("likes"), "推荐": (item.get("ext") or {}).get("recommends"),
                    "分享": m.get("shares"), "收藏": m.get("favorites"), "评论": m.get("comments"),
                    "约数": "、".join(a.get("field", "") for a in item.get("approximate") or []),
                })
            except ApiError as error:
                row["没取到"] = str(error)
            writer.writerow(row)
            print(f"  {n}/{len(links)} {row.get('阅读') if not row.get('没取到') else '没取到'}", file=sys.stderr)
    print(f"写好 {args.out}。实际花费 ${api.charged}。")


if __name__ == "__main__":
    main()
