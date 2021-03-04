

.PHONY: run all

run:
	for d in ./*; \
	do \
	  echo "folder: $$d"; \
	  make -C $$d; \
	  done

all: run