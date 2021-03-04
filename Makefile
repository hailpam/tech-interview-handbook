
.PHONY: run all

run:
	for d in ./*; \
	do \
	  echo "top folder: $$d"; \
	  if [ -f $$d/Makefile ]; \
	  then \
	    make -C $$d; \
	  fi \
	done

all: run