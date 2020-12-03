
SOURCES=$(wildcard images/*.py)
SVG_TARGETS=$(SOURCES:%.py=%.svg)
PNG_TARGETS=$(SOURCES:%.py=%.png)
TARGETS=$(PNG_TARGETS) $(SVG_TARGETS)

.PHONY: default
default: $(TARGETS)

%.svg: %.py
	python sketch.py images/library.py $< > $@

%.png: %.svg
	cairosvg $< -o $@

clean:
	-rm -f $(TARGETS)