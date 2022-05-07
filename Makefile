
.PHONY: run all

run: display
	for d in ./*; \
	do \
	  echo "top folder: $$d"; \
	  if [ -f $$d/Makefile ]; \
	  then \
	    make -C $$d; \
	  fi \
	done

display:
	tree | grep .py | grep -v __init__ | wc -l

all: run