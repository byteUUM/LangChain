#!/bin/bash
# Fix Hermes agent's broken cwd issue
cd /home/conwy/learn/lang-chain

echo "=== Remote Config ==="
git remote -v

echo ""
echo "=== Status ==="
git status

echo ""
echo "=== Adding github remote ==="
git remote add github git@github.com:byteUUM/LangChain.git 2>/dev/null || git remote set-url github git@github.com:byteUUM/LangChain.git

echo ""
echo "=== git add . ==="
git add .

echo ""
echo "=== git commit ==="
git commit -m "提示词模板"

echo ""
echo "=== git push gitee ==="
git push gitee

echo ""
echo "=== git push github ==="
git push github

echo ""
echo "=== DONE ==="
