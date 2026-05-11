#!/bin/bash
# Fix: the hermes session's CWD was deleted. 
# This script runs in a fresh shell process.
mkdir -p /home/conwy/learn/lang-chain-bak
cd /home/conwy/learn/lang-chain

echo "=== git remote -v ==="
git remote -v

echo ""
echo "=== Add/update github remote ==="
git remote add github git@github.com:byteUUM/LangChain.git 2>/dev/null || git remote set-url github git@github.com:byteUUM/LangChain.git

echo ""
echo "=== git remote -v (after) ==="
git remote -v

echo ""
echo "=== git add . ==="
git add .

echo ""
echo "=== git commit ==="
git -c user.name=conwy -c user.email=conwy@example.com commit -m "提示词模板"

echo ""
echo "=== git push gitee ==="
git push gitee

echo ""
echo "=== git push github ==="
git push github

echo ""
echo "=== ALL DONE ==="
