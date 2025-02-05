#  build dependencies

pip wheel --wheel-dir=./wheels -r requirement.txt

#  Install project and dependencies
# pip install --no-index --find-links=./wheels -r requirement.txt # (for local setup)
pip install -e . #(for production)

#  Build project wheel
python setup.py bdist_wheel