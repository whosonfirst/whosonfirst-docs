docs:
	bin/mk-docs.py

readme: docs
	touch README.tmp
	cat boilerplate/INTRO.md >> README.tmp
	echo "" >> README.tmp
	cat DOCS.md >> README.tmp
	echo "" >> README.tmp
	cat boilerplate/OUTRO.md >> README.tmp
	mv README.tmp README.md
