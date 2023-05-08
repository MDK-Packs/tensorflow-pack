./clean.sh
#./fetch_upstream.sh
python3 create_example_projects.py $1
cp .cdefault.yml ./out/.cdefault.yml
cp -R layer ./out/layer
