#########################
# Makefile for Pelican
#########################

# Variables
PELICAN=pelican
PELICANOPTS=

INPUTDIR=content
OUTPUTDIR=output
CONFFILE=pelicanconf.py
PUBLISHCONF=publishconf.py

CONFFILE_ZH=pelicanconf_zh.py
PUBLISHCONF_ZH=publishconf_zh.py

# Commands
PYTHON=python

# Targets
.PHONY: help clean html serve publish devserver html-zh publish-zh publish-all

help:
	@echo 'Makefile for Pelican-based blog'
	@echo
	@echo 'Usage:'
	@echo '  make html         (build English site with pelicanconf.py)'
	@echo '  make html-zh      (build Chinese site with pelicanconf_zh.py)'
	@echo '  make html-all     (build both English and Chinese sites)'
	@echo '  make publish      (build production English site with publishconf.py)'
	@echo '  make publish-zh   (build production Chinese site with publishconf_zh.py)'
	@echo '  make publish-all  (build production English and Chinese sites)'
	@echo '  make clean        (remove generated output files)'
	@echo '  make serve        (serve output/ folder locally)'
	@echo '  make devserver    (serve & rebuild on file changes)'
	@echo '  make help         (show this help)'

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

html-zh:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE_ZH)

html-all: html html-zh

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)

publish-zh:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF_ZH)

publish-all: publish publish-zh

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
	cd $(OUTPUTDIR) && python -m http.server

devserver:
	$(PELICAN) --autoreload --listen $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)
