from __future__ import annotations
import argparse
import json
from colorectal_cascade.service import run_fixture

def main() -> int:
    parser=argparse.ArgumentParser(description='结直肠癌筛查级联闭环引擎')
    parser.add_argument("fixture")
    parser.add_argument("--db",default="/tmp/colorectal_cascade.sqlite3")
    args=parser.parse_args()
    result=run_fixture(args.fixture,args.db)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True))
    return 0

if __name__ == "__main__": raise SystemExit(main())
