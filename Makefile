.PHONY: all pdf check clean
all: pdf
pdf check clean:
	$(MAKE) -C Results/QuantitativeIsoperimetric $@
