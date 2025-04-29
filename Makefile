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

# Commands
PYTHON=python

# Targets
.PHONY: help clean html serve publish devserver

help:
	@echo 'Makefile for Pelican-based blog'
	@echo
	@echo 'Usage:'
	@echo '  make html         (build site with pelicanconf.py)'
	@echo '  make publish      (build production site with publishconf.py)'
	@echo '  make clean        (remove generated output files)'
	@echo '  make serve        (serve output/ folder locally)'
	@echo '  make devserver    (serve & rebuild on file changes)'
	@echo '  make help         (show this help)'

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
	cd $(OUTPUTDIR) && python -m http.server

devserver:
	$(PELICAN) --autoreload --listen $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE)
