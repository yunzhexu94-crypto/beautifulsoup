#!/bin/bash
# Script to run all M2 tasks
# This script demonstrates all the commands from M2-README.md

cd /home/runner/workspace/beautifulsoup
export PYTHONPATH=/home/runner/workspace/beautifulsoup:$PYTHONPATH

echo "=========================================="
echo "Running All M2 Tasks"
echo "=========================================="
echo ""

echo "=== Task 2: Finding Links ==="
python apps/m2/task2.py apps/m2/test.html
echo ""

echo "=== Task 3: Listing All Tags ==="
python apps/m2/task3.py apps/m2/test.html
echo ""

echo "=== Task 4: Finding Tags with ID ==="
python apps/m2/task4.py apps/m2/test.html
echo ""

echo "=== Task 6: SoupReplacer Demo ==="
python apps/m2/task6.py apps/m2/test.html
echo ""

echo "=========================================="
echo "All tasks completed successfully!"
echo "=========================================="
