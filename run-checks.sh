if pylint src tests > /dev/null 2>&1; then
    echo "[CHECKS] [PASS] Pylint"
else
    pylint src tests
    echo "[CHECKS] [FAIL] Pylint"
fi

if python3 -m unittest discover -s ./tests -p 'test_*.py' > /dev/null 2>&1; then
    echo "[CHECKS] [PASS] Unit tests"
else
    python3 -m unittest discover -s ./tests -p 'test_*.py'
    echo "[CHECKS] [FAIL] Unit tests"
fi
