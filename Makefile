test:
	./run_tests.sh
docs:
	rm -rf docs
	pdoc3 --html --html-dir docs deadsimplekv
	cd docs/deadsimplekv; \
		mv * ../
.PHONY: docs

