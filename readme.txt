测试：python3 -m unittest discover -s tests/cascade_states -p 'test_*.py'
构建：python3 -m compileall -q colorectal_cascade
验收：python3 -m colorectal_cascade.commands.cascade fixtures/demo.json --db /tmp/colorectal_cascade-acceptance.sqlite3
